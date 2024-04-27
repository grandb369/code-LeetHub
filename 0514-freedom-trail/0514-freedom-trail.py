class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_len = len(ring)
        key_len = len(key)
        curr = [inf for _ in range(ring_len)]
        prev = [0 for _ in range(ring_len)]

        # Find the minimum steps between two indexes of ring
        def count_steps(curr, next):
            steps_between = abs(curr - next)
            steps_around = ring_len - steps_between
            return min(steps_between, steps_around)

        # For each occurrence of the character at keyIndex of key in ring
        # Stores minimum steps to the character from ring_index of ring
        for key_index in range(key_len - 1, -1, -1):
            curr = [inf for _ in range(ring_len)]
            for ring_index in range(ring_len):
                for character in range(ring_len):
                    if ring[character] == key[key_index]:
                        curr[ring_index] = min(curr[ring_index],
                                1 + count_steps(ring_index, character)
                                + prev[character])
            prev = curr.copy()

        return prev[0]