#include <iostream>
#include <string>
using namespace std;

template<class T>
struct TreeNode{
	T index;
	TreeNode<T> *left, *right;
};

template<class T>
void search(TreeNode<T> * root, T data){
	if(!root) {
		cout << "Not Found!";
	}
	auto current = root;
	while(current){
		if(data > current->index){
			current = current->right;
		}
		else if(current->index == data){
            cout << "Found " << current->index <<'\n';
  			return;
		}
		else{
			current = current->left;
		}
	}
	cout << ":( Not found!";
}

template<class T>
void InsertBst(TreeNode<T> * &root, T value){
	auto newNode = new TreeNode<T>();
	newNode->index=  value;
	if(!root){
		cout << "Len 0 so adding "<<'\n';
		root = newNode;
		return;
	}
	auto current = root;
	
	while(current){
		cout << "current value " << current->index;
		if(value >= current->index){
			cout << "Greater ..\n";
			if(current->right){
				current = current->right;
			}
			else{
				current->right = newNode;
				cout << "inserted " << value <<endl;
				return;
			}
		}
		else{
			cout << "Lesser ..\n";
			if(current->left){
					current = current->left;
			}
			else{
				current->left = newNode;
					cout << "inserted " << value <<endl;
				return;
			}
		
		}
	}
	
}

struct Trunk
{
    Trunk *prev;
    string str;
    Trunk(Trunk *prev, string str)
    {
        this->prev = prev;
        this->str = str;
    }
};

void showTrunks(Trunk *p)
{
    if (p == nullptr) {
        return;
    }
    showTrunks(p->prev);
    cout<< p->str;
}
 

template<class T>
void printTree(TreeNode<T>* root, Trunk *prev=NULL, bool isLeft=false)
{
    if (root == nullptr) {
        return;
    }
    string prev_str = "    ";
    Trunk *trunk = new Trunk(prev, prev_str);
    printTree(root->right, trunk, true);
    if (!prev) {
        trunk->str = "———";
    }
    else if (isLeft)
    {
        trunk->str = ".———";
        prev_str = "   |";
    }
    else {
        trunk->str = "`———";
        prev->str = prev_str;
    }
 
    showTrunks(trunk);
    cout << " " << root->index << endl;
 
    if (prev) {
        prev->str = prev_str;
    }
    trunk->str = "   |";
 
    printTree(root->left, trunk, false);
}


template<class T>
TreeNode<T>* retLoop(TreeNode<T> * root){
   if(!root) return nullptr;
   auto t = retLoop(root->left);
   if(t) return t;
   return root;
   retLoop(root->right);
}

template<class T>
TreeNode<T>* findMax(TreeNode<T> *root){
	if(!root) return 0;
	auto current = root;
	while(current->right){
		current = current->right;
	}
	return current;	
}
template<class T>
TreeNode<T>* findMin(TreeNode<T> *root){
	auto current = root;
	while(current->left){
		current = current->left;
	}
	return current;
}

template<class T>
TreeNode<T> *del(TreeNode<T> *root, T index){
	if(root==nullptr) return nullptr;
    if(root->index==index){
    	//go the data
    	if(!root->left && !root->right){
    		delete root;
    		return nullptr;
		}
		else if(root->left && root->right){
			auto leftMax = findMin(root->Right);
			cout << "The left max:  " <<leftMax->index <<'\n';
			root->index = leftMax->index;
		    root->left= 	del(root->left, leftMax->index);
			return root;
		}
		else if(root->left){
			auto tmp = root->left;
			delete root;
		    return tmp;
		}
		else if(root->right)
		{
			auto tmp =  root->right;
			delete root;
			return tmp;
		
		}
	}	
	else if(root->index > index){
		root->right = del(root->right, index);
		return root;
	}
	else if(root->index < index){
		root->left = del(root->left, index);
		return root;
	}

}

int main(){
	TreeNode<int> *b = nullptr;
	for(int i=0;i<10;i++){
		cout <<i <<endl;
		InsertBst<int>(b, i);
	}
	for(int i=0;i>-10;i--){
		cout <<i <<endl;
		InsertBst<int>(b, i);
	}
    for(int i=20;i<40;i++){
    		InsertBst<int>(b, i);
	}
	del(b, 0);
	printTree(b);
	
	search(b, 4);
}
