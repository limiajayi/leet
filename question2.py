# Definition for singly-linked list.
import math
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
    
    def lengthOfLongestSubstring(s: str) -> int:
        #it works in my heart and thats enough <3
        if not s:
            return 0
        h = {}
        counterCounter = []
        counter = 0

        for i in range(0, len(s)):
    
            if h.get(s[i]) == None:
                h[s[i]] = 1
                counter += 1
            else:
                counterCounter.append(counter)
                counter = 0
                counter += 1
                h.update({s[i]: h[s[i]] + 1})
                
        return max(counterCounter)
    
    def findMedianSortedArrays(nums1, nums2) -> float:
        if not nums1 and not nums2:
            return 0
        numsArray = []
        i = j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                numsArray.append(nums1[i])
                i += 1
            else:
                numsArray.append(nums2[j])
                j+= 1
        
        numsArray.extend(nums1[i:])
        numsArray.extend(nums2[j:])
        
        parity = len(numsArray) % 2
        
        if parity == 1:
            median = numsArray[math.ceil(len(numsArray) / 2) - 1]
        else:
            median = (numsArray[(len(numsArray) // 2) - 1] + numsArray[(len(numsArray) // 2)]) / 2
        
        return median
    
    def is_palindrome(my_string):
        if not my_string:
            return True
        if my_string[0] != my_string[-1]:
            return False
        else:
            return Solution.is_palindrome(my_string[1:-1])
    
    def longestPalindrome(s):
        n = len(s)
        
        check = Solution.is_palindrome(s)
        j = 0
        
        while check == False and j < n:
            if s.count(s[j]) > 1 or n == 2:
                s = s[j:-1]
                n = len(s)
                check = Solution.is_palindrome(s)
            else:
                j += 1
                
        return s
    

