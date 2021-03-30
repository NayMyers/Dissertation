server {
  listen 3002 default_server;
  listen 138.68.177.42;
  root /my-project/dist;
  index index.html index.htm index.nginx-debian.html;
  server_name 138.68.177.42;
  error_page 404 /index.html;
  location / {
    root /var/www/myapp/dist;
    try_files $uri  /index.html;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Host $http_host;
    proxy_set_header X-NginX-Proxy true;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_max_temp_file_size 0;
    proxy_redirect off;
    proxy_read_timeout 240s;
  }
}
