Caso precisemos persistir arquivos, podemos usar os volumes, que são diretórios gerenciados pelo docker. Tornando-os mais seguros no caso de interferência do sistema e do usuário com eles, o que impede erros inesperados e dá mais segurança e confiabilidade na execução de containers.

```
#cria volume manualmente
docker volume create my-volume
```

```
#associa volume a container. Caso o volume não exista, ele será criado durante a execução do comando
docker run -it -v my-volume:/app ubuntu bash
```

```
#também é possível fazer um bind mount com diretórios locais do SO, mas não é recomendado por questões de segurança (user pode deletar pasta e dar erro no container)
docker run -it -v /home/fabio/docker-folder:/app ubuntu bash
```

```
#podemos criar pastas temporárias, por exemplo, no caso de enviarmos senhas, que não persistam quando o container morrer
docker run -it --tmpfs=/app ubuntu bash
```
