def find_indices(input_list, n):
    global f, sec
    d = dict()
    if len(input_list) > 1:
        for position, value in enumerate(input_list):
            raznost = n - value
            d[raznost] = position
        for j, val in enumerate(input_list):
            s = d.get(val, -1)
            if j == s:
                continue
            else:
                if s != -1:
                    if isinstance(s, list):
                        f = s[0]
                        sec = s[1]
                        break
                    else:
                        f = s
                        s = d.get(n - val, -1)
                        if isinstance(s, list):
                            sec = s[0]
                        else:
                            sec = s
                        break
                else:
                    continue
        if s == -1:
            return None
        else:
            return f, sec
    else:
        return None
