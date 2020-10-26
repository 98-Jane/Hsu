#寻找两个正序数组的中位数  时间复杂度O(log(m+n))
#给定两个大小为m和n的正序（从小到大）数组 nums1 和 nums2，请找出并返回这两个正序数组的中位数
# 输入：nums1 = [1,3], nums2 = [2]  输出：2.00000  解释：合并数组 = [1,2,3] ，中位数 2
# 输入：nums1 = [1,2], nums2 = [3,4]  输出：2.50000  解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
# 输入：nums1 = [0,0], nums2 = [0,0]  输出：0.00000
# 输入：nums1 = [], nums2 = [1]  输出：1.00000

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k1 = ( len(nums1) + len(nums2) + 1 ) // 2
        k2 = ( len(nums1) + len(nums2) + 2 ) // 2
        def helper(nums1,nums2,k): #本质上是找第k小的数
            if(len(nums1) <len(nums2) ):
                nums1, nums2 = nums2 , nums1 #保持nums1比较长
            if(len(nums2)==0):
                return nums1[k-1] # 短数组空，直接返回
            if(k==1):
                return min(nums1[0],nums2[0])  #找最小数，比较数组首位
            t = min(k//2,len(nums2)) # 保证不上溢
            if( nums1[t-1]>=nums2[t-1] ):
                return helper(nums1 , nums2[t:],k-t)
            else:
                return helper(nums1[t:],nums2,k-t)
        return ( helper(nums1,nums2,k1) + helper(nums1,nums2,k2) ) /2



