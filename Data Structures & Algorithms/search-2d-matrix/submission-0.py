class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        n = len(matrix)
        high = n-1
        row = -1

        while high >= low:
            mid = (low + high) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif matrix[mid][0] > target:
                high = mid - 1
            elif matrix[mid][0] < target:
                low = mid + 1
        
        if row == -1:
            return False
        
        n = len(matrix[0])
        low = 0
        high = n-1
        while low <= high:
            mid = (low + high)// 2
            if matrix[row][mid]  == target:
                return True
            elif matrix[row][mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False









