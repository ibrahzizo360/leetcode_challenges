/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let max = nums[0]
    let curSum = 0;

    for(num of nums){
        if (curSum < 0){
            curSum = 0
        }

        curSum += num
        max = Math.max(curSum, max)
    }

    return max
};