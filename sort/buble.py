#动态方法
class Bubble:
    def bubbleSort(self,arr):
        n= len(arr)
        for i in range(n):
            for j in range(n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr

#静态方法
class BubbleStatic:
    @staticmethod
    def bubbleSort(arr):
        n= len(arr)
        for i in range(n):
            for j in range(n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr

if __name__ == "__main__":
    #创建实例对象
    s = Bubble()
    arr = [2,3,5,4,1]
    arr2 = s.bubbleSort(arr.copy())
    print("arr2",arr2)
    print(arr)
    arr3 = BubbleStatic.bubbleSort(arr.copy())
    print("arr3",arr3)