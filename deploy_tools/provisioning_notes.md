Provisionamento de um novo site
=================
## Pacotes necessários

* nginx
* python 3.8
* virtualenv + pip
* git

No ubuntu:
    sudo apt-get install nginx git python3.8 python3.8-venv

## Config do Nginx Virtual host

* veja nginx.template.conf
* substitua SITENAME por my-domain.com.br

## Serviço Systemd

* veja gunicorn-systemd.template.service
* substitua SITENAME por my-domain.com.br

## Estrutura de pastas:
suponha que temos uma conta de usuário em /home/username
/home/username
    SITENAME
        source
        static
