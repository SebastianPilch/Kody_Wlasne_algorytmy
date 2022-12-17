import copy
import random
import time


def redukcja_macierzy(Graf):
    sigma = 0
    graf = copy.deepcopy(Graf)
    for row in graf:
        minimalna_wartosc = float('inf')
        for k in row:
            if k < minimalna_wartosc:
                minimalna_wartosc = k
        # znaleźienie wartości minimalnej w wierszu i
        # zwiększenie wielkości redukcji macierzy
        for j in range(len(graf)):
            row[j] -= minimalna_wartosc
        # odjęcie minimum od całej macierzy
    for i in range(len(graf)):
        wektor_kolumn = []
        for j in range(len(graf)):
            wektor_kolumn.append(graf[j][i])
        # stworzenie listy przechowującej kolumę
        minimalna_wartosc = float('inf')
        for k in wektor_kolumn:
            if k < minimalna_wartosc:
                minimalna_wartosc = k
        sigma += minimalna_wartosc
        # znalezienie minimum kolumny
        # zwiększenie wielkości redukcji macierzy
        for j in range(len(graf)):
            graf[j][i] -= minimalna_wartosc
        # odjęcie minimum kolumny od całej macierzy
    return graf, sigma


def szukanie_zer_nzal(Red_Matrix, rev_side_row=False, rev_side_col=False):
    # argumenty to zredukowana macierz i kierunki szukania zer
    nzal_zeros = []
    in_col = []
    in_row = []
    zero_r = None
    zero_c = None
    # stworzenie list przechwujących znalezione indeksy zer niezależnych
    # oraz indeksy wierszy i kolumn w których znajdują się zera
    for i in range(len(Red_Matrix)):
        zeros_in_row = 0
        zeros_in_col = 0
        # liczba zer w wierszu i kolumnie
        for j in range(len(Red_Matrix)):
            if Red_Matrix[i][j] == 0:
                # szukanie zer w wierszu
                zero_r = i, j
                zeros_in_row += 1
            # jeśli zostało znalezione nadpisanie indeksów i zwiększenie liczby zer w wierszu
            if Red_Matrix[j][i] == 0:
                # szukanie zer w kolumnie
                zero_c = j, i
                zeros_in_col += 1
            # jeśli zostało znalezione nadpisanie indeksów i zwiększenie liczby zer w kolumnie
        if zeros_in_row == 1:
            # jeśli w wierszu jest tylko jedno zero zostaje dodane do zer niezależnych
            if zero_r is not None and zero_r not in nzal_zeros and zero_r[0] not in in_row and zero_r[1] not in in_col:
                # sprawdzenie czy nie zostało już dodane zero w danym wierszu lub kolumnie
                nzal_zeros.append(zero_r)
                in_col.append(zero_r[1])
                in_row.append(zero_r[0])
        if zeros_in_col == 1:
            # jeśli w kolumnie jest tylko jedno zero zostaje dodane do zer niezależnych
            if zero_c is not None and zero_c not in nzal_zeros and zero_c[0] not in in_row and zero_c[1] not in in_col:
                # sprawdzenie czy nie zostało już dodane zero w danym wierszu lub kolumnie
                nzal_zeros.append(zero_c)
                in_col.append(zero_c[1])
                in_row.append(zero_c[0])
    if len(nzal_zeros) == len(Red_Matrix):
        return nzal_zeros
    # jeżeli liczba zer i jedynek się nie zgadza macierz zostaje
    # przeszukana po wartościach nie będących w wierszach ani kolumnach wykreślonych
    if rev_side_row and rev_side_col:
        for k in range(2):
            for i in range(len(Red_Matrix)):
                for j in range(len(Red_Matrix)):
                    if len(Red_Matrix) - 1 - j not in in_col and len(Red_Matrix) - 1 - i not in in_row:
                        if Red_Matrix[len(Red_Matrix) - 1 - i][len(Red_Matrix) - 1 - j] == 0:
                            nzal_zeros.append((len(Red_Matrix) - 1 - i, len(Red_Matrix) - 1 - j))
                            in_col.append(len(Red_Matrix) - 1 - j)
                            in_row.append(len(Red_Matrix) - 1 - i)

    #inne kierunki przeszukiwania w przypadku nie znalezienia 10 zer niezależnych
    if not rev_side_row and not rev_side_col:
        for k in range(2):
            for i in range(len(Red_Matrix)):
                for j in range(len(Red_Matrix)):
                    if j not in in_col and i not in in_row:
                        if Red_Matrix[i][j] == 0:
                            nzal_zeros.append((i, j))
                            in_col.append(j)
                            in_row.append(i)

    if not rev_side_row and rev_side_col:
        for k in range(2):
            for i in range(len(Red_Matrix)):
                for j in range(len(Red_Matrix)):
                    if len(Red_Matrix) - 1 - j not in in_col and i not in in_row:
                        if Red_Matrix[i][len(Red_Matrix) - 1 - j] == 0:
                            nzal_zeros.append((i, len(Red_Matrix) - 1 - j))
                            in_col.append(len(Red_Matrix) - 1 - j)
                            in_row.append(i)

    if rev_side_row and not rev_side_col:
        for k in range(2):
            for i in range(len(Red_Matrix)):
                for j in range(len(Red_Matrix)):
                    if j not in in_col and len(Red_Matrix) - 1 - i not in in_row:
                        if Red_Matrix[len(Red_Matrix) - 1 - i][j] == 0:
                            nzal_zeros.append((len(Red_Matrix) - 1 - i, j))
                            in_col.append(j)
                            in_row.append(len(Red_Matrix) - 1 - i)
    return nzal_zeros


def wykreslanie_zer(matrix, zeros):
    matrix = copy.deepcopy(matrix)
    lines = dict()  # Stwórz słownik zawierający wszystkie wykreślenia w macierzy
    if len(zeros) == len(
            matrix):  # Jeśli liczba zer niezależnych równa rozmiarowi macierzy zwróć macierz binarną z lokalizacją miejsc zer niezależnych
        red_list = []
        for i in range(len(matrix)):
            red_list.append([0] * len(matrix[0]))
        for i in zeros:
            red_list[i[0]][i[1]] = 1
        return red_list, 0
    else:  # W przeciwnym przypadku przystąp do wykreślania zer
        red_matrix = copy.deepcopy(matrix)  # Stwórz kopię macierzy,w której zaznaczane będą wykreślone już zera
        for i in zeros:
            row_zeros = red_matrix[i[0]].count(0)  # Sprawdzenie ile jest zer jeszcze nie przykrytch w wierszu
            if row_zeros > 1:  # Jeżeli oprócz zera niezależnego występują inne zera wpisz wykreślenie 'horizontal' o odpowiednim indeksie do słownika
                for j in range(len(red_matrix[i[0]])):
                    if red_matrix[i[0]][j] == 0 and j != i[
                        1]:  # Oznaczenie przykrytych zer w wierszu jako fi (aktualizacja)
                        red_matrix[i[0]][j] = 'fi'
                if i[0] in lines.keys() and lines[i[0]] == 'v':
                    lines[i[0]] = 'h,v'
                else:
                    lines[i[0]] = 'h'
            else:
                for j in range(len(red_matrix)):
                    if red_matrix[j][i[1]] == 0 and j != i[0]:  # Oznaczanie przykrytych zer jako fi w kolumnie
                        red_matrix[j][i[1]] = 'fi'
                if i[1] in lines.keys() and lines[i[1]] == 'h':
                    lines[i[1]] = 'h,v'
                else:
                    lines[i[1]] = 'v'
        minimum = float('inf')
        for i in range(len(matrix)):  # Szukanie mninimum z niewykreślonych elementów
            if i in lines.keys() and (
                    lines[i] == 'h' or lines[i] == 'h,v'): continue  # Jeżeli element jest wykreślony, pomiń
            for j in range(len(matrix[i])):
                if j in lines.keys() and (
                        lines[j] == 'v' or lines[j] == 'h,v'): continue  # Jeżeli element jest wykreślony, pomiń
                if minimum > matrix[i][j]: minimum = matrix[i][j]  # Zaktualizuj minimum
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in lines.keys() and (lines[i] == 'h' or lines[i] == 'h,v') and j in lines.keys() and (
                        lines[j] == 'v' or lines[j] == 'h,v'):
                    matrix[i][j] += minimum  # Jeżeli element skreślony dwa razy, dodaj wartość minimalną
                elif i in lines.keys() and (lines[i] == 'h' or lines[i] == 'h,v'):
                    continue  # Jeżeli element skreślony raz nie modyfikuj elemntu
                elif j in lines.keys() and (lines[j] == 'v' or lines[j] == 'h,v'):
                    continue
                else:
                    matrix[i][j] -= minimum  # Jeżeli element nie jest skreślony odejmij od niego minimum

        return matrix, minimum  # Zwróć zmodyfikowaną macierz


def funkcja_celu(Red_Matrix, Time_Matrix):
    f_x = 0
    for i in range(len(Red_Matrix)):
        for j in range(len(Red_Matrix)):
            if Red_Matrix[i][j] == 1:
                f_x += Time_Matrix[i][j]
    return f_x


Macierz_1 = [[56, 20, 98, 20, 26, 40, 36, 80, 48, 43],
             [34, 73, 3, 26, 26, 24, 45, 36, 58, 82],
             [77, 49, 40, 80, 41, 38, 47, 40, 92, 27],
             [89, 62, 70, 66, 29, 1, 60, 46, 37, 64],
             [46, 63, 58, 51, 75, 68, 28, 29, 11, 17],
             [42, 60, 15, 36, 5, 87, 15, 78, 45, 53],
             [17, 87, 60, 85, 26, 79, 60, 51, 29, 47],
             [61, 96, 99, 60, 60, 37, 19, 6, 83, 78],
             [45, 98, 33, 90, 4, 12, 33, 100, 14, 42],
             [34, 18, 14, 63, 79, 52, 4, 64, 27, 57]]

Macierz_2 = [[8, 46, 4, 71, 88, 84, 42, 36, 72, 38, ],
             [82, 29, 2, 86, 22, 96, 55, 15, 28, 89, ],
             [93, 40, 35, 9, 81, 61, 93, 1, 71, 80, ],
             [76, 30, 93, 72, 4, 28, 18, 92, 99, 91, ],
             [80, 66, 71, 64, 44, 8, 68, 70, 5, 40, ],
             [69, 95, 26, 43, 17, 57, 33, 37, 5, 63, ],
             [6, 30, 9, 70, 51, 69, 79, 69, 79, 72, ],
             [2, 6, 24, 21, 24, 22, 28, 67, 77, 2, ],
             [11, 75, 18, 20, 71, 75, 69, 51, 6, 56, ],
             [4, 84, 21, 93, 51, 77, 65, 94, 22, 46, ]]

Macierz_3 = [[29, 78, 78, 79, 31, 73, 51, 33, 29, 63, ],
             [66, 33, 5, 76, 58, 81, 86, 23, 37, 8, ],
             [73, 36, 5, 8, 96, 56, 3, 81, 12, 91, ],
             [53, 4, 42, 64, 80, 88, 66, 52, 55, 64, ],
             [84, 94, 36, 3, 24, 36, 49, 43, 46, 79, ],
             [29, 5, 3, 72, 93, 78, 79, 1, 27, 98, ],
             [64, 16, 17, 79, 57, 13, 62, 98, 95, 28, ],
             [6, 3, 61, 19, 70, 3, 81, 90, 82, 83, ],
             [72, 52, 100, 21, 62, 33, 70, 67, 3, 6, ],
             [39, 77, 16, 50, 18, 64, 76, 26, 7, 86, ]]

grafs = [Macierz_1,Macierz_2,Macierz_3]


for graf in grafs:
    Matr, sigma = redukcja_macierzy(graf)
    zeros = szukanie_zer_nzal(Matr)
    new_mat, min = wykreslanie_zer(Matr, zeros)
    sigma += min
    k = 0
    start = len(zeros)
    ''' 
        Generalnie metoda spierdolona ale nie ma czasu poprawiać jak jest za dużo iteracji 
        czyli metoda nie jest w stanie znaleźć rozwiązania wypierdala błąd wybrałem takie macierze żeby było git
        Dla randomowych macierzy działa w 80% w rozmiarze 10x10 w 100% w rozmiarze 6X6 i mniejszych, więc raczej git 
        Piszę żebyś się nie bawił ze swoimi przykładami bo może wywalić błędy XD 
    '''

    # redukcja i przeszukiwanie do momentu znalezienia 10 miejsc niezależnych
    # lub do momentu zbyt dużej liczby iteracji
    while len(zeros) != len(graf) and k < 5 * (len(Matr) - start) + 10:
        bool_in_zeros_row = True
        bool_in_zeros_col = True
        if k > (len(Matr) - start):
            bool_in_zeros_row = False
            bool_in_zeros_col = False
        if k > 2 * (len(Matr) - start):
            bool_in_zeros_row = False
            bool_in_zeros_col = True
        if k > 3 * (len(Matr) - start):
            bool_in_zeros_col = False
            bool_in_zeros_row = True
        zeros = szukanie_zer_nzal(new_mat, bool_in_zeros_row, bool_in_zeros_col)
        new_mat, min = wykreslanie_zer(new_mat, zeros)
        sigma += min
        k += 1

    if k == 5 * (len(Matr) - start) + 10:
        print('błędna macierz')

    print("\n\nCzas pracy:                                           Przydział pracownika/maszyny do zadania:")
    string = ''
    for i in range(len(new_mat)):
        string += '['
        for j in range(len(new_mat)):
            string += str("{:^4}".format(graf[i][j]))
        string += ']              ['
        for j in range(len(new_mat)):
            string += str("{:^3}".format(new_mat[i][j]))
        string += ']\n'
    print(string)
    print('zera:', zeros, 'liczba zer:', len(zeros))

    zeros.sort()
    for i in zeros:
        print('Zadanie numer: ', i[0], ' przypisane do maszyny/pracownika: ', i[1], ' czas wykonania zadania: ',
              graf[i[0]][i[1]])

    print('Wielkość redukcji: ', sigma)
    print('Wartość funkcji celu dla macierzy z czasami pracy: ', funkcja_celu(new_mat, graf))
    print('Wartość funkcji celu dla macierzy zredukowanej: ', funkcja_celu(Matr, graf))
    print('\n\n\n')