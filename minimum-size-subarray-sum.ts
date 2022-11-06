function minSubArrayLen(target: number, nums: number[]): number {
    let minLen: number = 1/0;
    let start: number = 0;
    let end: number = 0;
    let currentSum : number = 0;
    for(;end<nums.length; end++){
        currentSum += nums[end];
        while(currentSum >= target){
            console.log('gt')
            minLen = Math.min(minLen, end - start + 1);
            console.log({minLen})

            currentSum -= nums[start] 
            start++;
        }

    }
    if(!Number.isFinite(minLen)) return 0;
    return minLen;

};