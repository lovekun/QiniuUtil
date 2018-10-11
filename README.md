# QiniuUtil
七牛云操作工具

# 使用说明
1. 查询单个文件: `python qiniuCommandLine.py -o query -b bucket_name -k key_name`
2. 查询一组文件(根据前缀): `python qiniuCommandLine.py -o queryList -b bucket_name`
3. 下载文件: `python qiniuCommandLine.py -o download -b bucket_name -k key_name`
4. 上传文件: `python qiniuCommandLine.py -o upload -f file_path -b bucket_name -k key_name`
5. 查询buckets: `python qiniuCommandLine.py -o queryBuckets`
6. 查询buckets对应的域名: `python qiniuCommandLine.py -o queryBucketDomain -b bucket_name`
7. 删除文件: `python qiniuCommandLine.py -o delete -b bucket_name -k key_name`
8. 移动文件(重命名): `python qiniuCommandLine.py -o move -sb srouce_bucket -sk source_key -db des_bucket -dk des_key`
9. 拷贝文件: `python qiniuCommandLine.py -o copy -sb srouce_bucket -sk source_key -db des_bucket -dk des_key`

# TODO
- [ ] 对结果进行解析，提高结果的可读性
