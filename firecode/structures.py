class TreeNode:
    # Binary tree
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def __eq__(self, other):
        if (self is None and other is None):
            return True
        if (self is None or other is None):
            return False
        return self.data == other.data and \
            self.left == other.left and \
            self.right == other.right


class ListNode:
    # Linked list
    def __init__(self, data):
        self.data = data
        self.next = None


class Interval:
    # Range with start and end
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end
