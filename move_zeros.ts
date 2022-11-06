/**
 Do not return anything, modify nums in-place instead.
 */
 function moveZeroes(nums: number[]): void {
    let zeroIndex = 0;
    let normalIndex = 0;

    while(zeroIndex + normalIndex < nums.length){
        if(nums[normalIndex] == 0){
            nums.splice(normalIndex, 1);
            nums.push(0);
            zeroIndex++;
        }
        else normalIndex++;
    }
};