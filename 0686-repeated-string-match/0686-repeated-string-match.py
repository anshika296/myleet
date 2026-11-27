class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        new=a
        count=1
        while len(new)<len(b):
            new+=a
            count+=1
        if b in new:
            return count
        new+=a#we do one extra repetition because b myt be crossing boundary between two copies 
        count+=1
        if b in new:
            return count
        return -1
        
