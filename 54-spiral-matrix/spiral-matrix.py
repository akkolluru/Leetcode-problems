from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        if not matrix or not matrix[0]:
            return []

        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1

        while top <= bottom and left <= right:
            # Go right
            for j in range(left, right + 1):
                answer.append(matrix[top][j])
            top += 1

            # Go down
            for i in range(top, bottom + 1):
                answer.append(matrix[i][right])
            right -= 1

            # Check if there's a row left to traverse
            if top <= bottom:
                # Go left
                for j in range(right, left - 1, -1):
                    answer.append(matrix[bottom][j])
                bottom -= 1

            # Check if there's a column left to traverse
            if left <= right:
                # Go up
                for i in range(bottom, top - 1, -1):
                    answer.append(matrix[i][left])
                left += 1

        return answer