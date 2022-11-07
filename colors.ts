/**
 Do not return anything, modify nums in-place instead.
 */
 function sortColors(nums: number[]): void {
    //  if(nums.length <=  2) return
      if(nums.length <= 1) return;
       const max = Math.max(...nums);
       const index = new Array(max + 1);
       const sorted = new Array(nums.length)
      index.fill(0);
      
      for(let i = 0;i<nums.length;i++){
          index[nums[i]]++;
  
      }
      console.log(`Occurence ${index}`)
  
      for(let i=0;i<nums.length+1;i++){
          if(i!=0){
              console.log(index[i], ' ', index[i-1])
              index[i] += index[i-1];
              
          }
      }
      console.log(`Cumm ${index}`)
      for(let i=0;i<nums.length;i++){
          sorted[index[nums[i]] - 1] =nums[i];
          index[nums[i]] --;
      }
      for(let i=0;i<sorted.length;i++) nums[i] = sorted[i]
       console.log({sorted})
  };