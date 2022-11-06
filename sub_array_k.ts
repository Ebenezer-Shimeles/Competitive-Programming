function subarraySum(nums: number[], k: number): number {
    let e = 0;
    const prefixSum = (new Array(0))
    prefixSum.fill(0)
    let sum = 0

    // for(let i=0;i<nums.length;i++){
    //     if(i == 0) prefixSum[i] = nums[i]
    //     else{
    //         prefixSum[i] = nums[i] + prefixSum[i-1];
    //     }

    // }
    // const getSum = (start, end) =>{
    //     if(start === 0) return prefixSum[end];
    //     else return prefixSum[end] - prefixSum[start-1];
    // }  
    // console.log({prefixSum})
    // console.log(getSum(0,1), ' ', getSum(1, 2))
    // let start = 0;

    // for(let end=start; end<nums.length;end++){
        
    //     if(nums[end] == k&& nums.length != 1) e++;
    //     const cSum = getSum(start, end)
    //     console.log('checking ', {start, end, cSum})
    //     if(cSum > k){
    //         start++;
    //     }
    //     if(cSum == k){
    //         e++;
    //         start++;
    //     }


    // }
    let m = new Map();

    for (let i = 0; i < nums.length; i++)
    {
        sum += nums[i];
        if(sum == k) e++;
        if (m.has(sum - k))
                e += m.get(sum - k);
  
          
            let count = m.get(sum);
            if (count == null)
                m.set(sum, 1);
            else
                m.set(sum, count + 1);
        }
        return e;
      //  return e;
};