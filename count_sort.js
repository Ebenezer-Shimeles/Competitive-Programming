function countingSort(arr) {
    // Write your code here
    const freqs = (new Array(100)).fill(0)
    
    for(const num of arr){
        freqs[num]++;
    }
    return freqs
    
    
}