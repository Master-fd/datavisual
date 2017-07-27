# -*- coding: utf-8 -*-
'''

'''

; 深圳开放平台测试环境
[program:seed_server]
command=/usr/local/python27/bin/gunicorn -w 5 -b 127.0.0.1:26805 -t 60 --worker-class gevent main:app
process_name=%(program_name)s ; process_name expr (default %(program_name)s)
numprocs=1                    ; number of processes copies to start (def 1)
directory=/data/wwwroot/open_data_report                ; directory to cwd to before exec (def no cwd)
autostart=true                ; start at supervisord start (default: true)
stopsignal=QUIT               ; signal used to kill process (default TERM)
redirect_stderr=true          ; redirect proc stderr to stdout (default false)
stdout_logfile=/data/other/python_log/supervisor_%(program_name)s.log        ; stdout log path, NONE for none; default AUTO
stdout_logfile_maxbytes = 50MB
stdout_logfile_backups  = 10


# 自助报表
server
{
    server_name seed_server_test.oa.com;
    listen 80;
    location / {
        proxy_pass http://127.0.0.1:26805;
        proxy_redirect off;
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Scheme $scheme;
        proxy_set_header REMOTE_ADDR $remote_addr;
    }
    access_log /data/other/nginx_logs/${host}_${server_port}_access.log main;
}

