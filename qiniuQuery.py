# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth
from qiniu import BucketManager
import sys

access_key = 'vr70Yo2pV5Ffp0YbEgnMjSa_EPgvthnci_VxiRs0'
secret_key = 'Dx2X_tZg-wCekIbRjwRijf3_C9fmwC7heCkfae5v'

def query(bucket_name, key):
    #初始化Auth状态
    q = Auth(access_key, secret_key)
    #初始化BucketManager
    bucket = BucketManager(q)
    #你要测试的空间， 并且这个key在你空间中存在
    # bucket_name = 'document'
    # key = 'mytest.jpg'
    #获取文件的状态信息
    ret, info = bucket.stat(bucket_name, key)
    print(info)

# arg1: bucket name
# arg2: key
if __name__ == "__main__":
    # link = upload('C:\Users\qiuaikun\Downloads\mytest.jpg', 'mytest.jpg')
    link = query(sys.argv[1], sys.argv[2])
    print(link)
