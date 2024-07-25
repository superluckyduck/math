class Select:
    def selectSort(self, arr):
        n = len(arr)
        for i in range(n):
            mid = i
            for j in range(i + 1, n):
                if arr[j] < arr[mid]:
                    mid = j
            arr[mid], arr[i] = arr[i], arr[mid]
        return arr

class SelectStatic:
    @staticmethod
    def selectSort(arr):
        n = len(arr)
        for i in range(n):
            mid = i
            for j in range(i + 1, n):
                if arr[j] < arr[mid]:
                    mid = j
            arr[mid], arr[i] = arr[i], arr[mid]
        return arr


if __name__ == "__main__":
    #创建实例对象
    s = Select()
    arr = [2,3,5,4,1]
    arr2 = s.selectSort(arr.copy())
    print("arr2",arr2)
    print(arr)
    arr3 = SelectStatic.selectSort(arr.copy())
    print("arr3",arr3)