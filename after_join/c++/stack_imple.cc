#include <iostream>
#include <memory>
#include <exception>
#include <sstream>

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
 *   Which hav O(n) n being the size of the stack
 *   I am generallry not trying to use anything in std c++ expcept i/o
 *   Also using the stack to do some stuff
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
   	   std::cout << "Stack deleted :(\n";
   }
};

class MemoryException: public std::exception
{
	const char* what() {
	   return "Unable to allocate memory for stack!\n";
	}
};

class StackOverflowException: public std::exception {
	const char * what() {
	    return "Stack is full !\n";
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
		for(int i=top;i  > -1;i--){
			
			std::cout << base[i] << ",";
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
	return i == '*' || i == '/' || i == '^' || i == '-' || i == '+' || i == '(' || i == ')';
}

typedef long double float32_t; 

float32_t EvalStack(unsigned char opr, Stack<float32_t> *stack){
	auto op1 = stack->Pop();
	auto op2 = stack->Pop();
	
	int64_t result;
	
	switch(opr){
		case '+':
			result = op1 + op2;
			std::cout <<op1<<'+'<<op2<<'='<<result<<'\n';
			break;
		case '-':
			result = op2 - op1;
			break;
		case '/':
			result = op2/op1;
			break;
		case '*':
			
			result = op1 * op2;
			std::cout <<op1<<'*'<<op2<<'='<<result<<'\n';
			break;
		case '^':
			result = pow(op2 ,op1);
			break;
			
	}
	return result;
}
float32_t EvalPostfix(int64_t* postfix, size_t len){
	auto stack = std::unique_ptr<Stack<float32_t>>(new ArrayStack<float32_t>());
	
	for(size_t i=0;i<len;i++){
		if(IsOperation(postfix[i])){
			auto result = EvalStack(postfix[i], stack.get());
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

float32_t EvalPrefix(int64_t *prefix, size_t len){
	auto stack = std::unique_ptr<Stack<float32_t>>(new PointerStack<float32_t>());
	
	for(size_t i=len;i > 0;i --){
		
		if(IsOperation(prefix[i-1])){
			auto result = EvalStack(prefix[i-1], stack.get());
			stack->Push(result);
		}
		else{
			stack->Push(prefix[i-1]);
		}
	}
	
	return stack->Pop();
	
	
}


uint8_t PreInValue(uint8_t opr){
	uint8_t pres[255];
	pres['+'] = 2;
	pres['-'] = 2;
	
	pres['*'] = 4;
	pres['/'] = 4;
	
	pres['^'] = 5;
	
	pres['('] = 0;
	pres[')'] = 1;
	return pres[opr];
}

uint8_t PreOutValue(uint8_t opr){
	uint8_t pres[255];
	pres['+'] = 1;
	pres['-'] = 1;
	
	pres['*'] = 3;
	pres['/'] = 3;
	
	pres['^'] = 6;
	
	pres['('] = 7;
	pres[')'] = 0;
	return pres[opr];
}

int64_t* InfixToPostfix(int64_t* infix, size_t len){
	/*
	
	*/
	auto return_value = new int64_t[len];
	auto stack = std::unique_ptr<Stack<int64_t>>(new ArrayStack<int64_t>);
	size_t out_len=0;
	
	for(size_t i=0;i<len;i++){
		if(IsOperation(infix[i])){
			std::cout << "opr '" << (char)infix[i] << "' \n";
			if(infix[i] == '('){
				stack->Push('(');
				stack->Print();
			}
			else if(infix[i] == ')'){
				while( !stack->IsEmpty() && stack->Peep()  != '('){
					return_value[out_len++] = stack->Pop();
				} 
				if(stack->Peep() == '(')
				    stack->Pop();
			}
			else{
				while(!stack->IsEmpty() && PreInValue( stack->Peep()) >= PreOutValue(infix[i]) ){
					std::cout << "Popping " << infix[i] << " >   " << stack->Peep() <<'\n';
					uint8_t opr = stack->Pop();
					return_value[out_len++] = opr;
				}
				
				stack->Push(infix[i]);
			}
		}
		else{
			std::cout << "Num " << infix[i] << '\n';
			return_value[out_len++] = infix[i];
		}
	}
	while(!stack->IsEmpty()){
		return_value[out_len++] = stack->Pop();
 	}
	
	return return_value;
} 

size_t CountBraces(int64_t *s, size_t len){
	size_t return_value = 0;
	
	for(size_t i=0;i<len;i++){
		if(s[i] == '(' || s[i] == ')') return_value ++;
	}
	
	return return_value;
}

float32_t EvalInfix(int64_t *infix,size_t len){
     auto *postfix = InfixToPostfix(infix, len);	
     std::cout << "Postfix: ";
     for(size_t i=0;i<len - CountBraces(infix, len);i++)
        if(postfix[i] > 255)
         std::cout << postfix[i] << " ";
        else std::cout << (char)postfix[i] << " ";
     std::cout <<'\n';
     return EvalPostfix(postfix, len-CountBraces(infix, len));
}

int64_t FromString(std::string s){
	std::stringstream ss;
	ss << s;
	int64_t return_value;
	ss >> return_value;
	return return_value;
}
bool IsNumChar(char s){
	return s>= '0' && s <='9'; 
}

int64_t* SplitStringToInt64(std::string s, size_t &len){
	//std::cout << "Given string length: " <<s.size() << '\n';
	int64_t *return_value = new int64_t[s.size()];
	std::string current_number = "";
	size_t j = 0;
    for(size_t i =0;i<s.size();i++){
    	if(s[i] == ' ') continue;
    	if(IsNumChar(s[i])){
    		current_number += s[i];
    //		std::cout << "Current num "<<current_number <<'\n';
		}
    	else{
    		if(!IsOperation(s[i])) throw std::logic_error("Erorr non operation given!");
    		return_value[j++] = FromString(current_number);
    		current_number = "";
    		return_value[j++] = s[i];
		}
    	
//    	if(){
//    		return_value[j] = s[i];
//    		j++;
//		}
		   
	}
	if(current_number.size()){
		return_value[j++] = FromString(current_number);
	}
	len = j;
	return return_value;
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
//   int64_t postfix[] = {10, 1, 2, '*', '+'};
//   cout << "Eval 1*2 + 10: " << EvalPostfix(postfix, 5) <<'\n';
//   int64_t prefix[] = {'+', '*', 1, 2, 330};
//   cout << "Eval 1*2 + 330:" << EvalPrefix(prefix, 5) << '\n';

//     int64_t infix[] = {60, '*', '(', 100, '-', 2, '^', 5, ')', '+', 2 };
//	cout <<"\n\n\n\n 60 * (100 - 2 ^ 5) + 2 = " << EvalInfix(infix, 11) <<'\n';
//   string s;
//   cout << "Input infix expression to evalutate: ";
//    getline()
    while(true){
    	system("cls");
    	cout << "Please Input an expression to evaluate: ";
    	string expr;
    	getline(cin, expr);
    	size_t split_len = 0;
    	auto split = SplitStringToInt64(expr, split_len);
//    	for(auto i=0;i<split_len;i++)
//    	   cout << "i " << i << " " << split[i] << endl;
    	cout << "\nThe result is: " << EvalInfix(split, split_len)<<'\n'; 
    	
    	system("pause");
	}
    return 0;
    
   
}
