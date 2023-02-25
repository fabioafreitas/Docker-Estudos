```
# lista as redes que o docker gerencia. As redes bridge são as que geram um isolamenot de rede entre containers
docker network ls
```

```
# cria uma nova rede interna do docker, gerenciada pelo drive bridge, para ter o isolamento de rede do docker
docker network create --driver bridge minha-bridge
```

Atividade: fazer os containers mongo:4.4.6 e aluradocker/alura-books:1.0 se comunicarem via rede docker
```
docker run -d --network minha-bridge --name meu-mongo mongo:4.4.6
docker run -d --network minha-bridge -p 3000:3000 aluradocker/alura-books:1.0    
```

