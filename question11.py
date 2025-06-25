class Solution:
    def maxArea(height):
        if not height:
            return 0
        
        ptrLeft = 0
        ptrRight = len(height) - 1
        areas = []
        
        maxLeft = 0
        maxRight = 0
        length = 0
        breadth = 0
        
        while ptrLeft < len(height) and ptrRight >= 0:
            if ptrLeft == ptrRight:
                break
            
            length = maxLeft if maxRight > maxLeft else maxRight
            breadth = ptrRight - ptrLeft
            areas.append(length * breadth)
            
            if height[ptrLeft] <= height[ptrRight]:
                ptrLeft += 1
                
            if height[ptrLeft] > height[ptrRight]:
                ptrRight -= 1
            
            maxLeft = height[ptrLeft]
            maxRight = height[ptrRight]
            
            
        return areas




print(Solution.maxArea([1,2,1]))