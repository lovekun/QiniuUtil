from qiniu import Auth, put_file, etag
import qiniu.config
import sys

domain = pf388se7v.bkt.clouddn.com
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

def queryList(bucket):
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
    ret, eof, info = bucket.list(bucket, prefix, marker, limit, delimiter)
    print(info)


# arg1: file path
# arg2: key
# arg3: bucket name
# arg4: method name
if __name__ == "__main__":
    # link = upload('C:\Users\qiuaikun\Downloads\mytest.jpg', 'mytest.jpg')
    link = upload(sys.argv[1], sys.argv[2])
    print(link)
