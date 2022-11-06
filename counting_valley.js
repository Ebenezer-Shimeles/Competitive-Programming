function countingValleys(steps, path) {
    // Write your code here
    let count = 0;
    let val = 0;
    let isDownV = false;
    for(let i=0;i<path.length;i++){
        if(path[i] == 'U') val++;
        if(isDownV && path[i] == 'U' && val ===0) count++;
        if(path[i] == 'D'){ val--; isDownV = true}
    }
    
    return count;

}