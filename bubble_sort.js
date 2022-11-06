function swap(a, b){
    [b,a] = [a, b];
}
/**
 * 
 * Array is sorted in 3 swaps.  
First Element: 1  
Last Element: 6  
 */
function countSwaps(a) {
    // Write your code here
    let swapCount = 0;
    for(let i=0;i<a.length;i++){
        for(let j=0;j<a.length-1;j++){
            if(a[j] > a[j+1]){
                
                [a[j], a[j+1]] = [a[j+1], a[j]];
                swapCount++;
            }
        }
    }
    console.log(`Array is sorted in ${swapCount} swaps.`)
    console.log(`First Element: ${a[0]} `)
    console.log(`Last Element: ${a[a.length - 1]} `)
}
