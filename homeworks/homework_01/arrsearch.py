def find_indices(input_list, n):
    global first, second
    d = dict()
    k1 = []
    k2 = []
    c = 0
    if len(input_list) > 1:
        for position, value in enumerate(input_list):
            raznost = n - value
            if raznost in d.keys():
                if c != 2:
                    k1.append(d.get(raznost))
                    k2 = k1
                    k1 = []
                    k2.append(position)
                    d[raznost] = k2
                    c += 1
            else:
                d[raznost] = position

        for j, val in enumerate(input_list):
            s = d.get(val, -1)
            if j == s:
                continue
            else:
                if s != -1:
                    if isinstance(s, list):
                        first = s[0]
                        second = s[1]
                        break
                    else:
                        first = s
                        s = d.get(n - val, -1)
                        if isinstance(s, list):
                            second = s[0]
                        else:
                            second = s
                        break
                else:
                    continue
        if s == -1:
            return "None"
        else:
            h = first, second
            return h
    else:
        return None

#find_indices([7, -6, -25, 3, 3, -25, 13, 1], -50)
#find_indices([331, -267, 274, 331, -55, -380,  -273, -382, -151], -51)
#find_indices([-382, -267, 274, -382, -55, -380,  -273, 331, -151], -51)