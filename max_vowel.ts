function maxVowels(s: string, k: number): number {
    if(s.length == k) return k;
    let start =0;
    let end = 0;
    let max = 0;
    let current = 0;
    const isVowel = (ch) => {
        return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u'
    
    }

    for(;end<s.length+1;end++){
        if(isVowel(s[end])){
           current++;
        }
        if(end - start  == k){
           // console.log('substring ', s.substring(start, end))
            if(isVowel(s[start])) current--
            start++;
            
        }
        max = Math.max(max, current)
    }
    return max;
};