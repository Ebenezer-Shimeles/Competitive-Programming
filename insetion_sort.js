function printArray(arr){
    for(let i =0;i<arr.length;i++)
         process.stdout.write(arr[i] + " ")
    
    console.log("")
}
function insertionSort1(n, arr) {
    // Write your code here
    let currentIndex = 0;
    
    
    for(;currentIndex < n;currentIndex++){
        let minimum = arr[currentIndex];
        let minimumIndex = currentIndex;
        for(let j=currentIndex;j<n;j++){
            if(minimum > arr[j]){
                minimumIndex = j;
                minimum = arr[j];
            }
        }
        arr.splice(minimumIndex, 1);
        arr.splice(currentIndex,0,  minimum)
        printArray(arr)
        
    }
    
} 