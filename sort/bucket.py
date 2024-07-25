class Bucket:
    def bucket_sort(self,arr, bucket_size=10):
        if len(arr) == 0:
            return arr
        # 1. 找到数组的最大值和最小值
        min_value = min(arr)
        max_value = max(arr)
        # 2. 创建桶
        bucket_count = (max_value - min_value) // bucket_size + 1
        buckets = [[] for _ in range(bucket_count)]
        # 3. 将元素放入相应的桶中
        for num in arr:
            index = (num - min_value) // bucket_size
            buckets[index].append(num)
        # 4. 对每个桶进行排序，并将结果合并
        sorted_array = []
        for bucket in buckets:
            sorted_array.extend(sorted(bucket))
        return sorted_array

# 测试桶排序
if __name__ == "__main__":
    arr = [2, 3, 5, 4, 1]
    s = Bucket()
    print(arr)
    arr2 = s.bucket_sort(arr, bucket_size=10)
    print("arr2", arr2)