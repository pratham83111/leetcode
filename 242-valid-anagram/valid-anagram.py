class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        count = {}
        for i in s:
            count[i]= count.get(i,0)+1
        for i in t:
            count[i] = count.get(i,0)-1
        for i in count.values():
            if i != 0:
                return False 
        return True