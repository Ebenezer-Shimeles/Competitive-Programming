function numIdenticalPairs(nums: number[]): number {
    let pairs = 0;
     for(let i =0;i<nums.length;i++){
         for(let j=i ;j<nums.length;j++){
              if(nums[i] == nums[j]){
                  if(i==j) continue;
                  pairs++;
                  console.log(nums[i], ' ', nums[j], ' ', i, ' ', j)
              }
         }
     }
     return pairs;
};