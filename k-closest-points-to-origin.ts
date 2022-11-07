function kClosest(points: number[][], k: number): number[][] {
    const distances = [];
   
    points.forEach(
        ([x, y])=>{
          distances.push(Math.pow(x, 2) + Math.pow(y, 2) )
        } 
    )
    console.log(distances);
    let sortedIndex = 0;

    for(;sortedIndex<distances.length;sortedIndex++){
        let minIndex = sortedIndex;
        let min = distances[minIndex];
        let pt = points[minIndex]
        for(let j=minIndex;j<distances.length;j++){
            if(distances[j] < min){
                minIndex = j;
                min = distances[j];
                pt = points[j]
            }
        } 
        console.log({min})
        points.splice(minIndex, 1);
        points.splice(sortedIndex, 0, pt)

        distances.splice(minIndex, 1);
        distances.splice(sortedIndex, 0, min)  

    }
    console.log(distances)

    return points.slice(0, k)

};