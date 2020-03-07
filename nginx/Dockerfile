FROM nginx:1.17.2-alpine

# DIR: logs
RUN mkdir -p /var/log/nginx
# DIR: plataforma 2
RUN mkdir -p /var/www/telessaude/v2
# DIR: SPA
RUN mkdir -p /var/www/telessaude/v4
# Alterando owner:group do arquivo para o user do nginx
RUN chown -R nginx: /var/www/telessaude

COPY nginx.conf /etc/nginx/
