class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:
        if target >= letters[-1] or target < letters[0]: return letters[0]
        l,r = 0,len(letters)
        while l <= r:
            mid = l + (r-l)//2
            if target < letters[mid]:
                r = mid-1
            elif target > letters[mid]:
                l = mid+1
            else:
                while letters[mid] == target: mid += 1
                return letters[mid]
        print(l,r)
        return letters[l]

s = Solution()
print(s.nextGreatestLetter(["e","e","e","k","q","q","q","v","v","y"],"q"))