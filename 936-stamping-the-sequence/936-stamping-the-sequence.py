class Solution:
        def movesToStamp(self, s, t):
            if s[0] != t[0] or s[-1] != t[-1]: return []
            n, m = len(s), len(t)
            path = [0] * m
            pos = collections.defaultdict(set)
            for i, c in enumerate(s): pos[c].add(i)

            def dfs(i, index):
                path[i] = index
                if i == m - 1: return index == n - 1
                nxt_index = set()
                if index == n - 1:  # rule 2
                    nxt_index |= pos[t[i + 1]]
                elif s[index + 1] == t[i + 1]:  # rule 0
                    nxt_index.add(index + 1)
                if s[0] == t[i + 1]:  # rule 1
                    nxt_index.add(0)
                return any(dfs(i + 1, j) for j in nxt_index)

            def path2res(path):
                down, up = [], []
                for i in range(len(path)):
                    if path[i] == 0:
                        up.append(i)
                    elif i and path[i] - 1 != path[i - 1]:
                        down.append(i - path[i])
                return down[::-1] + up

            if not dfs(0, 0): return []
            return path2res(path)