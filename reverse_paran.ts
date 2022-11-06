function reverseParentheses(s: string): string {
    const openStack = [];
    const closeStack = [];
    let finalStrArr = s.split('')
    let final = []
    
    for(let i= 0;i<s.length;i++){
        const char = s[i];
        if(char === '(') openStack.push(i);
        else if(char === ')'){
            const j = (openStack.pop()+1)
            const flip = final.slice(j, i).reverse() 
            console.log(flip)
            final.splice(j, i, ...flip)
            console.log(`flipped ${final}`)
        }
        final.push(char)
        
    }

    console.log(openStack)
    console.log(closeStack)
   return final.filter(char=>char!=')' && char != '(').join('')
};