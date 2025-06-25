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
    
    def convert(s, numRows):
        
        twoDArray = [[''] * (1000) for _ in range(numRows)]
        result = ""
        
        c = 0
        r = 0
        if numRows == 1:
            return s
        
        while r < numRows and c < len(twoDArray[0]) and len(s) > 0:
            
            twoDArray[r][c] = s[0]
            s = s[1:]
            
            if r + 1 == numRows and len(s) > 0:
                r = numRows - 2
                c += 1
                
                while r > 0 and len(s) > 0:
                    twoDArray[r][c] = s[0]
                    s = s[1:]
                    
                    c += 1
                    r -= 1
                
                if len(s) > 0:
                    twoDArray[r][c] = s[0]
                    s = s[1:]
                    
            r += 1
        
        
        for i in range(len(twoDArray)):
            for j in range(len(twoDArray[0])):
                result += twoDArray[i][j]
        
        return result
    
    def reverse(x):
        #reverse a string such that it is always within the range of [-2^31, 2^31 - 1]
        new = x #save the old number
        
        #if it is 0 then return 0
        if x == 0:
            return 0
        
        #if less than 0, make it positive by adding it twice to itself
        if x < 0:
            x -= 2 * x
            
        #convert to string and reverse it
        represent = str(x)[::-1]
        
        #remove starting zeroes
        while represent[0] == '0':
            represent = represent[1:]
        
        #if new was negative then add the negative to the front
        if  new < 0:
            represent = int('-' + represent)
        represent = int(represent)
        
        #return if not in the range
        if represent < -2**31 or represent > 2**31 - 1:
            return 0
        
        return represent

    
    def myAtoi(s):
        negative = False #assume always positive 
        s = s.strip() #remove white space
        
        #if 0 immediately return 0
        if s == "0" or s == "":
            return 0
        
        #if negative let negative = True
        if s[0] == "-":
            negative = True
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
            
        indicator = s[0].isdigit()
        new = ""
        
        while indicator == True and s != "":
            new += s[0]
            s = s[1:]
            if s != "":
                indicator = s[0].isdigit()
                
        if len(new) > 1:
            while new[0] == "0" and len(new) > 1:
                new = new[1:]
                
        if negative == True:
            new = "-" + new
            
        if new == "" or new == "-":
            return 0
        elif int(new) < -2**31:
            return -2**31
        elif int(new) > 2**31 - 1:
            return 2**31 - 1
            
        return int(new)
    
    def is_palindrome_int(x):
        my_string = str(x)
        opp = "".join(reversed(my_string))
        
        return opp == my_string
    
    
    

arr = Solution.is_palindrome_int(121)

print(arr)
