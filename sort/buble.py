#动态方法
class Buble:
    def bulbleSort(self,arr):
        n= len(arr)
        for i in range(n):
            for j in range(n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    print(arr)
        return arr

#静态方法
class BubleStatic:
    @staticmethod
    def bulbleSort(arr):
        n= len(arr)
        for i in range(n):
            for j in range(n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    print(arr)
        return arr