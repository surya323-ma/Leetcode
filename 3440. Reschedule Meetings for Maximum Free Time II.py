You are given an integer eventTime denoting the duration of an event. You are also given two integer arrays startTime and endTime, each of length n.

These represent the start and end times of n non-overlapping meetings that occur during the event between time t = 0 and time t = eventTime, where the ith meeting occurs during the time [startTime[i], endTime[i]].

You can reschedule at most one meeting by moving its start time while maintaining the same duration, such that the meetings remain non-overlapping, to maximize the longest continuous period of free time during the event.

Return the maximum amount of free time possible after rearranging the meetings.

Note that the meetings can not be rescheduled to a time outside the event and they should remain non-overlapping.

Note: In this version, it is valid for the relative ordering of the meetings to change after rescheduling one meeting.

  class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:  
        n = len(startTime)        
        def get_maximum_free_time(time):
            n = len(time)
            ans, cur_max_free_time = 0, 0
            for i in range(n-2):  
                ans = max(ans, abs(time[i+2][0] - time[i][1]) - abs((time[i+1][1]-time[i+1][0])))
                if cur_max_free_time >= abs(time[i+1][1]-time[i+1][0]):
                    ans = max(ans, abs(time[i+2][0] - time[i][1]))
                cur_max_free_time = max(cur_max_free_time, abs(time[i+1][0]-time[i][1]))
            
            ans = max(ans, abs(time[-1][0] - time[-2][1]))
            return ans 
        time = [[0, 0]]
        for i in range(n):
            time.append([startTime[i], endTime[i]])        
        time.append([eventTime, eventTime])
        cur_max = get_maximum_free_time(time)
        time = [x[::-1] for x in time]
        time = time[::-1]
        return max(cur_max, get_maximum_free_time(time))






                
                
