class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Step 1: binary search rows
        low, high = 0, len(matrix) - 1

        while low <= high:
            mid = (low + high) // 2

            if target < matrix[mid][0]:
                high = mid - 1
            elif target > matrix[mid][-1]:
                low = mid + 1
            else:
                # Step 2: binary search inside row
                row = mid
                left, right = 0, len(matrix[0]) - 1

                while left <= right:
                    m = (left + right) // 2

                    if matrix[row][m] == target:
                        return True
                    elif matrix[row][m] < target:
                        left = m + 1
                    else:
                        right = m - 1

                return False

        return False