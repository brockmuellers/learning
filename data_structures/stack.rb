# Note: in Ruby, Array#push and #pop work as a stack
class Stack
  def initialize(size = 10)
    # @size = size
    # @stack_array = Array.new(size)
    # @pointer = 0
    @store = []
  end

  def pop
    @store.pop
  end

  def push(element)
    @store.push(element)
  end
end
