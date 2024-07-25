class Counting:
    def countingSort(self,arr):
        maxValue = max(arr)
        # 创建计数桶
        bucketLen = maxValue + 1
        bucket = [0] * bucketLen
        #统计元素出现次数
        sortedIndex = 0
        arrLen = len(arr)
        for i in range(arrLen):
            if not bucket[arr[i]]:
                bucket[arr[i]] = 0
            bucket[arr[i]] += 1
        #填充排序后的数组
        for j in range(bucketLen):
            while bucket[j] > 0:
                arr[sortedIndex] = j
                sortedIndex += 1
                bucket[j] -= 1
        return arr

# 测试计数排序
if __name__ == "__main__":
    s = Counting()
    arr = [2, 3, 5, 4, 1]
    print(arr)
    arr2 = s.countingSort(arr.copy())
    print("arr2", arr2)