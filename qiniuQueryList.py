# -*- coding: utf-8 -*-

from qiniu import Auth, put_file, etag
from qiniu import BucketManager
import qiniu.config
import sys

domain = 'pf388se7v.bkt.clouddn.com'
access_key = 'vr70Yo2pV5Ffp0YbEgnMjSa_EPgvthnci_VxiRs0'
secret_key = 'Dx2X_tZg-wCekIbRjwRijf3_C9fmwC7heCkfae5v'

def queryList(bucket_name):
    q = Auth(access_key, secret_key)
    bucket = BucketManager(q)

    # bucket_name = 'lovekun'
    # 前缀
    prefix = None
    # 列举条目
    limit = 10
    # 列举出除'/'的所有文件以及以'/'为分隔的所有前缀
    delimiter = None
    # 标记
    marker = None
    ret, eof, info = bucket.list(bucket_name, prefix, marker, limit, delimiter)
    print(info)


# arg1: bucket name
if __name__ == "__main__":
    # link = upload('C:\Users\qiuaikun\Downloads\mytest.jpg', 'mytest.jpg')
    link = queryList(sys.argv[1])
    print(link)
