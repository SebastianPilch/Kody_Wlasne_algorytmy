import time

def text_finding(S, W):
    found = []
    iter = 0
    for m in range(len(S)-len(W)+1):
        idx = 0
        iter += 1
        while S[m + idx] == W[idx] and idx < len(W)-1:
            # print(S[m+idx],' ',W[idx],' ', idx)
            idx += 1
            iter += 1
        if idx == len(W)-1 and S[m+idx] == W[idx]:
            found.append(m)
            iter += 1
    return found, iter


def hash(word,N):
    hw = 0
    for i in range(len(N)):  # N - to długość wzorca
        hw = (hw*256 + ord(word[i])) % 101
    if hw <0:
        hw += 101
    return hw
def Metoda_Rabina_Karpa(S, W):
    found = []
    iter = 0
    W_hash = hash(W,W)
    for m in range(len(S)-len(W)+1):
        iter += 1
        if W_hash == hash(S[m:m+len(W)],W):
            idx = 0
            while S[m + idx] == W[idx] and idx < len(W) - 1:
                idx += 1
                iter += 1
            if idx == len(W) - 1 and S[m + idx] == W[idx]:
                found.append(m)
                iter += 1
    return found, iter


def Metoda_Knutha_Morrisa_Pratta(S, W):
    m = 0
    i = 0
    iter = 0
    found = []
    nP = 0
    Tab = Tablica_met_KMP(W)
    while m < len(S):
        iter += 1
        if W[i] == S[m]:
            m += 1
            i += 1
            iter += 1
            if i == len(W):
                found.append(m - i)
                nP += 1
                i = Tab[i]
        else:
            i = Tab[i]
            if i < 0:
                m += 1
                i += 1
    return found, iter

def Tablica_met_KMP(W: str):
    pos = 1
    cnd = 0
    Tab = [0] * (len(W) + 1)
    Tab[0] = -1
    while pos < len(W):
        if W[pos] == W[cnd]:
            Tab[pos] = Tab[cnd]
        else:
            Tab[pos] = cnd
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = Tab[cnd]
        pos += 1
        cnd += 1
    Tab[pos] = cnd
    return Tab




with open("lotr.txt", encoding='utf-8') as f:
    text = f.readlines()
Search = ' '.join(text).lower()
Template = "time."
t_start = time.perf_counter()
found, iter = text_finding(Search,Template)
t_stop = time.perf_counter()
print('\n\nMetoda naiwna: ')
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
print('liczba porównań: ',iter)
print(found)
print(len(found))



t_start = time.perf_counter()
found , iter = Metoda_Rabina_Karpa(Search, Template)
t_stop = time.perf_counter()
print('\n\nMetoda Rabina_Karpa : ')
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
print('liczba porównań: ',iter)
print(found)
print(len(found))

t_start = time.perf_counter()
found , iter =Metoda_Knutha_Morrisa_Pratta(Search, Template)
t_stop = time.perf_counter()
print('\n\nMetoda Knutha_Morrisa_Pratta : ')
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
print('liczba porównań: ',iter)
print(found)
print(len(found))