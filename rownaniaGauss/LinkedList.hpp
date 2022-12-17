#ifndef ROWNANIAGAUSS_LINKEDLIST_HPP
#define ROWNANIAGAUSS_LINKEDLIST_HPP
using namespace std;

class Element{
public:
    float* data_;
    Element* next_;
    Element(float* data) {data_ = data ,next_ = nullptr;}
    ~Element();
};
class LinkedList{
private:
    Element* head_;
public:
    LinkedList(int size) {size_rows = size,head_ = nullptr,size_cols = size+1;}
    void add(float* data);
    void print();
    float*& operator [] (const int i);
    int size_rows;
    int size_cols ;
    ~LinkedList();
};
#endif //ROWNANIAGAUSS_LINKEDLIST_HPP
