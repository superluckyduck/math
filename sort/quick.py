class Quick:
    def quickSort(self,arr, left=None, right=None):
        #定义快速排序要操作的子数组的范围
        left = 0 if not isinstance(left,(int, float)) else left
        right = len(arr)-1 if not isinstance(right,(int, float)) else right
        if left < right:
            #调用 partition以获得分区索引，该索引将数组分成两部分：在它左侧的元素小于等于索引，在它右侧的元素大于索引
            #递归地对两部分进行快速排序。
            partitionIndex = self.partition(arr, left, right)
            self.quickSort(arr, left, partitionIndex-1)
            self.quickSort(arr, partitionIndex+1, right)
        return arr

    def partition(self,arr, left, right):
        #将left作为基准
        pivot = left
        index = pivot+1
        i = index
        while  i <= right:
            #如果小于基准，将与arr[index]交换，并将index 向前推进
            if arr[i] < arr[pivot]:
                arr[i], arr[index] = arr[index], arr[i]
                index+=1
            i+=1
        #循环结束后，将基准的元素与最后一个小于 pivot 的元素交换，从而将基准放在排序好的位置
        arr[pivot], arr[index-1] = arr[index-1], arr[pivot]
        return index-1

class QuickStatic:
    @staticmethod
    def quickSort(arr, left=None, right=None):
        left = 0 if not isinstance(left,(int, float)) else left
        right = len(arr)-1 if not isinstance(right,(int, float)) else right
        if left < right:
            partitionIndex = QuickStatic.partition(arr, left, right)
            QuickStatic.quickSort(arr, left, partitionIndex-1)
            QuickStatic.quickSort(arr, partitionIndex+1, right)
        return arr

    @staticmethod
    def partition(arr, left, right):
        pivot = left
        index = pivot+1
        i = index
        while  i <= right:
            if arr[i] < arr[pivot]:
                arr[i], arr[index] = arr[index], arr[i]
                index+=1
            i+=1
        arr[pivot], arr[index-1] = arr[index-1], arr[pivot]
        return index-1


if __name__ == "__main__":
    #创建实例对象
    s = Quick()
    arr = [2,3,5,4,1]
    arr2 = s.quickSort(arr.copy())
    print("arr2",arr2)
    print(arr)
    arr3 = QuickStatic.quickSort(arr.copy())
    print("arr3",arr3)