#快速排序
# class Solution:
#     def quick_sort(self,arr):
#         if len(arr) < 2:
#             return arr
#         else:
#             pivot = arr[0]
#             less = [i for i in arr[1:] if i <= pivot]
#             greater = [i for i in arr[1:] if i > pivot]
#             return self.quick_sort(less) + [pivot] + self.quick_sort(greater)
#
# Quick_Sort = Solution()
# print(Quick_Sort.quick_sort([10, 5, 2, 3]))

#冒泡排序

#选择排序

#归并排序
def merge_sort(arr):
    def marge(left, right):
        result = []
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result += left
        result += right
        return result

    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    return marge(merge_sort(left), merge_sort(right))
arr = [8, 2, 5, 0, 7, 4, 6, 1]
print(merge_sort(arr))