class Solution:
    def two_sum(self, nums, target):
        """This fuction returns the indices of the two numbers within the array, that add up to the target value.

        :param nums: array of integers
        :type nums: array

        :param target: target value
        :type target: int
        
        :return: output
        :rtype: array
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] + nums[i] == target:
                    return [i,j]
                


if __name__=="__main__":
    nums=[3,2,4]
    target = 6
    solution = Solution()
    output = solution.two_sum(nums,target)
    print(output)