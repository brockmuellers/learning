# Doubly-linked list
require_relative 'node.rb'

class LinkedList
  attr_accessor :head, :tail

  def initialize(node)
    @head = node
    @tail = node
  end

  def add(node)
    if @tail
      @tail.child = node
      node.parent = @tail
      @tail = node
    else
      @head = node
      @tail = node
    end
  end

  def remove(value)
    node = search(value)

    if node
      if node = @head && node = @tail # there's only one node
        @head = nil
        @tail = nil
      elsif node = @head
        @head = node.child
        node.child.parent = nil
      elsif node = @tail
        @tail = node.parent
        node.parent.child = nil
      else
        node.parent.child = node.child
        node.child.parent = node.parent
      end

      node.parent = nil
      node.child = nil

      node.value # return node's value if removed
    end
  end

  def search(value)
    node = @head

    while node && (node.value != value)
      node = node.child
    end

    node
  end


  def print_all_nodes
    node = @head
    node_list = []

    while node
      node_list.push(node.value)
      node = node.child
    end

    node_list
  end
end
