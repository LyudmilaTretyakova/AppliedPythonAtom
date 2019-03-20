#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    if head is None:
        return head
    node = head
    prev = None
    while node is not None:
        tmp = node.next_node
        node.next_node = prev
        prev = node
        head = node
        node = tmp
    return head
