You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.
You start on square 1 of the board. In each move, starting from square curr, do the following:
Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of dice rolls required to reach the square n2. If it is not possible to reach the square, return -1.
#code here
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def get_1D_position(r, c):
            row = n - 1 - r
            if row % 2 == 0:
                return row * n + c
            else:
                return row * n + (n - 1 - c)
        flattened_board = [-1] * (n * n)
        for r in range(n):
            for c in range(n):
                pos = get_1D_position(r, c)
                if board[r][c] != -1:
                    flattened_board[pos] = board[r][c] - 1
        queue = deque([(0, 0)])  # (position, moves)
        visited = set()
        while queue:
            pos, moves = queue.popleft()
            if pos == n * n - 1:
                return moves
            for dice in range(1, 7):
                next_pos = pos + dice
                if next_pos < n * n and next_pos not in visited:
                    visited.add(next_pos)
                    if flattened_board[next_pos] != -1:
                        next_pos = flattened_board[next_pos]
                    queue.append((next_pos, moves + 1))
        return -1  
