class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        n=len(heights)
        r=n-1
        result = 0
        while l<r:
            width= r-l
            height = min(heights[l], heights[r])
            result = max(result, height*width)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return result