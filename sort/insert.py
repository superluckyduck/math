#插入排序
class Insert:
    def insertSort(self, arr):
        n = len(arr)
        for i in range(n):
            preIndex = i-1
            current = arr[i]
            while preIndex >= 0 and arr[preIndex] > current:
                arr[preIndex+1] = arr[preIndex]
                preIndex-=1
            arr[preIndex+1] = current
        return arr

class InsertStatic:
    @staticmethod
    def insertSort(arr):
        n = len(arr)
        for i in range(n):
            preIndex = i - 1
            current = arr[i]
            while preIndex >= 0 and arr[preIndex] > current:
                arr[preIndex + 1] = arr[preIndex]
                preIndex -= 1
            arr[preIndex + 1] = current
        return arr


if __name__ == "__main__":
    #创建实例对象
    s = Insert()
    arr = [2,3,5,4,1]
    arr2 = s.insertSort(arr.copy())
    print("arr2",arr2)
    print(arr)
    arr3 = InsertStatic.insertSort(arr.copy())
    print("arr3",arr3)