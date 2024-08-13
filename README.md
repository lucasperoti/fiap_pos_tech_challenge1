
# Projeto FIAP - Sistema de Controle de Pedidos

Este projeto foi desenvolvido como parte de um desafio técnico da FIAP, utilizando Django REST Framework e seguindo a Arquitetura Hexagonal. O sistema permite o cadastro e gestão de clientes, produtos e pedidos, além de simular um fake checkout através da rota de `orders`.

## Arquitetura Hexagonal

A arquitetura hexagonal, também conhecida como Ports and Adapters, foi aplicada neste projeto para garantir uma separação clara entre as regras de negócio e os detalhes de implementação, como frameworks e tecnologias. A estrutura do projeto está organizada da seguinte forma:

```
projeto_fiap/
│
├── adapters/
│   ├── driven/
│   │   └── infra/
│   │       └── database/
│   │           ├── models/
│   │           └── repositories/
│   └── driver/
│       └── api/
│           ├── controllers/
│           └── serializers/
│
├── core/
│   └── application/
│       └── services/
│   └── domain/
│       └── entities/
│       └── repositories/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
└── Dockerfile
└── docker-compose.yml
```

### Camadas da Arquitetura

- **Domain (Domínio):** Contém as entidades e repositórios que definem as regras de negócio. Essa camada é completamente independente de qualquer tecnologia específica.
- **Application (Aplicação):** Contém os serviços que orquestram as operações de negócio, chamando os repositórios do domínio.
- **Adapters:** Contém as implementações que conectam as regras de negócio a frameworks externos, como Django e o banco de dados PostgreSQL.
- **Config:** Contém as configurações do projeto Django.

## Como Rodar o Projeto com Docker

Para rodar o projeto utilizando Docker, siga os passos abaixo:

### 1. Clonar o Repositório

```bash
git clone https://github.com/lucasperoti/fiap_pos_tech_challenge1.git
cd projeto_fiap
```

### 2. Configurar o Banco de Dados

No arquivo `docker-compose.yml`, o serviço do banco de dados PostgreSQL já está configurado com os seguintes parâmetros:

```yaml
POSTGRES_DB=postech_fiap
POSTGRES_USER=postgres
POSTGRES_PASSWORD=0212
```

### 3. Construir e Rodar os Containers

Execute os comandos abaixo para construir e iniciar os containers:

```bash
docker-compose up --build
```

### 4. Acessar a Aplicação

Após iniciar os containers, você pode acessar a aplicação em `http://localhost:8000`.

## Rotas da API

A aplicação oferece as seguintes rotas de API:

### Clientes

- `GET /api/customers/`: Lista todos os clientes.
- `POST /api/customers/`: Cria um novo cliente.
- `GET /api/customers/{cpf}/`: Obtém detalhes de um cliente pelo CPF.
- `PATCH /api/customers/{cpf}/`: Atualiza um cliente existente pelo CPF.
- `DELETE /api/customers/{cpf}/`: Deleta um cliente existente pelo CPF.

### Produtos

- `GET /api/products/`: Lista todos os produtos.
- `POST /api/products/`: Cria um novo produto.
- `PUT /api/products/`: Atualiza um produto existente.
- `DELETE /api/products/`: Deleta um produto existente.

### Pedidos (Orders)

- `POST /api/orders/`: Cria um novo pedido, simulando um fake checkout.
- `GET /api/orders/{order_id}/`: Obtém detalhes de um pedido pelo ID.
- `PATCH /api/orders/{order_id}/`: Atualiza o status de um pedido existente.

### Simulação de Fake Checkout

A rota `POST /api/orders/` foi configurada para simular um processo de checkout fake. Ao chamar esta rota, um pedido é criado e os produtos selecionados são vinculados a esse pedido. Este processo simula a finalização de uma compra sem realizar qualquer transação financeira real.

## Acessando o Swagger

A aplicação oferece uma interface Swagger UI que permite visualizar e testar todas as rotas da API de forma interativa. Você pode acessar o Swagger UI através da seguinte URL:

http://127.0.0.1:8000/api/schema/swagger-ui/

Essa interface fornece uma maneira fácil e visual de interagir com as APIs disponíveis, facilitando a compreensão e o teste das funcionalidades oferecidas pelo sistema.

