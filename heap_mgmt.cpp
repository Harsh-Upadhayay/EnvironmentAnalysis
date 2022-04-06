#include <iostream>
#include <bitset>
#include <vector>
#include <math.h>
#include <climits>
#include <map>

using namespace std;


struct dataBlock {
    void *data;
    int size, in_use;
    dataBlock* next;
    bool allocated;

    dataBlock(){
        data = next = NULL;
        size = in_use = 0;
        allocated = false;
    }
};

class dataAllocator{
    
    protected:    
    dataBlock *head;

    public:
    dataAllocator(){
        head = NULL;
    }

    virtual dataBlock* get_data(int size) = 0;

    void FREE(dataBlock *x){
        x->allocated = false;
        // coalesce();
    }

    // void coalesce();

    void print(){
        while(head){
            cout << *((int*)(head->data)) << " " << head->data << " " << head->size << " " <<head->allocated << "\n";
            head = head->next; 
        }
    }
    
};

class firstFit : public dataAllocator{

    public : 

    dataBlock* get_data(int size){
        dataBlock *newNode  = new dataBlock;
        newNode->data = malloc(size);
        newNode->size = size;
        newNode->allocated = true;

        if(!head){
            head = newNode;
        }
        else{
            dataBlock *ptr = head;
            while(ptr && ptr->next){
                if(!(ptr->allocated) && ptr->size >= size){
                    ptr->allocated = true;
                    free(newNode);
                    return ptr;
                }
                ptr = ptr->next;
            }
            if(!(ptr->allocated) && ptr->size >= size){
                    ptr->allocated = true;
                    free(newNode);
                    return ptr;
                }
            ptr->next = newNode;;
        }

        return newNode;
    }
    
};

class nextFit : public dataAllocator{
    
    dataBlock *curr;

    public: 
    dataBlock* get_data(int size){
        dataBlock *newNode  = new dataBlock;
        newNode->data = malloc(size);
        newNode->size = size;
        newNode->allocated = true;

        if(!head){
            head = curr = newNode;
        }
        else{
            dataBlock *ptr = curr;
            while(ptr && ptr->next){
                if(!(ptr->allocated) && ptr->size >= size){
                    ptr->allocated = true;
                    free(newNode);
                    return ptr;
                }
                ptr = ptr->next;
            }
            if(!(ptr->allocated) && ptr->size >= size){
                    ptr->allocated = true;
                    free(newNode);
                    return ptr;
                }
            ptr->next = newNode;;
        }

        return newNode;
    }
    
};

class bestFit : public dataAllocator{
    
    public: 
    dataBlock* get_data(int size){
        dataBlock *newNode  = new dataBlock;
        newNode->data = malloc(size);
        newNode->size = size;
        newNode->allocated = true;

        if(!head){
            head = newNode;
        }
        else{
            int minDiff = INT_MAX, pos =  -1, i = 0;
            dataBlock *ptr = head;
            while(ptr && ptr->next){
                if(!(ptr->allocated) && ptr->size >= size){
                    if(ptr->size - size < minDiff){
                        minDiff = ptr->size - size;
                        pos = i;
                    }
                }
                ++i;
                ptr = ptr->next;
            }
            if(!(ptr->allocated) && ptr->size >= size){
                if(ptr->size - size < minDiff){
                    minDiff = ptr->size - size;
                    pos = i;
                }
            }
            ++i;
            
            if(pos != -1){
                while(pos--)
                    ptr = ptr->next;
                ptr->allocated = true;
                return ptr;
            }
            
            ptr->next = newNode;
        }

        return newNode;
    }
    
};


int main(){
    firstFit allocator;
    dataBlock *y = allocator.get_data(2*sizeof(int));
    int *data = (int*)y->data;
    data[0] = 20;
    data[1] = 22;
    // allocator.print();
    
    y = allocator.get_data(5*sizeof(int));
    data = (int *)y->data;
    data[0] = 11;
    data[1] = 12;
    data[2] = 13;
    data[3] = 14;
    data[4] = 15;
    // allocator.print();
    // allocator.FREE(y);

    y = allocator.get_data(sizeof(int));
    data = (int*)y->data;
    data[0] = 1000;
    allocator.print();
    
    y = allocator.get_data(sizeof(int)*20);
    data = (int*)y->data;
    for(int i = 0; i < 20; i++)
        data[i] = 20*(i+2);
    allocator.print();
}
