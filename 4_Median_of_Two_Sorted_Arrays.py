
class Solution():
    def findMedianSortedArrays(self, nums1: list[int], nums2:list[int]) -> int:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums=nums1+nums2
        nums.sort()
        if len(nums)%2==0:
            return (nums[int(len(nums)/2)-1]+nums[int(len(nums)/2)])/2
        else:
            return  nums[int(len(nums)/2)]
        # return len(nums)#statistics.mean(nums)
if __name__ == '__main__':
    s=Solution()
    print(s.findMedianSortedArrays(nums1=[1,2,3,1,2,3,1,2,3,1,2,3],nums2=[2,4,4,8,2,4,4,8,2,4,4,8,2,4,4,8]))
