class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Return early if the string is null or empty
        if not s:
            return s

        # Preprocess the string to handle palindromes uniformly
        modified_string = self._preprocess_string(s)
        n = len(modified_string)
        palindrome_radius_array = [0] * n
        center = 0
        right_boundary = 0
        max_palindrome_length = 0

        # Iterate through each character in the modified string
        for i in range(1, n - 1):
            mirror_index = 2 * center - i

            # Use previously computed values to avoid redundant calculations
            if right_boundary > i:
                palindrome_radius_array[i] = min(
                    right_boundary - i, palindrome_radius_array[mirror_index]
                )

            # Expand around the current center while characters match
            while (
                modified_string[i + 1 + palindrome_radius_array[i]]
                == modified_string[i - 1 - palindrome_radius_array[i]]
            ):
                palindrome_radius_array[i] += 1

            # Update the center and right boundary if the palindrome extends beyond the current boundary
            if i + palindrome_radius_array[i] > right_boundary:
                center = i
                right_boundary = i + palindrome_radius_array[i]

            # Update the maximum length of palindrome starting at the beginning
            if i - palindrome_radius_array[i] == 1:
                max_palindrome_length = max(
                    max_palindrome_length, palindrome_radius_array[i]
                )

        # Construct the shortest palindrome by reversing the suffix and prepending it to the original string
        suffix = s[max_palindrome_length:][::-1]
        return suffix + s

    def _preprocess_string(self, s: str) -> str:
        # Add boundaries and separators to handle palindromes uniformly
        return "^" + "#" + "#".join(s) + "#$"