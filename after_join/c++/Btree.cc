#include <iostream>
#include <stack>
#include <queue>
#include <memory>

constexpr size_t BTREE_SIZE = 1000; //no time to make resizes make latter

template<class T>
class Nullable{
T data;
public:
	void SetData(T d){
		data = d;
		has_data = true;
	}
	T GetData() const{
	   return data;
	}
	bool has_data = false;
};

template<class T>
struct TwoNode{
	T data;
	TwoNode *left,right;
};

template<class T, class IT>
class BTree{
	//IT is iterative type
	public:
		virtual void InorderRe(IT t) = 0;
		virtual void PostorderRe(IT t) = 0;
		virtual void PreorderRe(IT t) = 0;
		
		virtual void Inorder() = 0;
		virtual void Postorder() = 0;
		virtual void Preorder() = 0;
		virtual void LevelOrder() = 0;
		virtual void Insert(T data) = 0;
		virtual T sum(IT n) = 0;
		virtual T max(IT n) = 0;
		virtual T min(IT n) = 0;
		virtual int count(IT n) = 0;
};

template<class T>
class ArrayBTree: public BTree<T, int>{
  T *base;
  	//since the index begins with 0
		//need i+1
  size_t current_index = -1;
  	static inline size_t ParentIndex(size_t i){
			return (i-1)/2;
	}
	static inline size_t LeftIndex(size_t i){
		return i * 2 + 1;
	}
	static inline size_t RightIndex(size_t i)
	{
		return i * 2 + 2;
	}
	bool IsIn(int i){
	//	std::cout << "Checking " <<i << '\n';
		return i <= current_index;
	}
public:
//////////////////////////////////////////////////////////////////


	static inline void zigzag(T* heap, int len){
		using namespace std;
		auto IsIn = [len](int n){
		   return n < len;
	    };
	    auto LeftIndex = [](int i){
	    	return i * 2 + 1;
		};
		auto RightIndex = [](int i){
			return i*2 + 2;
		};
		auto ParentIndex = [](int i){
			return (i-1)/2;
		};
	    stack<int> s1;
		stack<int> s2;
		s1.push(0);
		
		while(!s1.empty() || !s2.empty()){
		
		   ///////////////////////////////////////////////////
		   	while(!s1.empty()){
				auto t = s1.top();
				cout << heap[t] << ", ";
		     	s1.pop();
				if(IsIn(LeftIndex(t))){
					s2.push(LeftIndex(t));
				}
				if(IsIn(RightIndex(t))){
					s2.push(RightIndex(t));
				}
			}
			
			while(!s2.empty()){
				auto t = s2.top();
				cout << heap[t] << ", ";
		     	s2.pop();
		     	if(IsIn(RightIndex(t))){
					s1.push(RightIndex(t));
				}
				if(IsIn(LeftIndex(t))){
					s1.push(LeftIndex(t));
				}
			
			}

		   ////////////////////////////////////////////////////
		}	
	}



///////////////////////////////////////////////////////////////
	static inline bool IsMaxHeap(T *heap, int len){
		auto IsIn = [len](int n){
		   return n < len;
	    };
	    auto LeftIndex = [](int i){
	    	return i * 2 + 1;
		};
		auto RightIndex = [](int i){
			return i*2 + 2;
		};
		auto ParentIndex = [](int i){
			return (i-1)/2;
		};
		std::stack<int> indexes;
		indexes.push(0); //push root node
		while(!indexes.empty()){
			auto t = indexes.top();
			indexes.pop();
			int l = LeftIndex(t);
			int r = RightIndex(t);
			if(IsIn(l)){
				std::cout << "Checking " << heap[l] << '\n';
				if(heap[l] > heap[t]){
					std::cout << "L1";
				 return false;
			    }
				indexes.push(l);
			}
			else {
					std::cout << "L1=>" << l << " " << heap[l] << '\n';
				return true;
			}
			if(IsIn(r)){
				std::cout << "Checking " << heap[r] << '\n';
				if(heap[r] > heap[t]){
						std::cout << "L1";
						return false;
				} 
				indexes.push(r);
			}
			else{
					std::cout << "La1";
				return true;
			}
		}
		return true;
		
		
	}
	    ArrayBTree(){
	    	base = new T[BTREE_SIZE];
		}
	    
	    virtual T sum(int n){
	    			 if(!IsIn(n)) return 0;
	    			 return base[n] + sum(LeftIndex(n)) + sum(RightIndex(n));
		}
		virtual T max(int n){
			 if(!IsIn(n)) return -10000000;
			int max = base[n];
			if(max < base[LeftIndex(n)]){
				max = base[LeftIndex(n)];
				
			}
			if(max < base[RightIndex(n)]){
				max = base[RightIndex(n)];
				
			}
			return max;
		}
		virtual T min(int n){
			if(!IsIn(n)) return 10000000;
			int min = base[n];
			if(min> base[LeftIndex(n)]){
				min = base[LeftIndex(n)];
				
			}
			if(min> base[RightIndex(n)]){
				min = base[RightIndex(n)];
				
			}
			return min;
		}
		int count(int n){
			if(!IsIn(n)) return 0;
			else return 1 + count(LeftIndex(n)) + count(RightIndex(n));
		}
	    void InorderRe(int t=0){
	       if(!IsIn(t)) return;
	   	   InorderRe(LeftIndex(t));
	   	   std::cout << base[t] << ", ";
	   	   InorderRe(RightIndex(t));
	    }
		virtual void PostorderRe(int t=0){
		   if(!IsIn(t)) return;
	   	   PostorderRe(LeftIndex(t));
	   	   PostorderRe(RightIndex(t));
	   	   std::cout << base[t] << ", ";
		}
		virtual void PreorderRe(int t=0){
		   if(!IsIn(t)) return;
		   std::cout << base[t] << ", ";
	   	   PreorderRe(LeftIndex(t));
	   	   PreorderRe(RightIndex(t));
		}
		
		
		virtual void Inorder(){
//			size_t c = 0;
//		    using namespace std;
//		    std::stack<int> next_index;
//		   
//		    while(IsIn(c)){
//		    	next_index.push(c);
//		    	c = LeftIndex(c);
//			}
//			while(!next_index.empty()){
//				//GOING BACK
//				int l = next_index.top();
//				next_index.pop();
//				cout << base[l] << ", ";
//				int r = RightIndex(l);
//				if(IsIn(r))
//                {
//                //	cout << base[r] << ", ";
//                	auto tmp = LeftIndex(r);
//                	next_index.push(r);
//                	while(IsIn(tmp)){
//                		next_index.push(tmp);
//                		tmp = LeftIndex(tmp);
//					}
//				
//				}
//			
//			}
//			cout <<'\n';
//    H, D, I, B, J, E, K, A, F, C, G,

            using namespace std;
            stack<int> next_index;
            int c= 0 ;
            while(IsIn(c)){
            	next_index.push(c);
            	c=  LeftIndex(c);
			}
            while(!next_index.empty()){
            	int l = next_index.top();
            	next_index.pop();
            	cout << base[l] << ", ";
            	
            	int r = RightIndex(l);
            	if(IsIn(r)){
            		next_index.push(r);
            		int rl = LeftIndex(r);
            		while(IsIn(rl)){
            			next_index.push(rl);
            			rl = LeftIndex(rl);
					}
				}
			}
			cout << '\n';
            
		}
		virtual void Postorder(){
//			std::stack<int> next_index;
//			std::stack<int> ps;
//		    
//			int c = 0;
//			while(IsIn(c)){
//				next_index.push(c);
//			//	if(IsIn(RightIndex(c))) next_index.push(RightIndex(c));
//				c = LeftIndex(c);
//			}
//		
//			while(!next_index.empty()){
//				int l = next_index.top(); //This is def a root too
//				next_index.pop();
//		        int r = RightIndex(l);
//		        if(IsIn(r)){
//		        	if(ps.empty() || ps.top() != l){
//		               ps.push(l);
//		               next_index.push(l);
//		               next_index.push(r);
//		               int ll = LeftIndex(r);
//		               while(IsIn(ll)){
//		               	  next_index.push(ll);
//		               	  ll = LeftIndex(ll);
//					   }
//					}
//					else{
//						ps.pop();
//						std::cout << base[l] << ", ";
//					}
//				}
//				else{
//					std::cout << base[l] << ", ";
//				}
//				
//			}
//			std::cout << '\n';
			using namespace std;
			stack<int> next_index, ps;
			int c = 0;
			while(IsIn(c)){
				next_index.push(c);
				c= LeftIndex(c);
			}
			while(!next_index.empty()){
				int lr = next_index.top(); next_index.pop();
			    
			    int lr_r = RightIndex(lr);
			    if(IsIn(lr_r)){
			    	if(ps.empty() ||  ps.top() != lr){
			    		ps.push(lr);
			    		next_index.push(lr);
			    	    next_index.push(lr_r);
			    		int lr_r_l = LeftIndex(lr_r);
			    		while(IsIn(lr_r_l)){
			    			next_index.push(lr_r_l);
			    			lr_r_l = LeftIndex(lr_r_l);
						}
					}
					else{
						ps.pop();
						cout << base[lr] << ", ";
					}
				}
				else{
					cout << base[lr] << ", ";
				}
				
			}
		}
	    virtual void Preorder(){
//	    	std::stack<int> s;
//	    	int c= 0 ;
//	    	while(IsIn(c)){
//	    		std::cout << base[c] << ", ";
//	    		int r = RightIndex(c);
//	    		if(IsIn(r)) s.push(r);
//	    		c = LeftIndex(c);
//			}
//			while(!s.empty()){
//				///std::cout << "DDD";
//				int r = s.top(); //Help someone's R
//				s.pop();
//				std::cout << base[r] << ", ";
//				int l = LeftIndex(r);
//				while(IsIn(l)){
//					std::cout << base[l] << ", ";
//					if(IsIn(RightIndex(l))){
//						s.push(RightIndex(l));
//					}
//					l = LeftIndex(l);
//				}
//			}
            using namespace std;
            stack<int> next_index;
            int c= 0;
            while(IsIn(c)){
            	cout << base[c] << ", ";
            
            	int r = RightIndex(c);
            	if(IsIn(r)){
            		next_index.push(r);
				}
				c = LeftIndex(c);
			}
            while(!next_index.empty()){
            	int r = next_index.top();
            	next_index.pop();
             	cout << base[r] << ", ";
            //	int l = LeftIndex(r);
            	while(IsIn(r)){
            		cout << base[r] << ", ";
            		int rr = RightIndex(r);
            		if(IsIn(rr))
            		   next_index.push(rr);
                    r = LeftIndex(r);
				}
            	
            	
			}
            
	    	
		}
		virtual void LevelOrder(){
			std::queue<int> q;
			q.push(0);
			
			while(!q.empty()){
				auto t = q.front();
				q.pop();
				std::cout << base[t] << ", ";
				int l = LeftIndex(t);
				int r = RightIndex(t);
				if(IsIn(l)){
					q.push(l);
				}
				if(IsIn(r)){
					q.push(r);
				}
				
			}
		}
		virtual void Insert(T data){
			base[++current_index] = data;
		}
};

int main(){
	using namespace std;
	
	ArrayBTree<char> t;
	int h[] = {10, 5, 7, 1, 2, -1000};
	 ArrayBTree<int>::zigzag(h, 6);
//    for(char a = 'A'; a<='K';a++){
//    	t.Insert(a);
//	}
//	cout << "\nPreorder: "; t.Preorder();
//	cout << "\nInorder: "; t.Inorder();
//    cout << "\nPostorder: "; t.Postorder();
//    cout <<"\nRecursive:\n";
//    
//	cout << "\nPreorder: "; t.PreorderRe();
//	cout << "\nInorder: "; t.InorderRe();
//    cout << "\nPostorder: "; t.PostorderRe();
//    
//    cout << "\nLevelOrder: "; t.LevelOrder();
//    
//    ArrayBTree<int> x;
//    for(int i=0;i<3;i++){
//    	x.Insert(i);
//	}
//	cout << "\nsum: "<<x.sum(0);
//	cout << "\nmax: " <<x.max(0);
//	cout << "\nmin: " << x.min(0);

}

