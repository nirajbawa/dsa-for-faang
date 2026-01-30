class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        dup = nums.copy()
        kd = k%n

        for i in range(0, n):
            nums[(k+i)%n] = dup[i]


