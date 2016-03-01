require_relative 'data_queue.rb'

class BinaryTree
  attr_accessor :value, :left, :right

  def initialize(value, left, right)
    @value = value
    @left = left
    @right = right
  end

  def print_node
    left = @left ? @left.value : 'nil'
    right = @right ? @right.value : 'nil'
    puts "Value: #{@value}, Left: #{left}, Right: #{right}"
  end

  def print_all_nodes
    left = @left ? @left.print_all_nodes : nil
    right = @right ? @right.print_all_nodes : nil

    if left || right
      [@value, left, right]
    else
      @value
    end
  end

  ### CREATION ###

  def self.create_binary_tree(structure)
    # structure: [root, left, right]
    # [1, [2, [4, 7, 8], [5, nil, 9]], [3, 6, nil]]
    # --------1--------
    # ----2-------3----
    # --4---5---6------
    # -7-8---9---------
    # note: might be better to use standardized structure like adjacency list
    if structure.is_a? Integer # input is a leaf
      BinaryTree.new(structure, nil, nil)
    elsif structure.is_a? Array # input is a tree
      left = create_binary_tree(structure[1])
      right = create_binary_tree(structure[2])
      BinaryTree.new(structure[0], left, right)
    end
  end

  def self.create_random_binary_tree(levels, side = nil)
    if levels > 0
      left = create_random_binary_tree(levels-1, 'left')
      right = create_random_binary_tree(levels-1, 'right')
      BinaryTree.new(rand(100), left, right)
    end
  end

  ### DFS TRAVERSAL ###

  def in_order_traversal
    if @left
      @left.in_order_traversal
    end

    puts @value

    if @right
      @right.in_order_traversal
    end
  end

  def post_order_traversal
    if @left
      @left.post_order_traversal
    end

    if @right
      @right.post_order_traversal
    end

    puts @value
  end

  def pre_order_traversal
    puts @value

    if @left
      @left.pre_order_traversal
    end

    if @right
      @right.pre_order_traversal
    end
  end

  ### BFS traversal ###

  def breadth_first_traversal(queue = DataQueue.new)
    puts @value

    if @left
      queue.enqueue @left
    end

    if @right
      queue.enqueue @right
    end

    next_node = queue.dequeue

    if next_node
      next_node.breadth_first_traversal(queue)
    end
  end

  ### ITERATIVE TRAVERSAL ###

  def self.iterative_in_order_traversal(root)
    stack = []
    node = root

    while !stack.empty? || node
      if node
        stack.push(node)
        node = node.left
      else
        node = stack.pop
        puts node.value
        node = node.right
      end
    end
  end


  def self.iterative_breadth_first_traversal(root, queue = DataQueue.new)
    node = root

    while node
      puts node.value

      if node.left
        queue.enqueue node.left
      end

      if node.right
        queue.enqueue node.right
      end

      node = queue.dequeue
    end
  end
end
