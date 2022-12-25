function isPalindrome(s: string): boolean {
    if(!s || !(s.length) || s.length <= 1) {
        //console.log('simple so returning true')
        return true;
    }
    const alpha = s.replace( /[^A-Za-z0-9]/g, "");
    
    let str2 = "";
    for(let i=0;i<alpha.length;i++){
            str2 += alpha[i].toLowerCase();
    }
    console.log(`Alpha = ${str2.split('')}`)
    for(let i=0;i<str2.length;i++){
      //  console.log('checking ', i, 'and ', str2.length - i - 1)
       if(str2[i] != str2[str2.length - i - 1]) return false;
    }
    return true;
};
