#!/usr/bin/env python
# coding: utf-8
from multiprocessing import Pool
import os


def count(path):
    s = ''
    with open(path, encoding='utf-8') as fd:
        s = fd.read()
        s = s.split(' ')
        s1 = ' '.join(s).split()
        return len(s1)


def word_count_inference(path_to_dir):
    ssd = {}
    out = []
    files = os.listdir(path_to_dir)
    files1 = [path_to_dir + '/' + f for f in files]
    l = 0
    with Pool(len(files1)) as p:
        out = (p.map(count, files1))
    out.append(sum(out))
    files.append('total')
    ssd = dict(zip(files, out))
    return ssd
