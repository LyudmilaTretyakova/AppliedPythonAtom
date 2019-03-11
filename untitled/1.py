#!/usr/bin/env python
# coding: utf-8
'''
    Метод возвращает индексы двух различных
    элементов listа, таких, что сумма этих элементов равна
    n. В случае, если таких элементов в массиве нет,
    то возвращается None
    Ограничение по времени O(n)
    :param input_list: список произвольной длины целых чисел
    :param n: целевая сумма
    :return: tuple из двух индексов или None
    '''

def find_indices(input_list, n):

    c=tuple()
    n=0
    k=len(input_list)-1
    pairs=dict()
    for i in input_list:
       pairs[i]= hash(i)
        #pairs={i:hash(i)}
    for i in input_list:
        if( hash(n-i) in pairs):
            pairs
            c=[i,pairs[i]]
    if len(c)==0:
        return 'None'
    else:
        return c
    raise NotImplementedError
