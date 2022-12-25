function transpose(matrix: number[][]): number[][] {
    if(!matrix) return matrix;

    const rowSize: number = matrix[0].length;
    const colSize: number = matrix.length;

    const result: number[][] = Array(rowSize);
    
    for(let i=0;i<rowSize;i++){
        result[i] = new Array(colSize)
    }
    
    for(let i=0;i<colSize;i++){
        for(let j=0;j<rowSize;j++){
             
             result[j][i] = matrix[i][j];
             //console.log(`Setting ${j} ${i} to ${matrix[i][j]} `, {result})
             // got a lot of output limit exceeded becaue of this guy ;(

        }
    }

 
    return result;

};