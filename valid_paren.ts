function isValid(s: string): boolean {
    const stack = []
    
    for(const char of s){
        if(char == '[' || char == '{' || char =='(' ) 
        {
          //  if(stack.length) return false;
             stack.push(char)
        } 
        else if(char == '}')
        {
             if(stack.pop()!='{') return false;   
        }
        else if(char == ']')
        {
              if(stack.pop()!='[') return false;
        }
        else if(char == ')')
        {
              if(stack.pop()!='(') return false;
        }
    }
   return stack.length  == 0;
};