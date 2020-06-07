class Solution:
    def mySqrt(self, x: int) -> int:
        # if x < 2: return x
        # l,r = 1,x
        # while l <= r:
        #     mid = l+(r-l)//2
        #     if mid*mid > x:
        #         r = mid-1
        #     elif mid*mid < x:
        #         l = mid+1
        #     else: return mid
        # return r

        #y = 2*x0(x-x0) + x0^2 - c
        #y == 0 -> x = 0.5*(c-x0^2)/x0 + x0
        x0 = x
        while x0**2 > x:
            temp = int(0.5 * (x - x0 ** 2) / x0 + x0)
            x0 = temp
            print(x0)
        return x0

s = Solution()
print(s.mySqrt(8))