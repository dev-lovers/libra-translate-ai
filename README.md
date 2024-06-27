# Libra Translate AI

Libra Translate AI é um componente essencial do aplicativo Libra Translate, focado na tradução automática de Libras (Língua Brasileira de Sinais) para texto ou voz. Utilizando modelos de aprendizado profundo, este serviço identifica e interpreta sinais em Libras a partir de imagens enviadas pelo backend, tornando a comunicação mais acessível e inclusiva para pessoas surdas ou com deficiência auditiva.

## Pré-requisitos

- Docker instalado no seu sistema. Você pode fazer o download e instalar o Docker a partir do [site oficial do Docker](https://www.docker.com/get-started).

## Como Implantar

Para subir o serviço utilizando Docker Compose com a tag de build:

1. Clone este repositório para o seu ambiente local, se ainda não o fez:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. Navegue até o diretório onde está localizado o arquivo `docker-compose.yml`:

   ```bash
   cd caminho/para/seu-repositorio
   ```

3. Execute o seguinte comando para construir (se necessário) e iniciar os containers definidos no seu arquivo `docker-compose.yml`:

   ```bash
   docker-compose up --build
   ```

Isso iniciará o servidor TensorFlow Serving no contêiner conforme definido no seu arquivo `docker-compose.yml`, tornando-o acessível nas portas especificadas.

## Acesso ao Servidor TensorFlow Serving

Uma vez que o servidor TensorFlow Serving esteja em execução, você pode acessar a previsão do modelo usando a interface REST (HTTP) ou gRPC. Aqui estão os URLs básicos para acesso:

- REST (HTTP): `http://localhost:8501/v1/models/iana:predict`
- gRPC: `grpc://localhost:8500`

Substitua `iana` pelo nome do seu modelo conforme especificado no seu arquivo `docker-compose.yml`.

## Informações Adicionais

- Verifique se o modelo está localizado no diretório correto dentro do contêiner, conforme especificado no Dockerfile utilizado pelo Docker Compose.
- Para informações detalhadas sobre o TensorFlow Serving e suas capacidades, consulte a [documentação oficial do TensorFlow Serving](https://www.tensorflow.org/tfx/guide/serving).
