class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = []
        postfix = []
        pre_product = 1
        post_product = 1

        for i in range(len(nums)):
            pre_product *= nums[i]
            prefix.append(pre_product)

        for j in reversed(range(len(nums))):
            post_product *= nums[j]
            postfix.append(post_product)


        postfix = list(reversed(postfix))
        prefix[:0] = [1]
        postfix.append(1)

        for k in range(len(nums)):
            num = prefix[k] * postfix[k+1]
            res.append(num)
            
        return res