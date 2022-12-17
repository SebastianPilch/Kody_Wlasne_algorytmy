from math import sqrt


def czp(number):
    res = []
    start = 2
    while start < sqrt(number):
        if number % start == 0:
            return czp(number // start) + czp(start)
        else:
            start += 1
    if not res:
        return [number]


def sito(number):
    result = [1 for i in range(number + 1)]
    result[0] = 0
    result[1] = 0
    akt = 2
    while akt < sqrt(number):
        if result[akt] == 1:
            for i in range(2, int(number / akt + 1)):
                # nie powinno być pierwiastka bo ogranicza przedział z
                # którego usuwamy wielokrotności, czyli na przykład dla pierwszzej dwójki
                # zamiast usunąć 15 wielokrotności występujących między 2 a 30 usuwają się tylko dwie pierwsza bo
                # int(sqrt(30)/3) = 3 co przekłada się na usunięcie 2 i niczego więcej
                # bo for wykona się tylko dla i=2
                result[i * akt] = 0
        akt += 1
    return result


print(czp(15))
print(czp(24))
res=sito(30)
for i in range(len(res)):
    if res[i] == 1:
        print(i)

