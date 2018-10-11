#!/usr/bin/python
# -*- coding: UTF-8 -*-

from qiniu import Auth, put_file, etag
from qiniu import BucketManager
from qiniu import http
import qiniu.config
import sys
import argparse
import json
import requests

access_key = 'vr70Yo2pV5Ffp0YbEgnMjSa_EPgvthnci_VxiRs0'
secret_key = 'Dx2X_tZg-wCekIbRjwRijf3_C9fmwC7heCkfae5v'

def upload(localfile, key, bucket):
    q = Auth(access_key, secret_key)
    bucket_name = bucket
    key = key
    token = q.upload_token(bucket_name, key, 3600)
    localfile = localfile
    result = http._get("http://api.qiniu.com/v6/domain/list?tbl=" + bucket, None, q)
    base_url = "http://" + result[0][0] + "/" + key
    ret, info = put_file(token, key, localfile)
    if info.status_code == 200:
        result = http._get("http://api.qiniu.com/v6/domain/list?tbl=" + bucket, None, q)
        link = "http://" + result[0][0] + "/" + key
        return link
    else:
        return "upload error"

def query(bucket_name, key):
    q = Auth(access_key, secret_key)
    bucket = BucketManager(q)
    ret, info = bucket.stat(bucket_name, key)
    q = Auth(access_key, secret_key)
    result = http._get("http://api.qiniu.com/v6/domain/list?tbl=" + bucket_name, None, q)
    print ret
    print(json.dumps(ret, sort_keys=True, indent=4))
    print "http://" + result[0][0] + "/" + key
    # print(info)

def queryList(bucket_name, prefix_name):
    q = Auth(access_key, secret_key)
    bucket = BucketManager(q)
    # 前缀
    prefix = prefix_name
    # 列举条目
    # limit = 10
    limit = None
    # 列举出除'/'的所有文件以及以'/'为分隔的所有前缀
    delimiter = None
    # 标记
    marker = None
    ret, eof, info = bucket.list(bucket_name, prefix, marker, limit, delimiter)
    print(json.dumps(ret, sort_keys=True, indent=4))

def queryBuckets():
    q = Auth(access_key, secret_key)
    result = http._get("http://rs.qbox.me/buckets", None, q)
    print result[0]

def queryBucketDomain(bucket_name):
    q = Auth(access_key, secret_key)
    result = http._get("http://api.qiniu.com/v6/domain/list?tbl=" + bucket_name, None, q)
    print result[0][0]

def download(bucket, key):
    q = Auth(access_key, secret_key)
    result = http._get("http://api.qiniu.com/v6/domain/list?tbl=" + bucket, None, q)
    base_url = "http://" + result[0][0] + "/" + key
    # base_url = 'http://domain/key'
    private_url = q.private_download_url(base_url, expires=3600)
    print(private_url)
    r = requests.get(private_url)
    assert r.status_code == 200

def delete(bucket_name, key):
    q = Auth(access_key, secret_key)
    bucket = BucketManager(q)
    ret, info = bucket.delete(bucket_name, key)
    print(info)
    assert ret == {}

# if move between the same bucket, then method can used to rename the file key
def move(src_bucket, src_key, des_bucket, des_key):
    q = Auth(access_key, secret_key)
    bucket = BucketManager(q)
    ret, info = bucket.move(src_bucket, src_key, des_bucket, des_key)
    print(info)
    assert ret == {}

def copy(src_bucket, src_key, des_bucket, des_key):
    q = Auth(access_key, secret_key)
    bucket = BucketManager(q)
    ret, info = bucket.copy(src_bucket, src_key, des_bucket, des_key)
    print(info)
    assert ret == {}

def cmd():
    args = argparse.ArgumentParser(description = 'QiNiuYun operation tools',epilog = 'Information end ')
    args.add_argument("-o", "--operation", type = str, dest = "operation", help = "specify operation", default = "upload", choices=["upload", "query", "queryList", "queryBuckets", "queryBucketDomain", "download", "delete", "move", "copy"])
    args.add_argument("-f", "--file", type = str, help = "the file to upload")
    args.add_argument("-k", "--key", type = str, help = "the key for the file to upload")
    args.add_argument("-b", "--bucket", type = str, help = "upload the file to specify bucket")
    args.add_argument("-c", "--condition", type = str, help = "query list by condition")
    args.add_argument("-sb", "--srcBucket", type = str, help = "source bucket")
    args.add_argument("-sk", "--srcKey", type = str, help = "source key")
    args.add_argument("-db", "--desBucket", type = str, help = "destination bucket")
    args.add_argument("-dk", "--desKey", type = str, help = "destination key")


    args = args.parse_args()
    d = args.__dict__
    if d["operation"] == "upload":
        upload(d["file"], d["key"], d["bucket"])
    elif d["operation"] == "query":
        query(d["bucket"], d["key"])
    elif d["operation"] == "queryList":
        queryList(d["bucket"], d["condition"])
    elif d["operation"] == "queryBuckets":
        queryBuckets()
    elif d["operation"] == "queryBucketDomain":
        queryBucketDomain(d["bucket"])
    elif d["operation"] == "download":
        download(d["bucket"], d["key"])
    elif d["operation"] == "delete":
        delete(d["bucket"], d["key"])
    elif d["operation"] == "move":
        move(d["srcBucket"], d["srcKey"], d["desBucket"], d["desKey"])
    elif d["operation"] == "copy":
        copy(d["srcBucket"], d["srcKey"], d["desBucket"], d["desKey"])


if __name__=="__main__":
    cmd()
