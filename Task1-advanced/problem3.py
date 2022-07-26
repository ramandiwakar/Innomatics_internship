class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxx= max(candies)
        res = [False]*len(candies)
        counter=0
        for i in candies:
            if i+extraCandies>=maxx:
                res[counter]=True
            counter+=1
            
        return res
        