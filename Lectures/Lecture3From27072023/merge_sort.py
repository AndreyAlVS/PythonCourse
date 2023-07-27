def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k +=1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k +=1
list1 = [1, 2, 44, 56, 65, 12, 79, 31, 54, 78, 16]
merge_sort(list1)
print(list1)