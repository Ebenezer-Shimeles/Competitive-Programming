#include <iostream>
#include <string>
#include <exception>
#include <memory>

#include <cstdlib>
#include <cstring>


constexpr size_t DEFAULT_QUEUE_SIZE = 1;
using std::string;
class Printable{
	public:
		virtual void Print() const noexcept = 0;
};

class Stringable{
	public:
		virtual std::string ToString()  const noexcept = 0;
};

template<class T>
class Queue : public Stringable, public Printable{
	public:
		virtual void Enqueue(T data) = 0;
		virtual T Dequeue() = 0;
		virtual T Peek() = 0;
		virtual bool IsFull() const noexcept = 0;
		virtual bool IsEmpty() const noexcept =0;
		virtual void Create(size_t size) = 0;
		virtual size_t Size() const noexcept = 0;
		virtual void Resize(size_t by) = 0;
		
		virtual ~Queue(){
			std::cout << "Queue deleted! :(\n";
		}
};

template<class T>
class ArrayQueue: public Queue<T>{
	
private:
    T *base;
	size_t head;
	size_t tail;
	size_t size;
	size_t capacity;
public:
	   std::string ToString() const noexcept{
	   	    using namespace std;
	   	    string return_value = "";
	   	    
	   	    
	   	    return_value +=  "[";
	   	    if(size == 1){
	   	    	return_value += base[0];
			   }
	        for(size_t i=head;i!=(tail +1) % capacity;i=(i+1)%capacity){
	        	
	        	return_value += base[i];
				return_value += ",";
			}
			return_value += "]";
			return return_value;
	   }
	   void Print() const noexcept{
	       std::cout << this->ToString() << '\n';
	   }
	   ~ArrayQueue(){
	   	  std::cout << "Array Queue deleted! :(";
	   	  delete []base;
	   	  
	   }
	   ArrayQueue(size_t c = DEFAULT_QUEUE_SIZE){
	   	    capacity = c;
	   	    head = -1;
	   	    tail = -1;
	   	    size = 0;
	   	    Create(capacity);
	   }  
	
	   size_t Capacity() const noexcept{
	       return capacity;
	   }
	   size_t Size() const noexcept{
	     return size;
	   }
	   void Resize(size_t by){
	   	 
	   	  std::cout << "Resizing queue\n :) head= " << head << " tail= " << tail << " values: "<< this << '\n';
	      size_t new_size = capacity + by;
	      T *new_base = new (std::nothrow)T[new_size];
	      if(!new_base){
	      	 std::cout <<"Error cannot allocate memory for Queue!";
	      	 throw  ("Error cannot allocate memory for Queue!");
		  }
		  memset(new_base, 0, new_size);
		  int j = 0;
	      for(size_t i=head;i!=(tail+1)%capacity;i=(i+1)%capacity){
	      	std::cout << "Copying "<< base[i] <<'\n';
	      	new_base[j++] = base[i];
		  }
		  capacity = new_size;
		  head = 0;
		  
		  tail = j - 1;
		  delete[] base;
		  base = new_base;
		  std::cout << "\n\n\nAfter resize " << this <<'\n';
		  
		  
	      
	   }
	  
	   void Enqueue(T data){
	        if(IsFull())
			   Resize(1);	
			std::cout << "\nAdding " << data <<'\n';
			tail = (tail+1)%capacity;
			base[tail] = data;
			if(head == -1){
				head = tail;
			}
			size++;
			std::cout << "After add "<< this <<'\n';
			
	   }
		T Dequeue(){
			if(IsEmpty())
			   throw ("Error Queue is empty!");
			T data = base[tail];
			size --;
			return data;
		}
		T Peek(){
			if(IsEmpty())
			   throw ("Error Queue is empty!");
			return base[tail];
			
		}
		bool IsEmpty() const noexcept{
		    return size == 0;
		}
		bool IsFull() const noexcept{
			return size == capacity;
		}
		void Create(size_t size){
			base = new T[size];
			if(!base){
	      	 throw ("Error cannot allocate memory for Queue!");
		    }
		}
};
template<class T>
std::ostream& operator<<(std::ostream& s, Queue<T> q){
	return s << q.ToString();
}
template<class T>
std::ostream& operator<<(std::ostream& s, Queue<T> *q){
	return s << q->ToString();
}

template<class T>
struct OneNode{
	//Don't delete anything here...
	T data;
	OneNode *next = nullptr;
	OneNode(){
		
	}
	OneNode(T d){
	   data = d;	
	}
};

template<class T>
class PointerQueue: public Queue<T>{
	
private:
       	OneNode<T> *_head = nullptr;
       	OneNode<T> *_tail = nullptr;
       	size_t size = 0;
       	
public:
	     std::string ToString() const noexcept{
	     	std::string return_value = "";
	     	auto tmp = _head;
	     	while(tmp){
	     		return_value += tmp->data;
	     		return_value += ",";
	     		tmp = tmp->next;
			 }
	     	return return_value;
	     }
	     void   Print() const noexcept{
	     //	std::cout << this->ToString();
	     }
	     void Enqueue(T data){
	     	    
	     	 	auto new_tail = new (std::nothrow)OneNode<T>(data);
	     	 	if(!new_tail){
	     	 		std::cout << "Cannot create new tail!\n";
	     	 		throw "Cannot create new tail!\n";
				}
	     	 	if(IsEmpty()){
	     	 		std::cout << "Queue is empty!\n";
	     	 		_head = _tail = new_tail;
				}
				else{
					_tail->next= new_tail;
					_tail = new_tail;
				}
				size++;
				std::cout << "Added " << data <<" Size " << size<<'\n';
			
				
		 }
		 T Dequeue(){
		 	//This takes from the front ;0
		 	//std::logic_error is missing somehow so.... fix it latter
		 	if(IsEmpty())
		 	   throw ("Queue is empty");
		 	T data =  _head->data;
		 	_head = _head->next;
		 	size--;
		 	return data;
		 }
		 
		 T Peek(){
		 	// Again takes from the front
		 	if(IsEmpty())
		 	    throw "Queue is empty!";
		 	return _head->data;
		 }
		 bool IsFull() const noexcept {
		    return false;
		 }
		 
		 bool IsEmpty() const noexcept{
		 	return _head == nullptr;
		 }
		 void Create(size_t size){
		 	//no make sense :)
		 }
		 
		 size_t Size() const noexcept{
		 	return size;
		 }
		 void Resize(size_t by){
		 	//no make sense :)
		 }
		
		~PointerQueue(){
			
			
//			auto p = _head;
//			while(p){
//				auto tmp = p->next;
//				delete p;
//				p = tmp;
//				
//				
//			}
			std::cout << "PointerQueue deleted! :(\n";
		}
};

bool IsPalindrome(std::string s){
	auto q = std::unique_ptr<Queue<uint8_t>>(new PointerQueue<uint8_t>());
	size_t i = 0;
	for( ;i<s.size()/2;i++){
		q->Enqueue(s[i]);
	}
	if(s.size() % 2){
		i++;
	}
	size_t back = s.size() - 1;
	while(!q->IsEmpty()){
		if(q->Dequeue() != s[back]) return false;
		back--;
	}
	return true;
}

int main(){
	using namespace std;
//	auto q = shared_ptr<  Queue<char> >(  new PointerQueue<char>()  );
//    
//    for(int i='A';i<='Z';i++){
//    	q->Enqueue(i);
//    //	q->Dequeue();
//    //	q->Dequeue();
//		cout << q << '\n';
//	}
//	cout << "HEre";
    //q->Enqueue('A');
//    q->Enqueue('B');
//    q->Enqueue('C');
//    q->Enqueue('D');
//	q->Print();

   while(true){
   	system("cls");
   	string s;
   	cout << "Enter a string to check if palindrome: ";
   	getline(cin, s);
   	if(IsPalindrome(s)){
   		cout << "\nIt is a palindrome\n";
	}
	else{
	   	cout << "\nIt is not a palindrome!\n";
	}
	system("pause");
   }
   

	
}
