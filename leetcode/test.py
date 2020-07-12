class Solution:
    def twoSum(self, nums, target):
        nums_list = {}
        for i in range (0, len(nums), i):
            nums_list[nums[i]] = i
            
        return nums_list
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]

if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    clients = []

    for _ in range(n):
        clients.append(list(map(int, input().rstrip().split())))

    print(nm)
