You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

Each meeting will take place in the unused room with the lowest number.
If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
When a room becomes unused, meetings that have an earlier original start time should be given the room.
Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and not including b.

import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        count = [0] * n 
        meetings.sort()
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)
        busy_rooms = []

        for start, end in meetings:
            duration = end - start
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(available_rooms, room)

            if available_rooms:
                room = heapq.heappop(available_rooms)
                heapq.heappush(busy_rooms, (end, room))
                count[room] += 1
            else:
                earliest_end, room = heapq.heappop(busy_rooms)
                new_end = earliest_end + duration
                heapq.heappush(busy_rooms, (new_end, room))
                count[room] += 1
        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i
