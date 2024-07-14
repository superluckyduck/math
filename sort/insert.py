#插入排序
class Insert:
    def insert(self, arr):
        n = len(arr)
        for i in range(n):
            mid = i
            for j in range(i + 1, n):
                if arr[j] < arr[mid]:
                    mid = j
            arr[mid], arr[i] = arr[i], arr[mid]
        return arr