class Merge:
    def mergeSort(self,arr):
        import math
        if(len(arr)<2):
            return arr
        s = Merge()
        middle = math.floor(len(arr)/2)
        left, right = arr[0:middle], arr[middle:]
        return s.merge(s.mergeSort(left), s.mergeSort(right))

    def merge(self,left,right):
        result = []
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        while left:
            result.append(left.pop(0))
        while right:
            result.append(right.pop(0))
        return result

class MergeStatic:
    @staticmethod
    def mergeSort(arr):
        import math
        if(len(arr)<2):
            return arr
        middle = math.floor(len(arr)/2)
        left, right = arr[0:middle], arr[middle:]
        return MergeStatic.merge(MergeStatic.mergeSort(left), MergeStatic.mergeSort(right))
    @staticmethod
    def merge(right,left):
        result = []
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        while left:
            result.append(left.pop(0))
        while right:
            result.append(right.pop(0))
        return result

if __name__ == "__main__":
    #创建实例对象
    s = Merge()
    arr = [2,3,5,4,1]
    arr2 = s.mergeSort(arr.copy())
    print("arr2",arr2)
    print(arr)
    arr3 = MergeStatic.mergeSort(arr.copy())
    print("arr3",arr3)