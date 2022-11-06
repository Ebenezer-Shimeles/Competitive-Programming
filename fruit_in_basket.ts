function totalFruit(fruits: number[]): number {
    let max = 0;
    let start = 0, end = 0;
    const map  = new Map();
    for(;end<fruits.length;end++){

          if(!map.has(fruits[end])){
              map.set(fruits[end], 1);
          }
          else{
              map.set(fruits[end], Number(map.get(fruits[end]) + 1)); 
          }
          while(map.size > 2){
              const val = Number(map.get(fruits[start]));
              map.set(fruits[start], val-1)
              if(Number(map.get(fruits[start]) == 0)){
                  map.delete(fruits[start])
              }
              start++;
              
          }
         max = Math.max(max, start-end + 1)

    }
    return max;
};