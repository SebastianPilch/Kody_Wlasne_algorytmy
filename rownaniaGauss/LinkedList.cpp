
#ifndef LinkedListcpp
#define LinkedListcpp
#include <iostream>
#include "LinkedList.hpp"
using namespace std;


void LinkedList::add(float* data) {
    Element* new_elem = new Element(data);
    if (head_ == nullptr){head_ = new_elem;}
    else{
        Element* next_elem = head_;
        while(next_elem -> next_ != nullptr){
            next_elem = next_elem->next_;
        }
        next_elem->next_ = new_elem;
    };
}

void LinkedList::print() {
    if(head_ == nullptr){cout << "[]" << endl;}
    else{
        Element temp_elem = *head_;
        cout <<"\n[";
        for(int i =0;i<size_rows;i++){
            for(int j=0;j < size_cols; j++){cout << ' ' << temp_elem.data_[j];}
            if(i < size_rows-1){temp_elem = *temp_elem.next_;cout << endl;}
        }
        cout << "]" << endl;
    }
}

float*& LinkedList::operator[](const int i) {
    if(i==0){return head_->data_;}
    Element* next_elem = head_->next_;
    for (int j = 1; j < i ; j++) {
        next_elem = next_elem->next_;
    }
    return next_elem->data_;}

Element::~Element() {
    if(this -> next_ != nullptr){delete next_;}
}


LinkedList:: ~LinkedList() {
    if(this->head_ != nullptr){delete head_;}
}

#endif








