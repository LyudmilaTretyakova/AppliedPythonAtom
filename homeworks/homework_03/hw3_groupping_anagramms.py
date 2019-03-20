#!/usr/bin/env python
# coding: utf-8


def groupping_anagramms(words):
    res = []
    k = 0
    try:
        t = [sorted(word.lower()) for word in words]
        for i in range(len(t)):
            if t[i] is not None:
                res.append([words[i]])
                for j in range(i + 1, len(t)):
                    if t[i] == t[j]:
                        res[k].append(words[j])
                        t[j] = None
                k += 1
                t[i] = None
        return res
    except Exception:
        return res
