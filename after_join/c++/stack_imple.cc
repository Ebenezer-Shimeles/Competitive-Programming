#include <iostream>
#include <memory>
#include <exception>

#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <cstdio>
#include <cstring>
/**
 * 
 *   Stack Implementation
 *   one is ArrayStack , Other is PointerStack
 *   All functions must have a time complexity of O(1) not inlcuding the destructors
*/
#define NILL -1

constexpr size_t DEFAULT_STACK_SIZE = 10;

template<class T>
class Stack{   
public:
   virtual void Print() = 0;
   virtual void create(size_t capacity = DEFAULT_STACK_SIZE) = 0;
   virtual T Pop() = 0;
   virtual void Push(T) = 0;
   virtual T Peep() = 0;
   virtual bool IsEmpty() const = 0;
   virtual ~Stack(){
   	   std::cout << "Stack deleted :(\a\n";
   }
};

class MemoryException: public std::exception
{
	const char* what() {
	   return "Unable to allocate memory for stack!\a\n";
	}
};

class StackOverflowException: public std::exception {
	const char * what() {
	    return "Stack is full !\n\a";
	}
};



template<class T>
class ArrayStack : public Stack<T>{
public:
	void Print(){
		if(top == NILL){
			throw std::logic_error("Error the stack is empty!");
		}
		std::cout <<"TOP => "<<top << " [";
		for(size_t i=top;i>=0;i--){
			std::cout <<"I " << i<<" "<< base[i] << ",";
		}
		std::cout << "]\n";
	}
	ArrayStack(size_t s = DEFAULT_STACK_SIZE){
		create(s);
		
		memset(base, '\0', s);
	}
	~ArrayStack(){
		delete [] base;
	}
	
	T Pop(){
		//check if it's empty
		if(top == NILL){
			throw std::logic_error("Error the stack is empty!");
		}
		return base[top--];
	}
	bool IsEmpty() const{
		return top ==  NILL;
	}
	T Peep(){
		if(top == NILL){
			throw std::logic_error("Error the stack is empty!");
		}
		return base[top];
	}
	void Push(T data){
//		if(top == NILL){
//			throw std::logic_error("Error stack is empty!");
//		}
		if(top == capacity){
			throw StackOverflowException();
		}
		base[++top] = data;
	}
	
	void create(size_t size){
		base = new T[size];
		capacity = size;
	}
private:
	 size_t capacity;
     T *base;
     signed long long  top = NILL;       

};

template<typename T>
struct OneNode{
	OneNode(){}
	OneNode(T data){
		this->data= data;
	}
	T data;
	OneNode<T> *next;
};

template<class T>
class PointerStack: public Stack<T>{
private:
	OneNode<T> *_root;
public:
	void Print(){
		
	}
    void create(size_t capacity = DEFAULT_STACK_SIZE){
       //doesn't make sense here	
    }
    T Pop(){
     	if(IsEmpty()){
     		throw std::logic_error("Error the stack is empty");
		 }
		 auto data = Peep();
		 _root = _root->next;
		 return data;
	 }
    void Push(T data){
    	auto new_top = new (std::nothrow)OneNode<T>(data);
    	if(!new_top){
    		throw MemoryException();
		}
    	new_top->next = _root;
    	_root = new_top;
	}
    T Peep(){
    	if(IsEmpty()){
     		throw std::logic_error("Error the stack is empty");
		 }
		 return _root->data;
	}
    bool IsEmpty() const noexcept{
    	return _root == nullptr;
	}
    ~PointerStack(){
    	auto tmp = _root;
    	
    	while(tmp){
    		auto t = tmp->next;
    		delete tmp;
    		tmp = t;
		}
		std::cout << "\nPointerStack deleted!:(";
	}

};

bool IsOperation(int64_t i){
	return i == '*' || i == '/' || i == '^' || i == '-' || i == '+';
}

typedef long double float32_t; 

float32_t EvalPostSingle(unsigned char opr, Stack<float32_t> *stack){
	auto op1 = stack->Pop() - '0';
	auto op2 = stack->Pop() - '0';
	
	int64_t result;
	
	switch(opr){
		case '+':
			result = op1 + op2;
			std::cout <<op1<<'+'<<op2<<'='<<result<<'\n';
			break;
		case '-':
			result = op1 - op2;
			break;
		case '/':
			result = op1/op2;
			break;
		case '*':
			
			result = op1 * op2;
			std::cout <<op1<<'*'<<op2<<'='<<result<<'\n';
			break;
		case '^':
			result = pow(op1 ,op2);
			break;
			
	}
	return result;
}
float32_t EvalPostfix(int64_t* postfix, size_t len){
	auto stack = std::unique_ptr<Stack<float32_t>>(new PointerStack<float32_t>());
	
	for(size_t i=0;i<len;i++){
		if(IsOperation(postfix[i])){
			auto result = EvalPostSingle(postfix[i], stack.get());
			std::cout << "Res: "<< "  " << result << '\n';
			stack->Push(result);
			std::cout << "Now stack: \n";
			stack->Print();
		}
		else{
		   stack->Push(postfix[i]);	
		   	std::cout << "Now stack: ";
			stack->Print();
		}
		
	}
	return stack->Pop();
}



int main(){
   using namespace std;
//   auto s =  shared_ptr<Stack<int>>( new PointerStack<int>() );
//
//   uint64_t num;
//   cout << "Please input the number u want to change to bin: ";
//   cin >> num;
//   
//   while(num){
//   	s->Push(num % 2);
//   	num /=2;
//   }
//   
//   while(!s->IsEmpty()){
//   	 cout << s->Pop();
//   }
   int64_t postfix[] = {'1', '1', '2', '*', '+'};
   cout << "Evali 1+1/2: " << EvalPostfix(postfix, 5) + '0'<<'\n';
   
}
