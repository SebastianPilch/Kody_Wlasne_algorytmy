#ifndef ROWNANIAGAUSS_SAVE_LOAD_HPP
#define ROWNANIAGAUSS_SAVE_LOAD_HPP
#include <fstream>
#include <iostream>
#include "LinkedList.hpp"

LinkedList load_data_from_file(int size,string file);
void save_result(LinkedList &mat, float* result,string file);
LinkedList load_data_from_console(int size);

#endif //ROWNANIAGAUSS_SAVE_LOAD_HPP
