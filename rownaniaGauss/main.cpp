#include <iostream>
#include "LinkedList.hpp"
#include "Gauss.hpp"
#include "save_load.hpp"
using  namespace std;

int main() {
    int option = 1;
    int size = 4;
    do{
        cout << "Podaj opcje odczytu danych: \n 0 - zakonczenie programu,\n 1 - dane z pliku,\n 2 - dane wprowadzane recznie\n " ;
        cin >> option;
        switch (option) {
            case 1:{
                cout << "Podaj rozmiar macierz: \n " ;
                cin >> size;
                LinkedList mat = load_data_from_file(size,"../Gauss.txt");
                float* result = Gauss_method(mat);
                save_result(mat,result,"../Rozwiazanie.txt");
                cout << "dane zapisane do pliku Rozwiazanie.txt\n";
                delete result;
            }
            break;
            case 2:{
                cout << "Podaj rozmiar macierz: \n " ;
                cin >> size;
                LinkedList mat = load_data_from_console(size);
                float* result = Gauss_method(mat);
                save_result(mat,result,"../Rozwiazanie.txt");
                cout << "dane zapisane do pliku Rozwiazanie.txt\n";
                delete result;
            }
            break;

        }

    }
    while(option != 0);

}
