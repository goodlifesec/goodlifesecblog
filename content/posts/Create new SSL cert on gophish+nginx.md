---
title: Create new SSL cert on gophish+nginx
date: 2024-12-03
draft: false
tags:
  - nginx
  - ssl
  - gophish
categories: Reference
---

1. login as root on the nginx server
2. create a new openssl certificate
	`sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/<<domain>>.key -out /etc/nginx/ssl/<<domain>>.cer`
1. copy the existing server block to the bottom of the nginx config file at `sudo vi /etc/nginx/conf.d/revers-proxy.conf` 
2. update the new block with the new domain name (see below)
3. save and quit
4. test nginx `nginx -t`
5. Issue the certificate with the command below
`./acme.sh --issue -d <<domain>> --server letsencrypt --nginx`
6. install certificate with the command below:
```
.acme.sh/acme.sh --install-cert -d <<domain>> \
> --key-file /etc/nginx/ssl/<<domain>>.key \
> --fullchain-file /etc/nginx/ssl/<<domain>>.cer \
> --reloadcmd "service nginx restart"
```


### server block
```
server {
        listen 80;
        server_name <<domain>> www.<<domain>>; ## server name can be replaced by nginx server IP address (ex. 192.168.1.132)

        location / {
                proxy_pass http://23.138.40.37:80; ## backend-server can be replaced with IP address of web sever to be proxied (ex. http192.168.1.37:80)
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
        listen 443 ssl;
        ssl_certificate_key /etc/nginx/ssl/<<domain>>.key;
        ssl_certificate /etc/nginx/ssl/<<domain>>.crt;
}
```