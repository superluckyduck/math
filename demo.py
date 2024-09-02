import math


class heap:
    def heapsort(self,nums):
        arrLen = len(nums)
        for i in range(math.floor(arrLen/2),-1,-1):
            self.heapify(nums,arrLen,i)

        for i in range(arrLen-1,0,-1):
            nums[i],nums[0] = nums[0],nums[i]
            arrLen -= 1
            self.heapify(nums,arrLen,0)



    def heapify(self,nums,arrLen,i):
        left = 2*i+1
        right = 2*i+2
        max = i
        if left<arrLen and nums[left]>nums[max]:
            max = left
        if right<arrLen and nums[right]>nums[max]:
            max = right
        if max !=i:
            nums[max],nums[i] = nums[i],nums[max]
            self.heapify(nums,arrLen,max)

if __name__ == "__main__":
    arr = [1,3,5,2,6]
    h = heap()
    h.heapsort(arr)
    print(arr)