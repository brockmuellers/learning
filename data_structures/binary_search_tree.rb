require_relative 'binary_tree.rb'

class BinarySearchTree < BinaryTree
  def initialize(value, left, right, self_balancing = nil)
    @self_balancing = self_balancing
    super value, left, right
  end

  def self.generate_tree(values)
    sorted = values.sort
    root_index = (values.length-1)/2

    if sorted.length > 1
      right_values = sorted[(root_index+1)..-1]
    else
      right_values = []
    end

    if sorted.length > 2
      left_values = sorted[0..root_index-1]
    else
      left_values = []
    end

    left_tree = left_values.empty? ? nil : BinarySearchTree.generate_tree(left_values)
    right_tree = right_values.empty? ? nil : BinarySearchTree.generate_tree(right_values)

    BinarySearchTree.new(sorted[root_index], left_tree, right_tree)
  end

  def balance_tree
    # not implemented
    case @self_balancing
    when :avl
    when :splay
    end
  end

  def insert_node(value)
    if value < @value
      if @left
        @left.insert_node(value)
      else
        @left = BinarySearchTree.new(value, nil, nil)
      end
    elsif value > @value
      if @right
        @right.insert_node(value)
      else
        @right = BinarySearchTree.new(value, nil, nil)
      end
    end

    if @self_balancing
      balance_tree
    end

    self
  end

  def remove_node(value) # this could use some cleanup
    # replace node with successor (min value on right subtree)
    # if no right subtree, replace node with left subtree
    node_and_parent = search_with_parent(value)
    node = node_and_parent[0]
    parent = node_and_parent[1]
    side = node_and_parent[2]
    puts node.value
    puts parent.value
    puts side

    if node.right # if there is a right subtree
      left_child = node.left
      right_child = node.right

      successor = node.right.delete_min_node(node)
      successor.left = left_child
      unless successor == right_child
        successor.right = right_child
      end

      if side == 'left' # node is left child
        parent.left = successor
      elsif side == 'right' # node is right child
        parent.right = successor
      end
    else
      if side == 'left' # node is left child
        parent.left = node.left
      elsif side == 'right' # node is right child
        parent.right = node.left
      end
    end

    if @self_balancing
      balance_tree
    end
  end

  def search(value)
    if value == @value
      self
    elsif value < @value
      if @left
        @left.search value
      end
    else
      if @right
        @right.search value
      end
    end
  end

  # helper methods

  def delete_min_node(parent = nil)
    if @left # find leftmost value
      @left.delete_min_node(self)
    elsif parent # if isn't the top node
      parent.left = @right
      @right = nil

      self
    end
  end

  def search_with_parent(value, parent = nil, side = nil)
    if value == @value
      [self, parent, side]
    elsif value < @value
      if @left
        @left.search_with_parent value, self, 'left'
      end
    else
      if @right
        @right.search_with_parent value, self, 'right'
      end
    end
  end
end
