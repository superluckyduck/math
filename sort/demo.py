import math
class New:
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

if __name__ == "__main__":
    s = New()
    arr = [2,7,5,3,4]
    print("原来的数组：",arr)
    new = s.Merge(arr)
    print(new)