FROM node:14
COPY . .
WORKDIR /app-node

# cria argumento existente em tempo de criação de container, mas não durante a execução do mesmo
ARG PORT_BUILD=8080             

# exporta um argumento para dentro do container, de modo que ele possa ser usando na sua execução
# PORT_ENV torna-se variável de ambiente, acessível pela aplicação
ENV PORT=$PORT_BUILD

EXPOSE $PORT_BUILD
RUN npm install
ENTRYPOINT npm start