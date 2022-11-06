function evalRPN(tokens: string[]): number {
    const stack = []
    
    for(let i=0;i<tokens.length;i++){
        if(tokens[i] === '+' 
           || 
           tokens[i] === '/'
             || 
           tokens[i] === '*'
             || 
           tokens[i] === '-'
          )
          {
              const num2 = stack.pop();
              const num1 = stack.pop()
              
              stack.push(opr(tokens[i], num1, num2))
          }
        else{
            stack.push(Number(tokens[i]))
            console.log('Stack: ', stack)
        }
        
        
    }
    return Number(stack[0])
};
function opr(oper, num1, num2){
console.log(`${oper} ${num1} ${num2}`)
if(oper==='*') return num1 * num2;
 else if(oper==='-') return num1 - num2;
 else if(oper==='/'){
      const res = num1/num2;
     
     if(res > 0) return Math.floor(res)
     else return Math.ceil(res)
 }
 else if(oper==='+') return num1 + num2;
}