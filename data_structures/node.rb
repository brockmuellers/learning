class Node
  attr_accessor :value, :parent, :child

  def initialize(value, parent: nil, child: nil)
    @value = value
    @parent = parent
    @child = child
  end
end
