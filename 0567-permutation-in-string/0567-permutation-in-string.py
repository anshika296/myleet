from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        count1=Counter(s1)# here we are making a freq hmap for substring that needs to b checked
        count2=Counter(s2[:len(s1)])#here w are checking first 2 or respective length of characters from str2
        if count1==count2:
            return True
        left=0
        for right in range(len(s1),len(s2)):
            count2[s2[right]]+=1 #here we add a new character
            count2[s2[left]]-=1 #here we reduce first alphabet freq
            if count2[s2[left]]==0:
                del count2[s2[left]] #then remove
            left+=1
            if count1==count2:
                return True
        return False

        
        