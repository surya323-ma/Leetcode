Design a data structure that can efficiently manage data packets in a network router. Each data packet consists of the following attributes:

source: A unique identifier for the machine that generated the packet.
destination: A unique identifier for the target machine.
timestamp: The time at which the packet arrived at the router.
Implement the Router class:

Router(int memoryLimit): Initializes the Router object with a fixed memory limit.

memoryLimit is the maximum number of packets the router can store at any given time.
If adding a new packet would exceed this limit, the oldest packet must be removed to free up space.
bool addPacket(int source, int destination, int timestamp): Adds a packet with the given attributes to the router.

A packet is considered a duplicate if another packet with the same source, destination, and timestamp already exists in the router.
Return true if the packet is successfully added (i.e., it is not a duplicate); otherwise return false.
int[] forwardPacket(): Forwards the next packet in FIFO (First In First Out) order.

Remove the packet from storage.
Return the packet as an array [source, destination, timestamp].
If there are no packets to forward, return an empty array.
int getCount(int destination, int startTime, int endTime):

Returns the number of packets currently stored in the router (i.e., not yet forwarded) that have the specified destination and have timestamps in the inclusive range [startTime, endTime].
Note that queries for addPacket will be made in increasing order of timestamp.

from collections import deque, defaultdict
import bisect

class Router:
    def __init__(self, memoryLimit):
        self.memoryLimit = memoryLimit
        self.queue = deque()  
        self.packetSet = set()  
        self.destTimeMap = defaultdict(list)  
    def addPacket(self, source, destination, timestamp):
        key = (source, destination, timestamp)
        if key in self.packetSet:
            return False  
        if len(self.queue) >= self.memoryLimit:
            old_packet = self.queue.popleft()
            old_key = tuple(old_packet)
            self.packetSet.remove(old_key)
            ts_list = self.destTimeMap[old_packet[1]]
            idx = bisect.bisect_left(ts_list, old_packet[2])
            if idx < len(ts_list) and ts_list[idx] == old_packet[2]:
                ts_list.pop(idx)
        self.queue.append([source, destination, timestamp])
        self.packetSet.add(key)
        self.destTimeMap[destination].append(timestamp)
        return True

    def forwardPacket(self):
        if not self.queue:
            return []
        packet = self.queue.popleft()
        key = tuple(packet)
        self.packetSet.remove(key)
        ts_list = self.destTimeMap[packet[1]]
        idx = bisect.bisect_left(ts_list, packet[2])
        if idx < len(ts_list) and ts_list[idx] == packet[2]:
            ts_list.pop(idx)
        return packet
    def getCount(self, destination, startTime, endTime):
        ts_list = self.destTimeMap[destination]
        left = bisect.bisect_left(ts_list, startTime)
        right = bisect.bisect_right(ts_list, endTime)
        return right - left

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)

























  
