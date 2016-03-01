# Calling this DataQueue to avoid interference with Ruby Queue class
class DataQueue
  def initialize
    @store = []
  end

  def dequeue
    @store.shift
  end

  def enqueue(elements)
    @store.push *elements
  end
end
