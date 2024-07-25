class Heap:
    def heapSort(self,arr):
        s = Heap()
        arrLen = len(arr)
        # 建立最大堆
        import math
        for i in range(math.floor(arrLen / 2), -1, -1):
            s.heapify(arr, arrLen, i)
        # 一个个提取元素，从堆中取出最大的元素
        for i in range(arrLen - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]# 交换当前根节点和最后一个节点
            arrLen -= 1
            s.heapify(arr, arrLen, 0) # 对根节点进行 heapify
        return arr

    def heapify(self,arr,arrlen, i):
        left = 2 * i + 1# 左子节点
        right = 2 * i + 2# 右子节点
        largest = i # 初始化最大的元素为根
        s = Heap()
        if left < arrlen and arr[left] > arr[largest]:
            largest = left
        if right < arrlen and arr[right] > arr[largest]:
            largest = right
        # 如果最大的元素不是根节点
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            s.heapify(arr, arrlen, largest)



# 测试堆排序
if __name__ == "__main__":
    s = Heap()
    arr = [2, 3, 5, 4, 1,6,8,7]
    print(arr)
    arr2 = s.heapSort(arr.copy())
    print("arr2", arr2)