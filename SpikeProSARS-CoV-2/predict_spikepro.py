# -*- coding: utf-8 -*-
import subprocess
import os
import numpy as np
import multiprocessing

# label = []
# sequence = []
# f = open('H:/Py Files/coronavirus_final_revise/for_github_add_host/data/SARS-CoV-2 S test set.fasta').readlines()
# for i in f:
#     if '>' in i:
#         label.append(i.rstrip('\n').lstrip('>'))
#     else:
#         sequence.append(i.rstrip('\n'))
# for i in range(len(label)):
#     f_new = open('H:/Py Files/SpikeProSARS-CoV-2-main/test/'+label[i]+'.fasta', 'w')
#     f_new.write('>'+label[i]+'\n')
#     f_new.write(sequence[i]+'\n')
#     f_new.close()


def run_predict(file):
    cmd = './SpikePro ./test/%s go > ./output/%s' % (file, file.split('.')[0]+'.txt')
    p = subprocess.Popen(cmd, shell=True)
    return_code = p.wait()
    return cmd


if __name__ == '__main__':
    path = '/mnt/h/Py Files/SpikeProSARS-CoV-2-main/test/'
    dir_list = os.listdir(path)
    # print(dir_list)
    cmd = 'cd "/mnt/h/Py Files/SpikeProSARS-CoV-2-main"'
    p = subprocess.Popen(cmd, shell=True)
    return_code = p.wait()
    # print(cmd)
    # for i in dir_list:
    #     cmd = './SpikePro ./test/%s go > ./output/%s' % (i, i.split('.')[0]+'.txt')
    #     p = subprocess.Popen(cmd, shell=True)
    #     return_code = p.wait()
    #     print(cmd)

    pool = multiprocessing.Pool(processes=32)
    pool.map(run_predict, dir_list)
    pool.close()
    pool.join()
