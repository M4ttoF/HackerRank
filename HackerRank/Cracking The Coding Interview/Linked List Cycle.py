"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    pass
    if head==None:
        return False
    nodes={}
    tmp=head
    while not tmp==None:
        if not tmp in nodes:
            nodes[tmp]=True
        else:
            return True
        tmp=tmp.next
    return False
    
