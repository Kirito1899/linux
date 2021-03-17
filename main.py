#!/usr/bin/env python
import sys
import os
import time

if len (sys.argv) != 4:
    print("Need arguments: string, count streams, number of iterations")
    exit()
pids = {}
n = 1
my_file = open("BabyFile.log", "a+")
main_tr = os.getpid()
my_number = 0
for i in range(0, int(sys.argv[2])):
    if os.getpid() == main_tr:
        n = os.fork()
        my_number = i + 1
if os.getpid() == main_tr:
    my_number = 0

for i in range(0, int(sys.argv[3])*my_number):
    my_file.write(f"{sys.argv[1]}, iterrs = {i}\n")
    time.sleep(1)

