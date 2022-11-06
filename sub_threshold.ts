function numOfSubarrays(arr: number[], k: number, threshold: number): number {
    let num = 0;
    let start = 0, end = 0;
    let sum = 0;
    for(;end<arr.length+1;end++){
      
       if(end-start == k){
             const avg = sum/k;
          // console.log(arr.slice(start, end), {sum, avg})
         
           if(avg >= threshold) num++;
           sum -= arr[start]
           start++;
       }
        sum += arr[end];
        
    }
    return num;
};