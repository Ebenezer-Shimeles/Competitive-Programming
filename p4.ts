function isPowerOfFour(n: number): boolean {
    if(n == 1) return true;
    const rem = n /4
    if(!Number.isInteger(rem) || n == 0) return false;

    return isPowerOfFour(rem)
};