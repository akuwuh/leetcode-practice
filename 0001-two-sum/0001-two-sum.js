/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let a= [];
    let x; 
    
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1 ; j < nums.length; j++) {
            x = target - nums[i]
            if (nums[j] === x ){
                a = [i,j];
                return a;
            }
        }
            
    }
    
    return null;
};