function maxSum(grid: number[][]): number {
    //tuns on o(n)
    const colSize = grid.length;
    const rowSize = grid[0].length;
    let max: number = -(1/0);

    const aSums = [];
    for(let i=0;i<colSize;i++){
        //goes through trying to find the prefix sums
        const times = grid[i].length == 3 ? 1 : grid[i].length - 2;  
        const sums = new Array(times);
        sums.fill(0);
        for(let j=0;j<  times ;j++){
            console.log(`Col = ${i} att = ${j}`);
            if(j == 0){
             let tSum = 0;
              for(let k=0;k<3;k++){
                  tSum += grid[i][k];
              }
              sums[0] = tSum;
            }
            else{
               sums[j] = sums[j-1] + grid[i][j+2] - grid[i][j-1];
            }

        }
        aSums.push(sums);
    }
    console.log({aSums});
    
    for(let i=0;i<colSize - 2; i++){
        const sumRow = aSums[i];
        for(let j=0;j<sumRow.length;j++){
            let s = sumRow[j] + aSums[i+2][j] + grid[i+1][j+1];
            if(s > max) max = s;
        }      
    }
     //first find the sums of 
    return max;
};