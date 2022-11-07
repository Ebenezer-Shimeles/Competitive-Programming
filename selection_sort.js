
//User function Template for javascript

/**
 *
 * select
 * @param {number[]} arr
 * @param {number} i
 * @return {number}
 *
 * selectionSort
 * @param {number[]} arr
 * @param {number} n
 */
 class Solution
 {
   select(arr,i){
      // code here such that selectionSort() sorts arr[]
      const chosenArray = arr.slice(i, arr.length);
      // console.log({chosenArray})
      let min = chosenArray[0];
      let minIndex= 0;
      for(let i=0;i<chosenArray.length;i++){
          if(chosenArray[i] < min){ 
               min = chosenArray[i];
               minIndex = i;
          }
          
      }
      arr.splice(minIndex+i, 1)
      //console.log('deleting at ', minIndex)
      //console.log('chosen ', min)
      return min;
   }
 
   //Function to sort the array using selection sort algorithm.
   selectionSort(arr,n){
    //code here
       const newArray = [1]
       for(let i=0;i<n;i++){
           arr.splice(i, 0, this.select(arr, i))
          // console.log('current array ', arr)
       }
   }
     
 }