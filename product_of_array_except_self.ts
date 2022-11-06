function productExceptSelf(nums: number[]): number[] {
    const prods = [];
    
    const left = new Array(nums.length)
    const right = new Array(nums.length)
   
    left.fill(1);
    right.fill(1);
    
    for(let  i =0;i<nums.length;i++){
        if(i == 0){
            left[i] = nums[i];
            right[nums.length -1 - i] = nums[nums.length -  1];
        }
        else{
            left[i] = nums[i] * left[i-1];
            right[nums.length - 1 - i] = nums[nums.length - 1 - i] * right[nums.length - i ]
        }
    }
    for(let i=0;i<nums.length;i++){
        if(i == nums.length - 1){
            console.log('ca;')
            prods[i] = left[nums.length - 2]
       }
      else if(i!=0)
        {
              prods[i] = right[i+1] * left[i-1]
              console.log(`i=${i} ${ right[nums.length - 1 -i]} * ${left[i-1]}`)
       }
      
       else{
           prods[i] = right[i+1]
       }
    }
    console.log({right, left})
    return prods
};