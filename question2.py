# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        
        stringOne = ''
        stringTwo = ''
        
        curr = l1
        while curr != None:
            stringOne += str(curr.val)
            curr = curr.next
        
        curr = l2
        while curr != None:
            stringTwo += str(curr.val)
            curr = curr.next
            
        num = int(stringOne[::-1]) + int(stringTwo[::-1])
            
        stringThree = str(num)[::-1]
        array = [int(ch) for ch in stringThree]
        
        list = ListNode(array[0])
        
        curr = list
        for i in range(1, len(array)):
            curr.next = ListNode(array[i])
            curr = curr.next
        
        return list



listOne = ListNode(2, ListNode(4, ListNode(3)))
listTwo= ListNode(5, ListNode(6, ListNode(4)))


print(Solution.addTwoNumbers(listOne, listTwo))
            