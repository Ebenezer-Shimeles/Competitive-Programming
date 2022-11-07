function targetIndices(nums: number[], target: number): number[] {
    const targets = []
    const max = Math.max(...nums);
    
    const indexes = (new Array(max+1));
    indexes.fill(0);
    console.log(`Init index = ${indexes}`)
    
    for(let i =0;i<nums.length;i++){
        console.log(nums[i])
        indexes[nums[i]]++;
    }
    console.log(`Occurence Index ${indexes}`)
    
    for(let i = 0;i<indexes.length;i++){
        if(i == 0){
           
        }else{
          indexes[i] += indexes[i-1]
        }
    }
    console.log(indexes)
    const sorted = (new Array(nums.length-1))
    sorted.fill(0)

    for(let i=0;i<nums.length;i++){
        console.log(`Inserting ${nums[i]}`)
        if(indexes[nums[i] ] - 1 >= 0) sorted[indexes[nums[i] ] - 1] = nums[i];
         if(indexes[nums[i] ] - 1 >= 0) indexes[nums[i]]--;
    }
     nums = sorted
     for(let i = 0;i<sorted.length;i++){
         if(sorted[i] === target){
             targets.push(i)
         }
     }
     console.log({sorted})


    return targets   
};