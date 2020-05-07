class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])
        print(intervals)
        cur = 0
        while cur+1 < len(intervals):
            if intervals[cur][1] < intervals[cur+1][0]: 
                cur += 1
                continue
            temp = [intervals[cur][0],intervals[cur+1][1]]
            if intervals[cur][1] < intervals[cur+1][1]: intervals[cur] = temp
            del intervals[cur + 1]
            print(intervals,cur)
        return intervals

s = Solution()
print(s.merge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]))