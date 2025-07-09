You are given an integer eventTime denoting the duration of an event, where the event occurs from time t = 0 to time t = eventTime.
You are also given two integer arrays startTime and endTime, each of length n. These represent the start and end time of n non-overlapping meetings, where the ith meeting occurs during the time [startTime[i], endTime[i]].
You can reschedule at most k meetings by moving their start time while maintaining the same duration, to maximize the longest continuous period of free time during the event.
The relative order of all the meetings should stay the same and they should remain non-overlapping.Return the maximum amount of free time possible after rearranging the meetings.
Note that the meetings can not be rescheduled to a time outside the event #code here
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        diff=[i-j for i,j in zip(startTime[1:],endTime)]
        if startTime[0]!=0: diff=[startTime[0]]+diff
        if endTime[-1]<eventTime: diff=diff+[eventTime-endTime[-1]]
        
        k+=1
        
        if len(diff)<=k: return sum(diff)
        else:
            s=sum(diff[:k])
            ans=s
            for i in range(k,len(diff)):
                s+=diff[i]-diff[i-k]
                ans=max(ans,s)
                
        return ans
