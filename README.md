# Armas e Munição API
Projeto de desafio para vaga de Desenvolvedor Python Jr.

### Pré-requisitos:
* Docker
* Docker-compose

### Como subir o projeto:
- OBS: Existe a possibilidade do Git fazer alterações em arquivos do tipo LF para CRLF no momento do checkout, que interferem com o script sh utilizado para sincronizar a subida dos containers pelo docker-compose. Caso o comando "docker-compose up" acuse o erro "/usr/bin/env: ‘bash\r’: No such file or directory", execute o comando "git config --global core.autocrlf false" e clone o repositório em outra pasta

- git clone https://github.com/rodrigowb4ey/guns-and-ammo-api.git guns_api
- cd guns_api
- docker-compose up
- Acesse a aplicação em localhost:8000

### Frameworks utilizados no desenvolvimento:
- Django
- Django REST Framework

## Autor:
* Rodrigo Bezerra Saraiva
