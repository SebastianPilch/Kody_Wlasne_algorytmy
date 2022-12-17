#ifndef save_loadcpp
#define save_loadcpp
#include <fstream>
#include <iostream>
#include "LinkedList.hpp"
#include "save_load.hpp"
using namespace std;

LinkedList load_data_from_file(int size,string file){
    LinkedList matrix(size);
    for(int i = 0; i<size ;i++){
        matrix.add((new float[size+1]));}
    ifstream file_matrix;
    file_matrix.open(file);
    float data;
    for(int i = 0; i < size;i++){
        for(int j = 0; j <size + 1;j++){
            file_matrix >> data;
            matrix[i][j] = data;
        }
    }
    return matrix;
}

void save_result(LinkedList &mat, float* result,string file){

    ofstream outdata;
    outdata.open(file);
    float* vector = new float[mat.size_rows];
    if( !outdata.is_open() ){cerr << "Error: file could not be opened" << endl;
        exit(1);
    }
    outdata << "Macierz:" << endl << "[";
    for(int i=0 ;i < mat.size_rows ;i++){
        for(int j=0 ;j < mat.size_cols ;j++){
            if(j == mat.size_rows){vector[i] = mat[i][mat.size_rows];}
            else{outdata << mat[i][j] << " ";}
        }
        if(i < mat.size_rows-1){outdata << endl;}
    }
    outdata << "]" << endl;
    outdata << "Wektor zmiennych:" << endl << "[";
    for(int i=0 ;i < mat.size_rows ;i++){outdata << vector[i] << " " ;}
    outdata << "]" << endl << "Rozwiązanie:"<<endl << "[";
    for(int i=0 ;i < mat.size_rows ;i++){outdata << result[i] << " " ;}
    outdata << "]" << endl;
    outdata.close();

}

LinkedList load_data_from_console(int size) {
    LinkedList matrix(size);
    for(int i = 0; i<size ;i++) {matrix.add(new float[size + 1]);}
    for (int i = 0; i < size; i++) {
        float data;
        for (int j = 0; j < size; j++) {
            cout << "wprowadz dana z wiersza " << i + 1 << " i kolumny " << j + 1<<"\n";
            cin >> data;
            matrix[i][j] = data;
        }
        cout << "wprowadz dana z wektora wyrazow wolnych z wiersza " << i + 1<<"\n";
        cin >> data;
        matrix[i][size] = data;
    }
    return matrix;
}


#endif