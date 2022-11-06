class MinStack {
    private min = (1/0)
    private minArr = []
    private stack = []
    constructor() {

    }
    
    push(val: number): void {
       this.stack.push(val);
       if(this.min >= val){
           this.min = val;
           this.minArr.push(this.min)
       }
    }

    pop(): void {
        
        const ret =  this.stack.pop()
        if(ret == this.minArr[this.minArr.length - 1]){
            console.log('poping from top')
            this.minArr.pop();
            this.min = this.minArr[this.minArr.length-1];
        }
        if(this.stack.length == 0){
             this.minArr = [];
             this.min = 1/0
        }
        return ret;
    }

    top(): number {
        return this.stack[this.stack.length - 1]
    }

    getMin(): number {
        return this.min
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */