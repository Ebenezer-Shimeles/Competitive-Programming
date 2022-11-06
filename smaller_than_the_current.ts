function smallerNumbersThanCurrent(nums: number[]): number[] {
    const smaller = [];

    const max = Math.max(...nums);
    const array = (new Array(max)).fill(0);
    
    
    nums.forEach(num =>{
        array[num]++;
    })
    for(let i=0;i<array.length-1;i++){
        array[i+1] += array[i];
    }
    console.log(array);
    nums.forEach(num =>{
        const ans = array[num-1]
        if(ans) smaller.push(ans)
        else smaller.push(0)
    })
    return smaller
    
};