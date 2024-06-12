# Projeto Jeitto - CRUD de Clientes

## Requisitos

Para executar o projeto, você precisará ter o Docker e Docker Compose instalados.

## Instalação

1. Clone o repositório para o seu ambiente local.
2. Adicione o arquivo `.env` no diretório raiz da aplicação.

## Executando a Aplicação com Docker

1. Construa as imagens do Docker: `docker compose build` ou `docker compose up --build`
  
3. Para iniciar os contêineres sem reconstruir, utilize:
   `docker compose up`

## Migração do Banco de Dados

Para gerar as migrações no banco de dados, execute o seguinte comando: `alembic upgrade head`

## Rotas

### Criar Cliente

    Rota: customers/
    Método: POST
    Payload:

    {
      "name": "string",
      "email": "EmailStr",
      "phone": "string"
    }

### Recuperar Cliente

    Rota: customers/{customer_id: int}
    Método: GET
    Parâmetro: Inteiro referente ao ID do cliente

## Fixtures

Para facilitar e verificar se o retorno dos endpoints estavam tendo o comportamento esperado, criei algumas fixtures.
Abaixo estão os exemplos utilizados para gerar payloads de clientes e retornar um cliente específico.

Objeto usado para gerar um payload de cliente:
```python
CreateCustomer(name="Matheus", email="matheus@example.com", phone="21999999999")
```

Objeto usado para recuperar um cliente específico:
```Python
RetrieveCustomer(id=1, name="Matheus", email="matheus@example.com", phone="21999999999")
```

## Testes Unitários

Para executar os testes unitários, certifique-se de que tenha instalado em sua máquina a biblioteca `pytest` utilize o seguinte comando caso esteja executando a partir do diretório raiz da aplicação:
  ```bash
  pytest -v app/tests/
  ```
