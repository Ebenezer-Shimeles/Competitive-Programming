#include <iostream>

constexpr size_t MAX_HEAP_SIZE = 100;


template<class T>
class MaxHeap{
	
	private:
		T* base;
		size_t size = 0;
		size_t capacity;
	public:
		void Print(){
			for(int i=0;i<size;i++){
				std::cout << base[i] <<",";
			}
			std::cout << '\n';
		}
		void init(size_t c = MAX_HEAP_SIZE){
			size = 0;
            capacity = c;
            base = new T[c];
		}
		int parent(int i){
			return (i-1)/2;
		}
		int left(int i){
			return 2 * i + 1;
		}
		int right(int i){
			return 2* i + 2;
		}
		void siftup(int i){
			if(i >= size || i <=  0 ) return;
			
			while(i > 0 && base[i] > base[parent(i)]){
				std::swap(base[i], base[parent(i)]);
				i = parent(i);
			}
			
		}
		void siftdown(int i){
			if(i < 0 || i >= size){
				return;
			}
			while(i<size/2){
				int r = right(i);
				int l = left(i);
				
				int max = l;
				if(base[r] > base[l]){
					max = r;
				}
				if(base[max] > base[i]){
					std::swap(base[max], base[i]);
					i = max;
				}
				else{
					break;
				}
				
				
			}
		}
		
		void insert(T data){
			base[size++] = data;
			if(size != 1){
				siftup(size-1);
			}
			
		}
		void removeMax(){
			
			if(size-1 != 0){
			  std::swap(base[0], base[--size]);
			  siftdown(0);
		    }
		}
		bool isEmpty(){
			return size == 0;
		}
		bool isFUll(){
			return size == capacity;
		}
		MaxHeap(){
			init();
		}
		void updateKey(T val, int pos){
			bool g =  val > base[pos];
			
			base[pos] = val;
			if(g){
				siftup(pos);
			}
			else siftdown(pos);
		}
		MaxHeap(T *arr, size_t len){
			capacity = len;
			base = new T[len];
			size = len;
			for(int i=0;i<len;i++){
				base[i] = arr[i];
			}
			heapify();
		}
		void heapify(){
			//we sift down every node that is an internal node
			for(int i=size/2-1;i>=0;i--){
				siftdown(i);
			}
		}
};


int main(){
	using namespace std;
	int to[] = { 1, 10, 10000, 2, 6, 6, 0, 4};
	auto m = MaxHeap<int>(to, 8);
	
	m.Print();

	
}
