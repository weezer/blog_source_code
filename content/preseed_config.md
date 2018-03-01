Title: a tip for preseed
Date: 02-12-2018
Category: tech
Tags: tech
Slug: preseed_config 
Authors: Weezer Su
Summary: a tip for preseed
```
d-i mirror/protocol string http
d-i mirror/http/hostname string cn.archive.ubuntu.com
d-i mirror/http/directory string /ubuntu
d-i mirror/http/proxy string
```
above is default, if you want to use local cache, switch it to below
```
d-i mirror/country string manual
d-i mirror/protocol string http
d-i mirror/http/hostname string 172.16.112.133  ＃HTTP服务器
d-i mirror/http/directory string /ubuntu12.04.4  ＃ISO目录
d-i mirror/http/proxy string http://172.16.112.133/＃proxy地址
```

