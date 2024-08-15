import random


def random_access(nums: list[int])-> int:
    random_index = random.randint(0,len(nums)-1)
    random_num = nums[random_index]
    return random_num

def insert(nums:list[int],index:int,num:int):
    for i in range(len(nums)-1,index,-1):
        nums[i] = nums[i-1]
    nums[index] = num

def remove(nums:list[int],index):
    for i in range(index,len(nums)-1):
        nums[i] = nums[i+1]

def find(nums:list[int],num:int)->int:
    for i in range(len(nums)):
        if nums[i] == num:
            return i
    return -1

def extend(nums:list[int],num:int)->list[int]:
    res = [0]*(len(nums)+num)
    for i in range(len(nums)):
        res[i] = nums[i]
    return res

if __name__ == "__main__":
    arr: list[int] = [0]*5
    nums: list[int] = [1,3,4,5,2]
    num = random_access(nums)
    print(num)
    print(nums)
    insert(nums,3,6)
    print(nums)
    remove(nums,3)
    print(nums)
    f = find(nums,3)
    print(f)
    new = extend(nums,5)
    print(new)