class Solution(object):
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        start_r = start_c = 0
        litter = {}
        idx = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = idx
                    idx += 1

        if idx == 0:
            return 0

        full = (1 << idx) - 1

        q = deque([(start_r, start_c, energy, 0, 0)])
        best = {}

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c, e, mask, moves = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                ne = e - 1

                if ne < 0:
                    continue

                if classroom[nr][nc] == 'R':
                    ne = energy

                nmask = mask

                if (nr, nc) in litter:
                    nmask |= 1 << litter[(nr, nc)]

                if nmask == full:
                    return moves + 1

                state = (nr, nc, nmask)

                if ne > best.get(state, -1):
                    best[state] = ne
                    q.append((nr, nc, ne, nmask, moves + 1))

        return -1
        