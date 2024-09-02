class find:
    def binarySearch(self,arr,target)->int:
        i,j = 0,len(arr)-1
        while i<=j:
            m = i + (j - i) // 2
            if arr[m]>target:
                j = m-1
            elif arr[m]<target:
                i = m+1
            else:
                return m
        return -1
    def binarySearchInsert(self,arr,target)->int:
        i, j = 0, len(arr) - 1
        while i <= j:
            m = i + (j - i) // 2
            if arr[m] > target:
                j = m - 1
            elif arr[m] < target:
                i = m + 1
            else:
                j = m-1
        return i

if __name__ == "__main__":
    f = find()
    arr = [1,2,3,4,5]
    target = 3
    index = f.binarySearch(arr,target)
    print(index)
    target = 4
    index = f.binarySearchInsert(arr, target)
    print(index)