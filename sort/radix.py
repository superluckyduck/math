class Radix:
    def radixSort(self,arr, exp):
        n = len(arr)
        output = [0] * n  # 输出数组
        count = [0] * 10  # 计数数组，大小为10（0-9）
        # 计算每个数字的出现次数
        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1
        # 按位累加（变为位置索引）
        for i in range(1, 10):
            count[i] += count[i - 1]
        # 构建输出数组
        i = n - 1
        while i >= 0:
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            i -= 1
        # 将输出数组复制到原数组
        for i in range(n):
            arr[i] = output[i]

    def radix_sort(self,arr):
        # 找到最大值，以确定最大位数
        max_value = max(arr)
        s = Radix()
        # 对每一位进行排序
        exp = 1
        while max_value // exp > 0:
            s.radixSort(arr, exp)
            exp *= 10
        return arr

# 测试计数排序
if __name__ == "__main__":
    s = Radix()
    arr = [2, 3, 5, 4, 1]
    print(arr)
    arr2 = s.radix_sort(arr.copy())
    print("arr2", arr2)