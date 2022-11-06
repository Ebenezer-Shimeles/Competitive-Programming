function longestOnes(nums: number[], k: number): number {
    if(nums.length == k) return nums.length;
    let ans =0;
    let fast = 0, slow = 0;
    let zero = 0;

    for(;fast<nums.length;fast++){
        if(nums[fast] == 0) zero++;

        while(zero > k){
            if(nums[slow++] == 0) zero--;
        }
        ans = Math.max(ans, fast-slow+1)
    }
    return ans

};