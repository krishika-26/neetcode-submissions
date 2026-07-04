class Solution:
    def largestRectangleArea(self, h):
        s=[];a=0;h+=[0]
        for i,x in enumerate(h):
            while s and h[s[-1]]>x:
                H=h[s.pop()]
                a=max(a,H*(i-(s[-1]+1 if s else 0)))
            s.append(i)
        return a