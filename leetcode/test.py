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

def ceasar_cipher(original, key):
    encrypted = ''
    for i in range (len(original)):
        char = chr(ord(original[i]) + key) if ord(original[i]) + key <= 122 else chr(ord(original[i]) + key - 26)
        encrypted += char
        pass
    return encrypted


def decrypt(encrypted, key):
    decrypted = ''
    for i in range (len(encrypted)):
        char = chr(ord(encrypted[i]) - key) if ord(encrypted[i]) - key >= 97 else chr(ord(encrypted[i]) - key + 26)
        decrypted += char
        pass
    return decrypted

if __name__ == '__main__':

    # try:
    #     int(input("Enter a number: "))
    # except ZeroDivisionError as err:
    #     print(err)
    # except ValueError as err:
    #     print(err)


    bob = ['a', 'b', 'c', 'd', 'e']

    index = int(input())
    
    print(bob[index])

    # nm = input().split()

    # n = int(nm[0])

    # clients = []

    # for _ in range(n):
    #     clients.append(list(map(int, input().rstrip().split())))

    # print(nm)
