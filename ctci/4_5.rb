require_relative './data_structures/binary_search_tree.rb'
require_relative './data_structures/binary_tree.rb'

def tree_is_bst?(tree)
  if tree == nil
    true
  elsif tree.left && (tree.left.value > tree.value)
    false
  elsif tree.right && (tree.right.value < tree.value)
    false
  elsif tree_is_bst?(tree.left) && tree_is_bst?(tree.right)
    true
  end
end

bt = BinaryTree.create_binary_tree([1, [2, [4, 7, 8], [5, nil, 9]], [3, 6, nil]])
puts bt.print_all_nodes.to_s
puts "Is this a BST? #{tree_is_bst?(bt)}"

bst = BinarySearchTree.generate_tree([4,66,7,2,124,746,88,0,0])
puts bst.print_all_nodes.to_s
puts "Is this a BST? #{tree_is_bst?(bst)}"
