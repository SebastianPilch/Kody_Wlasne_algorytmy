import copy
import math


def string_compare(P, T, i, j):
    if i == 0:
        return j
    if j == 0:
        return i
    zamian = string_compare(P, T, i - 1, j - 1) + int(P[i] != T[j])
    wstawien = string_compare(P, T, i, j - 1) + 1
    usuniec = string_compare(P, T, i - 1, j) + 1

    lowest_cost = min(zamian, wstawien, usuniec)
    return lowest_cost



def print_matrix(Matrix):
    string = ''
    for i in range(len(Matrix)):
        string += '['
        for j in range(len(Matrix[0])):
            string += "{:^3}".format(str((Matrix[i][j])))
        string += ']'
        string += '\n'
    print(string)


# print(string_compare(P3, T3, len(P3) - 1, len(T3) - 1))


def string_compare_PD(P, T):
    D = [[i for i in range(len(T))]]
    for i in range(1, len(P)):
        D.append([i if j == 0 else 0 for j in range(len(T))])

    D_letters = [['X' if i == 0 else 'I' for i in range(len(T))]]
    for i in range(1, len(P)):
        D_letters.append(['D' if j == 0 else 'X' for j in range(len(T))])

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            zamian = D[i - 1][j - 1] + (P[i] != T[j])
            wstawien = D[i][j - 1] + 1
            usuniec = D[i - 1][j] + 1

            cost = min(zamian, wstawien, usuniec)
            D[i][j] = cost
            letter = 'X'
            if cost == zamian:
                if P[i] == T[j]:
                    letter = 'M'
                else:
                    letter = 'S'
            elif cost == wstawien:
                letter = 'I'
            else:
                letter = 'D'
            D_letters[i][j] = letter
    # print_matrix(D)
    # print_matrix(D_letters)
    return D[len(P) - 1][len(T) - 1], D_letters


def recreated_path(D_letters, i, j) -> str:
    recreated_ = ""

    temp = D_letters[-1][-1]

    while temp != 'X':
        if temp in ['M', 'S']:
            i -= 1
            j -= 1
            recreated_ += temp
        elif temp == 'D':
            i -= 1
            recreated_ += temp
        elif temp == 'I':
            j -= 1
            recreated_ += temp

        temp = D_letters[i][j]
    recreated_ = recreated_[::-1]
    return recreated_


def string_compare_PD_2(P, T):
    D = [[0 for i in range(len(T))]]
    for i in range(1, len(P)):
        D.append([i if j == 0 else 0 for j in range(len(T))])

    D_letters = [['X' if i == 0 else 'I' for i in range(len(T))]]
    for i in range(1, len(P)):
        D_letters.append(['D' if j == 0 else 'X' for j in range(len(T))])

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            zamian = D[i - 1][j - 1] + (P[i] != T[j])
            wstawien = D[i][j - 1] + 1
            usuniec = D[i - 1][j] + 1

            cost = min(zamian, wstawien, usuniec)
            D[i][j] = cost
            letter = 'X'
            if cost == zamian:
                if P[i] == T[j]:
                    letter = 'M'
                else:
                    letter = 'S'
            elif cost == wstawien:
                letter = 'I'
            else:
                letter = 'D'
            D_letters[i][j] = letter
    starting_point = []
    for i in range(1, len(T)):
        if D[-1][i] == min(D[-1][:]):
            starting_point.append(i)

    return D[len(P) - 1][len(T) - 1], D_letters, starting_point[0] - len(P) + 1


def string_compare_PD_3(P, T):
    D = [[i for i in range(len(T))]]
    for i in range(1, len(P)):
        D.append([i if j == 0 else 0 for j in range(len(T))])

    D_letters = [['X' if i == 0 else 'I' for i in range(len(T))]]
    for i in range(1, len(P)):
        D_letters.append(['D' if j == 0 else 'X' for j in range(len(T))])

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            if P[i] != T[j]:
                zamian = D[i - 1][j - 1] + float('inf')
            else:
                zamian = D[i - 1][j - 1]
            wstawien = D[i][j - 1] + 1
            usuniec = D[i - 1][j] + 1

            cost = min(zamian, wstawien, usuniec)
            D[i][j] = cost
            letter = 'X'
            if cost == zamian:
                if P[i] == T[j]:
                    letter = 'M'
                else:
                    letter = 'S'
            elif cost == wstawien:
                letter = 'I'
            else:
                letter = 'D'
            D_letters[i][j] = letter
    # print_matrix(D)
    # print_matrix(D_letters)
    return D[len(P) - 1][len(T) - 1], D_letters, D


def get_sequence(path, P):
    sequence = ""
    i = 1
    for letter in path:
        if letter == 'M':
            sequence += P[i]
            i += 1
        elif letter == 'D':
            i += 1
    return sequence


P2 = " kot"
T2 = " pies"

print(string_compare(P2, T2, len(P2) - 1, len(T2) - 1))


P3 = ' autobus'
T3 = ' autokar'
#
min_value, Letters_matrix = string_compare_PD(P3, T3)
print(min_value)
# print_matrix(Letters_matrix)

P4 = ' thou shalt not'
T4 = ' you should not'

min_value, parents = string_compare_PD(P4, T4)

print(recreated_path(parents, len(P4) - 1, len(T4) - 1))



P5 = 'ban'
T5 = 'mokeyssbanana'

min_value, par, st_pt = string_compare_PD_2(P5, T5)
print('ban: ', st_pt)

P6 = 'bin'
T6 = 'mokeyssbanana'

min_value, par, st_pt = string_compare_PD_2(P6, T6)
print('bin: ',st_pt)

P7 = ' democrat'
T7 = ' republican'

min_value, parents, tab = string_compare_PD_3(P7, T7)
path = recreated_path(parents, len(P7) - 1, len(T7) - 1)
print(get_sequence(path, P7))

T8 = ' 243517698'
sorted_T8 = sorted(T8)
P8 = " "
for n in sorted_T8[1:]:
    P8 += str(n)

min_value, parents, mat = string_compare_PD_3(P8, T8)
path = recreated_path(parents, len(P8)-1, len(T8)-1)
sequence = get_sequence(path, P8)
print(sequence)