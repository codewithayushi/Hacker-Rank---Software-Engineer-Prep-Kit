#10. One-Pass Removal of k-th Node from End

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')


def removeKthNodeFromEnd(head, k):
    # Write your code here
    if head is None:
        return head
    
    # Find length
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    
    # If k is invalid (>= length or < 0)
    if k < 0 or k >= length:
        return head
    
    # k is 0-indexed from end
    # Convert to position from start (0-indexed)
    pos_from_start = length - 1 - k
    
    # Remove head
    if pos_from_start == 0:
        return head.next
    
    # Find node before target
    current = head
    for _ in range(pos_from_start - 1):
        current = current.next
    
    current.next = current.next.next
    return head

if __name__ == '__main__':
    head_count = int(input().strip())

    head = SinglyLinkedList()

    for _ in range(head_count):
        head_item = int(input().strip())
        head.insert_node(head_item)

    k = int(input().strip())

    result = removeKthNodeFromEnd(head.head, k)

    print_singly_linked_list(result, '\n')
    print()
