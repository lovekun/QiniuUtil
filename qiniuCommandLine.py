#!/usr/bin/python
# -*- coding: UTF-8 -*-

from qiniu import Auth, put_file, etag
from qiniu import BucketManager
form qiniu import http
import qiniu.config
import sys
import argparse

domain = "pf388se7v.bkt.clouddn.com"
access_key = 'vr70Yo2pV5Ffp0YbEgnMjSa_EPgvthnci_VxiRs0'
secret_key = 'Dx2X_tZg-wCekIbRjwRijf3_C9fmwC7heCkfae5v'

def upload(localfile, key, bucket='document'):
    q = Auth(access_key, secret_key)
    bucket_name = bucket
    key = key
    token = q.upload_token(bucket_name, key, 3600)
    localfile = localfile
    ret, info = put_file(token, key, localfile)
    if info.status_code == 200:
        link = "http://" + domain + key
        return link
    else:
        return "upload error"

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

def queryBuckets():
    q = Auth(access_key, secret_key)
    # token = q.token("/buckets\n") 
    result = http._get("http://rs.qbox.me/buckets", None, q)
    print result

def cmd():
    args = argparse.ArgumentParser(description = 'QiNiuYun operation tools',epilog = 'Information end ')
    args.add_argument("-o", "--operation", type = str, dest = "operation", help = "specify operation", default = "upload", choices=["upload", "query", "queryList", "queryBuckets"])
    args.add_argument("-f", "--file", type = str, help = "the file to upload")
    args.add_argument("-k", "--key", type = str, help = "the key for the file to upload")
    args.add_argument("-b", "--bucket", type = str, help = "upload the file to specify bucket")
    
    args = args.parse_args()
    d = args.__dict__
    if d["operation"] == "upload":
        upload(d["file"], d["key"], d["bucket"])
    elif d["operation"] == "query":
        query(d["bucket"], d["key"])
    elif d["operation"] == "queryList":
        queryList(d["bucket"])
    elif d["operation"] == "queryBuckets":
        queryBuckets()

if __name__=="__main__":
    cmd()