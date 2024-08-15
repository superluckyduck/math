import math


class Sort:
    def Bubblesort(self,arr):
        n = len(arr)
        for i in range(n):
            for j in range(n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]

    def Quick(self,arr):
        n = len(arr)
        self.QuickSort(arr,0,n-1)

    def QuickSort(self,arr,left,right):
        if left<right:
            index = self.Quickly(arr,left,right)
            self.QuickSort(arr,left,index)
            self.QuickSort(arr,index+1,right)

    def Quickly(self,arr,left,right):
        fixed = left
        index = left+1
        for i in range(left,right+1):
            if arr[i]<arr[fixed]:
                arr[i],arr[index]= arr[index],arr[i]
                index +=1
        arr[fixed],arr[index-1] = arr[index-1],arr[fixed]
        return index-1


    def Insert(self,arr):
        n = len(arr)
        for i in range(n):
            num = arr[i]
            j=i-1
            while j>=0 and arr[j]>num:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = num

    def Merge(self,arr):
        if len(arr)<2:
            return arr
        mid = math.floor(len(arr)/2)
        left = arr[0:mid]
        right = arr[mid:]
        return self.MergeSort(self.Merge(left),self.Merge(right))
    def MergeSort(self,left,right):
        res = []
        while left and right:
            if left[0]<=right[0]:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))
        while left:
            res.append(left.pop(0))
        while right:
            res.append(right.pop(0))
        return res



if __name__ == "__main__":
    array = [1,6,3,2,4]
    s = Sort()
    # s.Bubblesort(array)
    # s.Quick(array)
    # s.Insert(array)
    new = s.Merge(array)
    print(array)
    print(new)
