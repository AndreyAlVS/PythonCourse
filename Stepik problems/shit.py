class Solution:
    def __init__(self):
        self.nums1 = nums1
        self.m = m
        self.nums2 = nums2
        self.n = n


def merge_(num1: list[int], o: int, num2: list[int], p: int) -> list:
    for _ in range(o):
        if num1[-1] == 0:
            num1.remove(num1[-1])
    for _ in range(p):
        if num2[-1] == 0:
            num2.remove(num2[-1])
    nums3 = num1 + num2
    nums3.sort()
    return nums3


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    res = merge_(nums1, m, nums2, n)
    print(res)
