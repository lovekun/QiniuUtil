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

# arg1: file path
# arg2: key
# arg3: bucket name
if __name__ == "__main__":
    # link = upload('C:\Users\qiuaikun\Downloads\mytest.jpg', 'mytest.jpg')
    link = upload(sys.argv[1], sys.argv[2])
    print(link)
