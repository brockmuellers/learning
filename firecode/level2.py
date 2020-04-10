#!/usr/bin/python3

import queue
from structures import ListNode
from structures import TreeNode


class DeleteCircularTail:
    # Delete tail of a circular linked list
    def delete_at_tail(self, head):
        previous = head
        pointer = head.next
        tail = None

        while tail is None:
            if pointer.next == head:
                tail = pointer
                break

            previous = previous.next
            pointer = pointer.next

        previous.next = head
        return head

    def test(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node1

        result = self.delete_at_tail(node1)

        assert result == node1
        assert node1.next == node2
        assert node2.next == node3
        assert node3.next == node1

        print("DeleteCircularTail")


class DeleteCircularHead:
    def delete_at_head(self, head):
        if (head is None) or (head.next == head):
            return None

        pointer = head

        while (pointer.next != head):
            pointer = pointer.next

        pointer.next = head.next

        return head.next

    def test(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node1

        result = self.delete_at_head(node1)

        assert result == node2
        assert node2.next == node3
        assert node3.next == node4
        assert node4.next == node2

        print("DeleteCircularHead")


class IsAnagram:
    # Check if two strings are anagrams
    def is_anagram(self, input1, input2):
        if (input1 is None) or (input2 is None):
            return False

        if len(input1) != len(input2):
            return False

        char_counts_1 = self._count_chars(input1)
        char_counts_2 = self._count_chars(input2)

        if (char_counts_1 != char_counts_2):
            return False

        return True

    def _count_chars(self, input_str):
        char_counts = {}

        for c in input_str:
            if c in char_counts:
                char_counts[c] = char_counts[c] + 1
            else:
                char_counts[c] = 1

        return char_counts

    def test(self):
        assert self.is_anagram("abc", "cab") is True
        assert self.is_anagram("b", "b") is True
        assert self.is_anagram("bd", "cb") is False
        assert self.is_anagram("abc", "ccb") is False
        assert self.is_anagram(None, None) is False
        print("IsAnagram")


class ValidateBST:
    # Validate that a binary tree is a binary search TreeNode
    def validate_BST(self, root):
        return self.validate(root, float('-inf'), float('inf'))

    def validate(self, root, mini, maxi):
        if root is None:
            return True

        if root.left is not None:
            if not (root.left.data < root.data and root.left.data > mini):
                return False

        if root.right is not None:
            if not (root.right.data > root.data and root.right.data < maxi):
                return False

        return self.validate(root.left, mini, root.data) and \
            self.validate(root.right, root.data, maxi)

    def test(self):
        self._test_case_1()
        self._test_case_2()
        print("ValidateBST")

    def _test_case_1(self):
        node14 = TreeNode(14, None, None)
        node18 = TreeNode(18, None, None)
        node30 = TreeNode(30, node14, node18)
        node15 = TreeNode(15, None, None)
        node20 = TreeNode(20, node30, node15)

        assert self.validate_BST(node20) is False

    def _test_case_2(self):
        node14 = TreeNode(14, None, None)
        node18 = TreeNode(18, None, None)
        node15 = TreeNode(15, node14, node18)
        node30 = TreeNode(30, None, None)
        node20 = TreeNode(20, node15, node30)

        assert self.validate_BST(node20) is True


class NumberOfLeaves:
    # Count number of leaf nodes in a binary tree
    def number_of_leaves(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        return self.number_of_leaves(root.left) + \
            self.number_of_leaves(root.right)

    def test(self):
        node8 = TreeNode(8, None, None)
        node9 = TreeNode(9, None, None)
        node4 = TreeNode(4, node8, node9)
        node5 = TreeNode(5, None, None)
        node6 = TreeNode(6, None, None)
        node7 = TreeNode(7, None, None)
        node2 = TreeNode(2, node4, node5)
        node3 = TreeNode(3, node6, node7)
        node1 = TreeNode(1, node2, node3)

        assert self.number_of_leaves(node1) == 5
        print("NumberOfLeaves")


class TransposeMatrix:
    # Transpose a matrix in place
    def transpose_matrix(self, matrix):
        for i in range(len(matrix) - 1):
            for j in range(i + 1, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

    def test(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        expected = [
            [1, 5, 9, 13],
            [2, 6, 10, 14],
            [3, 7, 11, 15],
            [4, 8, 12, 16]
        ]

        self.transpose_matrix(matrix)

        assert matrix == expected

        print("TransposeMatrix")


class FindMaxBinaryTree:
    # Recursively find max element in binary tree
    def find_max(self, root):
        if root is None:
            return float("-inf")
        return max(root.data, self.find_max(root.left), self.find_max(root.right))

    def test(self):
        node4 = TreeNode(4, None, None)
        node5 = TreeNode(5, None, None)
        node6 = TreeNode(6, None, None)
        node7 = TreeNode(7, None, None)
        node2 = TreeNode(2, node4, node5)
        node3 = TreeNode(3, node6, node7)
        node1 = TreeNode(1, node2, node3)

        assert self.find_max(node1) == 7

        print("FindMaxBinaryTree")


class IsListEven:
    # Check if linked list length is even or odd
    def is_list_even(self, head):
        count = 0

        pointer = head

        while (pointer is not None):
            count += 1
            pointer = pointer.next

        return (count % 2) == 0

    def test(self):
        assert self.is_list_even(None) is True

        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node1.next = node2
        node2.next = node3
        node3.next = node4

        assert self.is_list_even(node1) is True

        node5 = ListNode(5)
        node4.next = node5

        assert self.is_list_even(node1) is False

        print("IsListEven")


class CompressString:
    # Compress string
    def compress_string(self, text):
        result = ""
        count = 0

        for i in range(len(text)):
            c = text[i]
            count += 1

            if (i == len(text) - 1 or c != text[i + 1]):
                result += c
                if count > 1:
                    result += str(count)

                count = 0

        return result

    def test(self):
        assert self.compress_string("abc") == "abc"
        assert self.compress_string("aaabbbbbcccc") == "a3b5c4"
        assert self.compress_string("aabbbbccc") == "a2b4c3"

        print("CompressString")


class IntIsPalindrome:
    # Is an integer a palindrome
    def is_palindrome(self, x):
        if x < 0:
            return False

        temp = x
        reverse = 0

        while (temp > 0):
            lowest_digit = temp % 10
            reverse = reverse * 10 + lowest_digit
            temp = temp // 10

        return reverse == x

    def test(self):
        assert self.is_palindrome(-1) is False
        assert self.is_palindrome(0) is True
        assert self.is_palindrome(121) is True
        assert self.is_palindrome(1221) is True
        assert self.is_palindrome(1223) is False

        print("IntIsPalindrome")


class SumBinaryTree:
    def sum_tree(self, root):
        if root is None:
            return 0

        return root.data + self.sum_tree(root.left) + self.sum_tree(root.right)

    def test(self):
        node14 = TreeNode(14, None, None)
        node18 = TreeNode(18, None, None)
        node30 = TreeNode(30, node14, node18)
        node15 = TreeNode(15, None, None)
        node20 = TreeNode(20, node30, node15)

        assert self.sum_tree(node20) == 97

        print("SumBinaryTree")


class FindBinaryTreeNode:
    # Iteratively find a node in a binary tree
    def find_node(self, root, val):
        nodes_to_visit = queue.Queue()
        nodes_to_visit.put(root)

        while not nodes_to_visit.empty():
            head = nodes_to_visit.get()

            if head is None:
                continue

            if head.data == val:
                return head

            nodes_to_visit.put(head.left)
            nodes_to_visit.put(head.right)

        return None

    def test(self):
        node14 = TreeNode(14, None, None)
        node18 = TreeNode(18, None, None)
        node30 = TreeNode(30, node14, node18)
        node15 = TreeNode(15, None, None)
        node20 = TreeNode(20, node30, node15)

        assert self.find_node(node20, 18) == node18

        print("FindBinaryTreeNode")


if __name__ == "__main__":
    DeleteCircularTail().test()
    DeleteCircularHead().test()
    IsAnagram().test()
    ValidateBST().test()
    NumberOfLeaves().test()
    TransposeMatrix().test()
    IsListEven().test()
    CompressString().test()
    IntIsPalindrome().test()
    SumBinaryTree().test()
    FindBinaryTreeNode().test()
