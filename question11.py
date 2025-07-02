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
        
        