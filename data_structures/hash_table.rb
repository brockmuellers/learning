require_relative 'linked_list.rb'

class HashTable
  # Uses nested arrays for default collision reduction strategy; better choices might be:
  # * Linked lists
  # * Linear probing (make the table larger and store colliding values in next available position)
  def initialize(size, function: nil, collision_type: :arrays)
    @size = size
    @function = function || lambda { |value| value.hash }
    @collision_type = collision_type

    case collision_type
    when :arrays
      @table = Array.new(size) { [] }
    when :linked_lists
      @table = Array.new(size) { LinkedList.new(nil) }
    when :linear_probing
      @table = Array.new(size*2) # need a larger table for N elements (though maybe this is too large)
    end
  end

  def add(value)
    hash_value = hash(value)

    case @collision_type
    when :arrays
      unless @table[hash_value].include?(value)
        @table[hash_value] << value
      end

    when :linked_lists
      unless @table[hash_value].search(value)
        @table[hash_value].add(Node.new(value))
      end

    when :linear_probing
      unless @table.include?(value)
        if @table.include?(nil)
          index = hash_value

          if @table[index] # the hash element is already filled
            index = next_table_index(index)

            while @table[index] && (index != hash_value) # find next empty element
              index = next_table_index(index)
            end
          end

          @table[index] = value
        else
          raise "Hash table is full."
        end
      end
    end
  end

  def hash(value)
    @function.call(value) % @table.length
  end

  def remove(value)
    hash_value = hash(value)

    case @collision_type
    when :arrays
      @table[hash(value)].delete(value)

    when :linked_lists
      if @table[hash(value)]
        @table[hash(value)].remove(value)
      end

    when :linear_probing
      index = search(value)

      if index
        @table[index] = nil
        value
      end
    end
  end

  def search(value) # returns index or nil
    hash_value = hash(value)

    case @collision_type
    when :arrays
      if @table[hash_value].include?(value)
        hash_value
      end

    when :linked_lists
      if @table[hash_value].search(value)
        hash_value
      end


    when :linear_probing # this is a gross implementation
      index = hash_value

      if @table[index] != value # search other elements for the value
        index = next_table_index(index)

        while (@table[index] != value) && (index != hash_value)
          index = next_table_index(index)
        end
      end

      if @table[index] == value
        index
      end
    end
  end

  private

  def next_table_index(current)
    if current >= @table.length - 1 # at end of table; need to loop back to beginning
      0
    else
      current + 1
    end
  end
end
