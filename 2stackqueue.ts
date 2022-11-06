class MyQueue {
    private mainStack: any[] = []; //main stack
    private tempStack: any[] = [];
    constructor() {

    }

    push(x: number): void {
        this.mainStack.push(x);
    }

    pop(): number {
        const len = this.mainStack.length
        for(let i=0;i<len - 1;i++){
           
            this.tempStack.push(this.mainStack.pop())
        }
        const val = this.mainStack.pop()
        
        const tempLen = this.tempStack.length;
        for(let i=0;i<tempLen;i++){
            this.mainStack.push(this.tempStack.pop())
        }
        return val
    }

    peek(): number {
          const len = this.mainStack.length
        for(let i=0;i<len - 1;i++){
           
            this.tempStack.push(this.mainStack.pop())
        }
        const val = this.mainStack[0]
        
        const tempLen = this.tempStack.length;
        for(let i=0;i<tempLen;i++){
            this.mainStack.push(this.tempStack.pop())
        }
        return val
    }

    empty(): boolean {
         return this.mainStack.length === 0
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */