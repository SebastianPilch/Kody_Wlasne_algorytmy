#ifndef Gausscpp
#define Gausscpp
#include <iostream>
#include "LinkedList.hpp"
#include "Gauss.hpp"
#include <cstdlib>

const float epsilon = 1e-10;

float* Gauss_method(LinkedList &matrix_ ){
    int size = matrix_.size_rows;
    LinkedList copy_matrix(size);
    for(int i = 0; i < size;i++) {
        copy_matrix.add((new float[size+1]));
        for (int j = 0; j < size+1; j++) {
            copy_matrix[i][j] = matrix_[i][j];
        }
    }
    int row = 1;
    for(int j = 0; j < size-1;j++) {
        for (int k = row; k < size; k++) {
            float ratio = copy_matrix[k][j] / copy_matrix[j][j];
            for (int i = row-1; i < size+1; i++) {
                copy_matrix[k][i] = copy_matrix[k][i] - copy_matrix[j][i]* ratio;
            }
        }
        row++;
    }
    float* result = new float[size];
    float* vector = new float[size];
    for(int i =0; i < size;i++){vector[i] = copy_matrix[i][size];}
    for(int j = size-1; j >= 0;j--) {
        float sum = 0;
        for (int k = j + 1; k < size; k++) {sum += copy_matrix[j][k] * result[k];}
        result[j] = (vector[j] - sum)/copy_matrix[j][j];
        if (abs(result[j]) < epsilon){result[j] = 0;}
    }
    return result;
}

#endif
