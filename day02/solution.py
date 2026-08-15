from typing import List

class ListNode:
    def __init__(self, val: int, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr is not None:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next

        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
            return

        curr = self.head
        while curr.next is not None:
            curr = curr.next
            
        curr.next = new_node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        curr = self.head
        i = 0
        while curr.next is not None and i < index - 1:
            curr = curr.next
            i += 1

        if curr.next is not None:
            curr.next = curr.next.next
            return True

        return False

    def getValues(self) -> List[int]:
        valores = []
        curr = self.head

        while curr is not None:
            valores.append(curr.val)
            curr = curr.next
            
        return valores