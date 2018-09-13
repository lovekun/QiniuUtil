# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import Auth, put_file, etag
import qiniu.config

access_key = 'vr70Yo2pV5Ffp0YbEgnMjSa_EPgvthnci_VxiRs0'
secret_key = 'Dx2X_tZg-wCekIbRjwRijf3_C9fmwC7heCkfae5v'

q = Auth(access_key, secret_key)

bucket_name = 'document'

key = 'mytest.jpg'

#上传文件到七牛后， 七牛将文件名和文件大小回调给业务服务器。
#policy={
#        'callbackUrl':'http://p8uwsq3zo.bkt.clouddn.com/callback.php',
#        'callbackBody':'filename=$(fname)&filesize=$(fsize)'
#        }

# token = q.upload_token(bucket_name, key, 3600, policy)
token = q.upload_token(bucket_name, key, 3600)

# localfile = '/Users/lovekun/Desktop/aaa.jpg'
localfile = 'C:\Users\qiuaikun\Downloads\mytest.jpg'

ret, info = put_file(token, key, localfile)
print(info)
print(ret)
print("http://p8uwsq3zo.bkt.clouddn.com/" + key)
# assert ret['key'] == key
# assert ret['hash'] == etag(localfile)

# http://p8uwsq3zo.bkt.clouddn.com/mytest.jpg

