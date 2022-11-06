function chalkReplacer(chalk: number[], k: number): number {
    const len = chalk.length;
  
    let sum = 0;
    chalk.forEach(s=>sum+=s)
    k = k % sum

    if(!k) return 0

    for(let i=0;i<chalk.length;i++){
        k = k - chalk[i];
        if(k < 0) return i
      
    }
  
};