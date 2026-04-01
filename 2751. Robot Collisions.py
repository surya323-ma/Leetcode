There are n 1-indexed robots, each having a position on a line, health, and movement direction.

You are given 0-indexed integer arrays positions, healths, and a string directions (directions[i] is either 'L' for left or 'R' for right). All integers in positions are unique.

All robots start moving on the line simultaneously at the same speed in their given directions. If two robots ever share the same position while moving, they will collide.

If two robots collide, the robot with lower health is removed from the line, and the health of the other robot decreases by one. The surviving robot continues in the same direction it was going. If both robots have the same health, they are both removed from the line.

Your task is to determine the health of the robots that survive the collisions, in the same order that the robots were given, i.e. final health of robot 1 (if survived), final health of robot 2 (if survived), and so on. If there are no survivors, return an empty array.

Return an array containing the health of the remaining robots (in the order they were given in the input), after no further collisions can occur.

Note: The positions may be unsorted.

 class Solution:
    def survivedRobotsHealths(self, pos, hp, dir):
        order = sorted(range(len(pos)), key=lambda i: pos[i])
        st, res = [], []
        for i in order:
            if dir[i] == 'R':
                st.append((i, hp[i]))   # use tuple
            else:
                h = hp[i]
                while st and h > 0:
                    if st[-1][1] > h:
                        st[-1] = (st[-1][0], st[-1][1]-1); h = 0
                    elif st[-1][1] < h:
                        h -= 1; st.pop()
                    else:
                        st.pop(); h = 0
                if h: res.append((i, h))
        res += st
        return [h for _, h in sorted(res)]
