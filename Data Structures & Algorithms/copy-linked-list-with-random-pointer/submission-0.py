"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        nodeMap = {}

        current = head

        while current:
            nodeMap[current] = Node(current.val)
            current = current.next
        
        current = head
        while current:
            nodeMap[current].next = nodeMap.get(current.next)
            nodeMap[current].random = nodeMap.get(current.random)
            current = current.next

        return nodeMap[head]







