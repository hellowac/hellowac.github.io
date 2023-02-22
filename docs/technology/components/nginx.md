# nginx

* 官网: <https://nginx.org/>
* 下载: <https://nginx.org/en/download.html>
* 文档: <https://nginx.org/en/docs/>

**安装**

* 首页: <https://nginx.org/en/docs/install.html>
* 包安装: <https://nginx.org/en/linux_packages.html>
* RHEL/CentOS: <https://nginx.org/en/linux_packages.html#RHEL-CentOS>

## 示例配置

```conf
upstream linuxidc {
        server localhost:8500;
        server localhost:8501;
        server localhost:8502;
        server localhost:8503;
}

server {
    listen       80;
    listen       [::]:80;
    #server_name  security.cdiisp.com;
    root         /opt/front;
    client_max_body_size 100M;

    #Load configuration files for the default server block.
    #include /etc/nginx/default.d/*.conf;

    location ^~ /api {
        include /etc/nginx/uwsgi_params;
        proxy_pass http://linuxidc;
        # uwsgi_pass portal;
        proxy_set_header REMOTE_ADDR $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    error_page 404 /404.html;
    location = /404.html {
    }

    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
    }
}

```
