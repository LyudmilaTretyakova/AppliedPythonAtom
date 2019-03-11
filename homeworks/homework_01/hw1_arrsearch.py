def find_indices(input_list, n):
    f = 0
    ss = 0
    dic = dict()
    if len(input_list) > 1:
        for position, value in enumerate(input_list):
            dic[n - value] = position
        for j, val in enumerate(input_list):
            s = dic.get(val, -1)
            if j == s:
                continue
            else:
                if s != -1:
                    if isinstance(s, list):
                        f = s[0]
                        ss = s[1]
                        break
                    else:
                        f = s
                        s = dic.get(n - val, -1)
                        if isinstance(s, list):
                            ss = s[0]
                        else:
                            ss = s
                        break
                else:
                    continue
        if s == -1:
            return None
        else:
            return f, ss
    else:
        return None
