def find_q(points_list_, begin):
    q = None
    for i in range(len(points_list_)):
        if points_list_[i] != begin:
            q = points_list_[i]
            turn_list = []
            for j in range(len(points_list_)):
                if points_list_[j] != begin and i != j:
                    r = points_list_[j]
                    turn = (q[1] - begin[1]) * (r[0] - q[0]) - (r[1] - q[1]) * (q[0] - begin[0])
                    if turn > 0:
                        turn_list.append('R')
                    if turn < 0:
                        turn_list.append('L')
                    else:
                        turn_list.append('I')
            if 'I' not in turn_list and 'R' not in turn_list:
                break
    return q


def find_path(points_list, Kontrola_wspoliniowych = True):
    begin_point = None
    min_x = float('inf')
    min_y = float('inf')
    for i in range(len(points_list)):
        if points_list[i][0] < min_x:
            begin_point = points_list[i]
            min_x = points_list[i][0]
            min_y = points_list[i][1]
        elif points_list[i][0] == min_x and points_list[i][1] < min_y:
            begin_point = points_list[i]
            min_x = points_list[i][0]
            min_y = points_list[i][1]

    used_points = []
    p = begin_point
    q = find_q(points_list, begin_point)
    while len(used_points) == 0 or used_points[-1] != begin_point:
        for r in points_list:
            if r != q and r != p:
                turn = (q[1] - p[1]) * (r[0] - q[0]) - (r[1] - q[1]) * (q[0] - p[0])
                if turn > 0:
                    q = r
                if turn == 0 and Kontrola_wspoliniowych:
                    if p[0]**2+p[1]**2 > q[0]**2+q[1]**2 > r[0]**2+r[1]**2 or p[0]**2+p[1]**2 < q[0]**2+q[1]**2 < r[0]**2+r[1]**2:
                        q = r

        used_points.append(q)
        p = q
        q = find_q(points_list, p)
    return used_points


# points_1 = [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
# points_2 = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]
points_3 = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
# print(find_path(points_1))
# print(find_path(points_2))
print('Wersja bez sprawdzania punktów współliniowych:')
print(find_path(points_3,False))
print('Wersja ze sprawdzaniem punktów współliniowych: ')
print(find_path(points_3))