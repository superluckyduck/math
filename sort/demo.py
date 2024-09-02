import math
#归并
class Merge:
    def Merge(self,arr):
        n = len(arr)
        if n<2:
            return arr
        mid = math.floor(n/2)
        left,right = arr[0:mid],arr[mid:]
        return self.merge_sort(self.Merge(left),self.Merge(right))
    def merge_sort(self,left,right):
        out = []
        i = 0
        while (len(left) != 0 and len(right) != 0 ):
            if left[0] <= right[0]:
                out.append(left.pop(0))
            else:
                out.append(right.pop(0))
            i +=1
        while len(left) != 0:
            out.append(left.pop(0))
        while len(right) != 0:
            out.append(right.pop(0))
        return out

#选择
class Select:
    def select(self,arr):
        n = len(arr)
        for i in range(n):
            index = i
            for j in range(i,n):
                if arr[index]>arr[j]:
                    index = j
            arr[index],arr[i] = arr[i],arr[index]
        return arr
#桶
class Bucket:
    def bucket(self,arr,b):
        maxVal = max(arr)
        minVal = min(arr)
        count = (maxVal-minVal)//b+1
        buckets = [[] for _ in range(count)]
        for num in arr:
            index = (num-minVal)//b
            buckets[index].append(num)
        sorter = []
        for val in buckets:
            sorter.extend(sorted(val))
        return sorter
#计数
class Counting:
    def counting(self,arr):
        maxVal = max(arr)
        sorter = [0]*(maxVal+1)
        for num in arr:
            sorter[num] += 1
        index = 0
        for j in range(maxVal+1):
            while sorter[j] > 0:
                arr[index] = j
                index += 1
                sorter[j] -= 1
        return arr






if __name__ == "__main__":
    s = Merge()
    arr = [2,7,5,3,4]
    print("原来的数组：",arr)
    new = s.Merge(arr)
    print(new)
    s = Select()
    print("原来的数组：", arr)
    new = s.select(arr.copy())
    print(new)
    s = Bucket()
    print("原来的数组：", arr)
    new = s.bucket(arr.copy(),2)
    print(new)
    s = Counting()
    print("原来的数组：", arr)
    new = s.counting(arr.copy())
    print(new)