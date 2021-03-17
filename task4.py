#!/usr/bin/python3
import sys
import os
import time
import os.path

if len (sys.argv) != 4:
    print("Need arguments: string, count streams, number of iterations")
    exit()
pids = []
n = 1
my_file = open("File.log", "a+")
main_tr = os.getpid()
main_ppid = os.getppid()
my_number = 0
for i in range(0, int(sys.argv[2])):
    if os.getpid() == main_tr:
        n = os.fork()
        my_number = i + 1
        pids.append(n)
if os.getpid() == main_tr:
    my_number = 0

for i in range(1, int(sys.argv[3])*my_number):
    if os.getppid() == main_ppid:
        os.kill(os.getpid(), 1)
    my_file.write(f"{sys.argv[1]}, iterrs = {i}, pid = {os.getpid()}, my_number = {my_number}\n")
    time.sleep(10)

if os.getpid() == main_tr:
    for p in pids:
        if os.path.exists(f'/proc/{p}') == False:
            os.kill(os.getpid(), 1)
