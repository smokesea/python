# coding=utf-8

import os

#  Once had a problem that bothered me for a long time,
#  when processing online Nginx logs, > 1G files, according to normal operation
#  needs a long time。
#  Some people say that you can use hadoop, but I only do some simple statistical work, 
#  hadoop is too heavy.
#  
#  Method1: use builin lib `gzip`
#  Result: python3 1G gz log use > 60s。python 2.7 > 10m
def read_gz_log_buildin(filename):
    if not os.path.exists(filename):
        raise Exception("no such file %s" % filename)
    import gzip
    with gzip.open(filename, 'rb') as f:
        for line in f:
            line = line[:-1]
            print(line)
        f.close()
    


#  Method2: OS linux, need `gunzip` command installed 
#  use popen call the cmd and fethch output
#  Result: any python version 1G gz log file use time <10s
def read_gz_log_popen(filename):
    if not os.path.exists(filename):
        raise Exception("no such file %s" % filename)
    rf = os.popen("gunzip -c %s" % filename)
    for line in rf:
        line = line[:-1]  # trim \n
        # print(line)  # do something
    cmd_ret = rf.close()
    if cmd_ret is None:
        print("success")
    else:
        print("error code is %d" % cmd_ret)

read_gz_log_buildin("nginx_access_log_2017xxxxx.gz")