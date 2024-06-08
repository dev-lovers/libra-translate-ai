# Guia de Implantação do Contêiner TensorFlow Serving

Este guia fornecerá instruções básicas sobre como implantar o contêiner Docker configurado para servir modelos TensorFlow usando TensorFlow Serving.

## Pré-requisitos

- Docker instalado no seu sistema. Você pode fazer o download e instalar o Docker a partir do [site oficial do Docker](https://www.docker.com/get-started).

## Como Implantar

1. Clone este repositório para o seu ambiente local:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. Navegue até o diretório clonado:

   ```bash
   cd seu-repositorio
   ```

3. Construa o contêiner Docker usando o Dockerfile fornecido:

   ```bash
   docker build -t meu-servidor-tensorflow .
   ```

4. Execute o contêiner Docker:

   ```bash
   docker run -p 8501:8501 -p 8500:8500 meu-servidor-tensorflow
   ```

Isso iniciará o servidor TensorFlow Serving no contêiner e o tornará acessível nas portas 8500 (gRPC) e 8501 (REST) do seu sistema.

## Acesso ao Servidor TensorFlow Serving

Uma vez que o servidor TensorFlow Serving esteja em execução, você pode acessar a previsão do modelo usando a interface REST (HTTP) ou gRPC. Aqui estão os URLs básicos para acesso:

- REST (HTTP): `http://localhost:8501/v1/models/iana:predict`
- gRPC: `grpc://localhost:8500`

Substitua `iana` pelo nome do seu modelo conforme especificado durante a construção do contêiner.

## Informações Adicionais

- Certifique-se de que o modelo esteja localizado no diretório correto dentro do contêiner, conforme especificado no Dockerfile.
- Para informações detalhadas sobre o TensorFlow Serving e suas capacidades, consulte a [documentação oficial do TensorFlow Serving](https://www.tensorflow.org/tfx/guide/serving).
