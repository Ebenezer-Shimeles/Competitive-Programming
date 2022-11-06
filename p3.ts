function isPowerOfThree(n: number): boolean {
    console.log(n, ' ', n === 1)
     if(n === 1 ){ 
         console.log('ret')
          return true;
     }
     const rem = n/3;
     if(!Number.isInteger(rem) || n == 0) return false;

     else return isPowerOfThree(rem)
};