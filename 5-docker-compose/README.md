Replicando a atividade dos comandos abaixo num docker-compose

Atividade: fazer os containers mongo:4.4.6 e aluradocker/alura-books:1.0 se comunicarem via rede docker
```
docker run -d --network minha-bridge --name meu-mongo mongo:4.4.6
docker run -d --network minha-bridge -p 3000:3000 aluradocker/alura-books:1.0    
```

Comandos do compose
```
docker-compose up 
docker-compose up -d
docker-compose ps
docker-compose down
```