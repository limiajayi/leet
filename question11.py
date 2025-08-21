import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxArea(height):
        if not height:
            return 0
        
        ptrLeft = 0
        ptrRight = len(height) - 1
        areas = []
        
        width = ptrRight - ptrLeft
        length = height[ptrLeft] if height[ptrLeft] <= height[ptrRight] else height[ptrRight]
        area = width * length
        
        areas.append(area)
        
        while ptrLeft < len(height) and ptrRight > 0:
            
            if ptrLeft == ptrRight:
                break
            
            if height[ptrLeft] < height[ptrLeft + 1]:
                ptrLeft += 1
                
            width = ptrRight - ptrLeft
            length = height[ptrLeft] if height[ptrLeft] <= height[ptrRight] else height[ptrRight]
            area = width * length
            areas.append(area)
            
            if height[ptrRight - 1] > height[ptrRight]:
                ptrRight -= 1
            
            width = ptrRight - ptrLeft
            length = height[ptrLeft] if height[ptrLeft] <= height[ptrRight] else height[ptrRight]
            area = width * length
            areas.append(area)
                
            if len(areas) > 5:
                if areas[len(areas) - 2] == areas[len(areas) - 1]:
                    break
            
        return areas
    
    def intToRoman(num):
        #Ctrl + [] to change indent
        
        dict = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90,  "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
        romans = ""
        
        
        for letter in dict:
            while num >= dict[letter]:
                
                romans += letter
                num -= dict[letter]
                
        return romans
    
    def longestCommonPrefix(strs):
        """Find the longest common prefix amongst an array of strings"""
        if not strs:
            #if the array is empty just return an empty string
            return ""
        
        #let the initial prefix be the first string
        prefix = strs[0]
        
        #from the second string till the last
        for i in range(1, len(strs)):
            
            current = strs[i] #current string being compared with the first
            equal = len(prefix) == len(current) #conditional that helps with the loop
            
            while equal == False or prefix != current: 
                #while the current string and prefix are not equal in length or prefix is not equal to the current string
                #reduce the longer string by 1 until they're equal in length and in value
                if len(prefix) > len(current):
                    prefix = prefix[:-1]
                else:
                    current = current[:-1]
                
                equal = len(prefix) == len(current)
        
        #return the longest common prefix
        return prefix
    
    def twoSum(nums, target):
        arrayOfArrays = []
    
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
        
                if (nums[i] + nums[j]) == target:
                    arrayOfArrays.append([nums[i], nums[j]])
                
        return arrayOfArrays
    
    def threeSum(nums):
        
        arrayOfArrays = []
        memory = []
        
        for i in range(len(nums)):
            
            if nums[i] not in memory:
                minus = nums[i] * -1
                new = nums[i+1:]
                targets = Solution.twoSum(new, minus)
                
                for j in range(len(targets)):
                    targets[j].append(nums[i])
                    arrayOfArrays.append(targets[j])
            
            memory.append(nums[i])
            
        
        return arrayOfArrays
    
    def letterCombinations(digits):
        
        if not digits:
            return []
    
        def helper(processed, up):
            if not up:
                return [processed]
        
            button = int(up[0])
            ans = []
            
            if 2 <= button <= 6:
                for i in range((button-2)*3, (button-1)*3):
                    ch = chr(ord('a') + i)
                    ans += helper(processed + ch, up[1:])
            elif button == 7:
                for i in range(15, 19):
                    ch = chr(ord('a') + i)
                    ans += helper(processed + ch, up[1:])
            elif button == 8:
                for i in range(19, 22):
                    ch = chr(ord('a') + i)
                    ans += helper(processed + ch, up[1:])
            elif button == 9:
                for i in range(22, 26):
                    ch = chr(ord('a') + i)
                    ans += helper(processed + ch, up[1:])
            return ans

        return helper("", digits)
    
    def removeNthFromEnd(head: ListNode, n: int):
        current = head
        target = head
        prev = head
        counter = 0
        
        if current.next == None and n == 1:
            head = ListNode()
        
        
        while current.next != None:
            current = current.next
            counter += 1
            
            if counter >= n:
                target = target.next
            
            if counter >= n + 1:
                prev = prev.next
                
        prev.next = target.next
        target = None
        
        new = head
        arr = []
        arr.append(new.val)
        
        while new.next != None:
            new = new.next
            arr.append(new.val)
            
        return arr
    
    def isValid(s):
        chars = '([{'
        others = ']})'
        track = []
        stack = []
        unmatches = 0
        otherStack = []
        arr = [var for var in s]
        value = False
        
        if arr[len(s) - 1] in chars:
            return False
        
        for i in range(len(s)):
            #initially check if the character is either ( or { or [
            if arr[i] in chars:
                stack.append(arr[i])
                track.append(arr[i])
            elif arr[i] in others:
                otherStack.append(arr[i])
                
                if len(track) > 0:
                    soth = arr[i]
                    match arr[i]:
                            case ')':
                                value = True if track[-1] == '(' else False
                            case '}':
                                value = True if track[-1] == '{' else False
                            case ']':
                                value = True if track[-1] == '[' else False
                    if value == False:
                        unmatches += 1
                    track.pop()
                            

        return (len(stack) == len(otherStack)) and value and unmatches == 0
    
    def mergeTwoLists(list1: ListNode, list2: ListNode):
        curr1 = list1
        curr2 = list2
        newList = ListNode()
        curr3 = newList
        
        #checking both lists
        
        #if list1 is empty and list2 is not empty
        if curr2 != None and curr1 == None:
            while curr2 != None:
                curr3.next = ListNode(curr2.val, None)
                curr3 = curr3.next
                curr2 = curr2.next
            newList = newList.next
            return newList
                
        #if list1 is not empty and list2 is empty
        if curr1 != None and curr2 == None:
            while curr1 != None:
                curr3.next = ListNode(curr1.val, None)
                curr3 = curr3.next
                curr1 = curr1.next
            newList = newList.next
            return newList
        
        #if they're both empty
        if curr1 == None and curr2 == None:
            newList = newList.next
            return newList
        
        #if they're both non-empty
        while curr1 != None and curr2 != None:
            if curr1.val < curr2.val:
                curr3.next = ListNode(curr1.val, None)
                curr3 = curr3.next
                curr1 = curr1.next
            elif curr1.val > curr2.val:
                curr3.next = ListNode(curr2.val, None)
                curr3 = curr3.next
                curr2 = curr2.next
            else:
                curr3.next = ListNode(curr1.val, ListNode(curr2.val, None))
                curr3 = curr3.next.next
                
                curr1 = curr1.next
                curr2 = curr2.next
                
        #if list2 is longer than list1
        if curr1 == None and curr2 != None:
            while curr2 != None:
                curr3.next = ListNode(curr2.val, None)
                curr3 = curr3.next
                curr2 = curr2.next
                
        #if list1 is longer than list2
        if curr2 == None and curr1 != None:
            while curr1 != None:
                curr3.next = ListNode(curr1.val, None)
                curr3 = curr3.next
                curr1 = curr1.next
        
        
        newList = newList.next
        return newList
    
    #we have an array that keeps up with nodes
    def hasCycle(head):
        #linked list question
        arr = []
        pos = -1
        
        curr = head
        #this is to break normal lists
        while curr != None:
            #if current is in the array, 
            # loop through the array to find the exact index
            #where the loop starts
            if curr in arr:
                for i in range(len(arr)):
                    if arr[i] == curr:
                        pos = i
                #break to prevent an infinite loop
                break
            
            arr.append(curr)
            
            curr = curr.next 
            
        if pos == -1:
            return False
        return True
    
    def isAnagram(self, s: str, t: str) -> bool:
        #check if two strings s and t are anagrams
        checkLength = len(s) == len(t)
        if checkLength == False:
            return checkLength

        arr1 = [ind for ind in s]
        arr2 = [ind for ind in t]
        value = False

        for i in range(len(arr1)):

            if arr1[i] in arr2:
                arr2.remove(arr1[i])
                value = True

        if len(arr2) == 0:
            return True
        return False
    
    
    # im thinking add the root initially
    # remove the remove
    # swap the left and right
    # add left and right back in queue
    # repeat
    def invertTree(root: TreeNode):
        empty = []
        empty.append(root)
        
        while len(empty) > 0:
            initial: TreeNode = empty.pop(0)
            print(initial.val)
            
            if initial == None:
                break
            
            if not initial.left and not initial.right:
                break
            
            #if there is only a left node
            if initial.right == None:
                temp = initial.left
                initial.right = temp
                initial.left = None
                
                empty.append(initial.right)
                
                #if there is only a right node
            elif initial.left == None:
                temp = initial.right
                initial.left = temp
                initial.right = None
                empty.append(initial.left)
            
            #if there are left and right nodes
            if initial.left != None and initial.right != None:
                temp = initial.left
                initial.left = initial.right
                initial.right = temp
                empty.append(initial.left)
                empty.append(initial.right)
                
        return root
        

treeRoot: TreeNode = TreeNode(2, TreeNode(3, TreeNode(1, None, None), None), None)

print(Solution.invertTree(treeRoot).right.right.val)




# arr1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
# arr2 = ListNode(1, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None)))))

# value2 = ListNode(2, None)
# value1 = ListNode(1, value2)
# value2.next = value1

# print(Solution.hasCycle(value1))

# curr3 = Solution.mergeTwoLists(arr2, arr1)

# while curr3 != None:
#     print(curr3.val)
#     curr3 = curr3.next
