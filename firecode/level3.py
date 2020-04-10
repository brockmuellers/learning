#!/usr/bin/python3

from structures import Interval
from structures import ListNode
from structures import TreeNode


class MirrorBinaryTree:
    def mirror(self, root):
        if root is None:
            return None

        left = root.left
        right = root.right
        root.left = right
        root.right = left

        self.mirror(left)
        self.mirror(right)

        return root

    def test(self):
        node4 = TreeNode(4, None, None)
        node5 = TreeNode(5, None, None)
        node6 = TreeNode(6, None, None)
        node7 = TreeNode(7, None, None)
        node2 = TreeNode(2, node4, node5)
        node3 = TreeNode(3, node6, node7)
        node1 = TreeNode(1, node2, node3)

        self.mirror(node1)

        assert node1.left == node3
        assert node1.right == node2
        assert node3.left == node7
        assert node3.right == node6
        assert node2.left == node5
        assert node2.right == node4

        print("MirrorBinaryTree")


class CyclicListSpaceON:
    # Is linked list cyclic? Space complexity O(n)
    def is_cyclic(self, head):
        visited_set = set()

        while head is not None:
            if head in visited_set:
                return True

            visited_set.add(head)
            head = head.next

        return False

    def test(self):
        assert self.is_cyclic(None) is False

        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)

        node1.next = node2
        node2.next = node3
        node3.next = node4

        assert self.is_cyclic(node1) is False

        node4.next = node1

        assert self.is_cyclic(node1) is True

        print("CyclicListSpaceON")


class MergeRanges:
    # Merge overlapping intervals
    def merge_intervals(self, intervals):
        if (intervals is None) or (len(intervals) < 2):
            return intervals

        sorted_intervals = sorted(intervals, key=lambda i: i.start)
        results = []

        acc_interval = sorted_intervals[0]

        for i in range(1, len(sorted_intervals)):
            new_interval = sorted_intervals[i]

            if (new_interval.start <= acc_interval.end):
                acc_interval = Interval(
                    acc_interval.start,
                    max(acc_interval.end, new_interval.end))
            else:
                results.append(acc_interval)
                acc_interval = new_interval

        results.append(acc_interval)

        return results

    def test(self):
        assert self.merge_intervals(None) is None
        assert self.merge_intervals([]) == []
        assert self.merge_intervals([Interval(1, 2)]) == [Interval(1, 2)]

        intervals1 = [Interval(1, 3), Interval(6, 8), Interval(2, 5), Interval(6, 7)]
        expected1 = [Interval(1, 5), Interval(6, 8)]

        assert self.merge_intervals(intervals1) == expected1

        intervals2 = [Interval(6, 7), Interval(1, 3)]
        expected2 = [Interval(1, 3), Interval(6, 7)]

        assert self.merge_intervals(intervals2) == expected2

        print("MergeRanges")


class RotateSquareImageClockwise:
    def rotate_square_image_cw(self, matrix):
        for i in range(1, len(matrix)):
            for j in range(0, i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        num_flips = len(matrix) // 2
        for i in range(len(matrix)):
            for j in range(num_flips):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][-(j + 1)]
                matrix[i][-(j + 1)] = temp

    def test(self):
        img = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.rotate_square_image_cw(img)

        expected = [[6, 3, 0], [7, 4, 1], [8, 5, 2]]
        assert img == expected

        print("RotateSquareImageClockwise")


class CountHalfNodes:
    # Count nodes with only one child in binary tree
    def number_of_half_nodes(self, root):
        if root is None:
            return 0

        is_half_node = 0
        if (root.left is not None and root.right is None):
            is_half_node = 1
        elif (root.left is None and root.right is not None):
            is_half_node = 1

        return is_half_node + \
            self.number_of_half_nodes(root.right) + \
            self.number_of_half_nodes(root.left)

    def test(self):
        node9 = TreeNode(9, None, None)
        node8 = TreeNode(8, None, None)
        node4 = TreeNode(4, node9, None)
        node5 = TreeNode(5, None, None)
        node6 = TreeNode(6, None, node8)
        node7 = TreeNode(7, None, None)
        node2 = TreeNode(2, node4, node5)
        node3 = TreeNode(3, node6, node7)
        node1 = TreeNode(1, node2, node3)

        assert self.number_of_half_nodes(node1) == 2

        print("CountHalfNodes")


if __name__ == "__main__":
    MirrorBinaryTree().test()
    CyclicListSpaceON().test()
    MergeRanges().test()
    RotateSquareImageClockwise().test()
    CountHalfNodes().test()
