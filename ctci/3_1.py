class ArrayThreeStacks(object):
  def __init__(self, stacksize):
    self.stacks = [None]*(3*stacksize + 3)

  def push(self, stacknum, element):
    pointer = self.stack_pointer(stacknum)
    if pointer == None:
      pointer = self.stacksize()*(stacknum-1)-1
    if self.stacks[pointer+1]:
      print('Out of space')
    else:
      self.stacks[pointer+1] = element
      self.stacks[-stacknum] = pointer+1

  def pop(self, stacknum):
    pointer = self.stack_pointer(stacknum)
    if pointer == None:
      print('this stack is empty')
    else:
      element = self.stacks[pointer]
      self.stacks[pointer] = None
      self.stacks[-stacknum] = pointer-1
      print(element)

  def stack_pointer(self, stacknum):
    # stack[-1] is stack1, stack[-2] is stack2, etc
    return self.stacks[-stacknum]

  def stacksize(self):
    return int(len(self.stacks)/3-1)

  # for testing
  def print_stack(self, stacknum):
    start = self.stacksize()*(stacknum-1)
    end = self.stacksize()*stacknum - 1
    print(self.stacks[start:end])



stacks_array = ArrayThreeStacks(10)
stacks_array.print_stack(2)
stacks_array.push(2, 'a')
stacks_array.print_stack(2)
stacks_array.push(2, 'c')
stacks_array.print_stack(2)
stacks_array.pop(2)
stacks_array.print_stack(2)
# storing stacks next to each other
# space is linear, pop is linear, push is linear
