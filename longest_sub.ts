function lengthOfLongestSubstring(s: string): number {
    let longest: number = 0;
    
    const set = new Set();
    let start = 0, end =0;
    for(;end<s.length && start<s.length;){
           if(!set.has(s[end])){
               set.add(s[end++]);
               if(longest < end-start) longest = end-start;

           }
           else{
              set.delete(s[start++])
           }
    } 

    return longest

};