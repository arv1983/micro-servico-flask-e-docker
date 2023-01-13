# API TESTE SERASA

### RODAR TESTES:

python3 -m unittest -v

### RODAR APLICAÇÂO:

docker-compose up -d --build

## Usuarios

#### Criar usuário:

**URL** : `http://localhost:5000`

**Method** : `POST`

```json
{
  "name": "Nome Teste",
  "cpf": "01555487009",
  "email": "teste@teste.com",
  "phone_number": "51985862273"
}
```

## Resposta sucesso

**Code** : `201 CREATED`

**Content example**

```json
{
  "id": 1,
  "name": "Nome Teste",
  "cpf": "015.554.870-09",
  "email": "teste@teste.com",
  "phone": "51985862273",
  "created_at": "Sat, 02 Jul 2022 22:10:52 GMT",
  "updated_at": null
}
```

## Erros

**Condição** : Usuário já tem cadastro

**Code** : `401`

**Content** :

```json
{
  "erro": "CPF já cadastrado"
}
```

##

**Condition** : CPF Inválido

**Code** : `409 CONFLICT`

**Content** :

```json
{
  "erro": "CPF inválido"
}
```

##

**Condition** : CPF Inválido

**Code** : `401 CONFLICT`

**Content** :

```json
{
  "erro": "CPF já cadastrado"
}
```

##

#### Listar todos os usuários:

**URL** : `http://localhost:5000`

**Method** : `GET`

```json
[
  {
    "id": 1,
    "name": "Nome Teste",
    "cpf": "015.554.870-09",
    "email": "teste@teste.com",
    "phone": "51985862273",
    "created_at": "Sat, 02 Jul 2022 22:21:24 GMT",
    "updated_at": null
  },
  {
    "id": 2,
    "name": "Nome Teste2",
    "cpf": "008.440.123-49",
    "email": "teste2@teste.com",
    "phone": "51985862273",
    "created_at": "Sat, 02 Jul 2022 22:21:24 GMT",
    "updated_at": null
  }
]
```

##

#### Buscar usuário por CPF

**URL** : `http://localhost:5000/cpf/01555487009`

**Method** : `GET`

```json
{
  "id": 1,
  "name": "Nome Teste",
  "cpf": "015.554.870-09",
  "email": "teste@teste.com",
  "phone": "51985862273",
  "created_at": "Sat, 02 Jul 2022 22:10:52 GMT",
  "updated_at": null
}
```

##

#### Buscar usuário por ID

**URL** : `http://localhost:5000/id/1`

**Method** : `GET`

```json
{
  "id": 1,
  "name": "Nome Teste",
  "cpf": "015.554.870-09",
  "email": "teste@teste.com",
  "phone": "51985862273",
  "created_at": "Sat, 02 Jul 2022 22:10:52 GMT",
  "updated_at": null
}
```

##

### Editar usuário:

**URL** : `http://localhost:5000/cpf/01555487009`

**Method** : `PATCH`

```json
{
  "name": "anderson",
  "email": "novoemail@novoemail.com",
  "phone": "51985862273"
}
```

#### Resposta sucesso

**Code** : `200 OK`

```json
{
  "id": 1,
  "name": "anderson",
  "cpf": "015.554.870-09",
  "email": "novoemail@novoemail.com",
  "phone": "51985862273",
  "created_at": "Sat, 02 Jul 2022 22:21:24 GMT",
  "updated_at": "Sat, 02 Jul 2022 22:32:09 GMT"
}
```

#### Erro

**Condição** : Usuário já tem cadastro

**Code** : `409 CONFLICT` no content

##

### Deletar usuário:

**URL** : `http://localhost:5000/cpf/01555487009`

**Method** : `DELETE`

#### Resposta sucesso

**Code** : `200 OK`

#### Resposta Erro

**Condição** : Usuário não encontrado

**Code** : `404 NOT FOUND`

---

## Ordem

#### Criar ordem:

**URL** : `http://localhost:5002`

**Method** : `POST`

```json
{
  "user_id": 1,
  "item_description": "teste description",
  "item_quantity": 2,
  "item_price": 2.25
}
```

#### Resposta sucesso

**Code** : `201 CREATED`

#### Erro

**Condição** : Usuário não encontrado

**Code** : `404 NOT FOUND`

```json
{
  "Error": "User id not found"
}
```

#### Listar todas ordens:

**URL** : `http://localhost:5002`

#### Resposta sucesso

**Code** : `200 OK`

**Method** : `GET`

```json
{
  [
    {
      "id": 1,
      "user id": 1,
      "item_description": "teste description3",
      "item_quantity": 2.0,
      "item_price": 2.25,
      "total_value": 4.5,
      "created_at": "Sun, 03 Jul 2022 15:10:22 GMT",
      "updated_at": null
    }
  ]
}
```

#### Erro

**Condição** : Não existe ordem

**Code** : `404 NOT FOUND`

#### Ordem por CPF:

**URL** : `http://localhost:5002/order/1`

**Method** : `GET`

#### Resposta sucesso

**Code** : `200 OK`

```json
{
  "id": 1,
  "user id": 1,
  "item_description": "teste description3333",
  "item_quantity": 3.0,
  "item_price": 2.25,
  "total_value": 6.75,
  "created_at": null,
  "updated_at": "Sun, 03 Jul 2022 00:00:00 GMT"
}
```

#### Erro

**Condição** : Ordem não encontrada

**Code** : `404 NOT FOUND`

```json
{
  "Error": "Order not found."
}
```

#### Ordem por id:

**URL** : `http://localhost:5002/order/cpf/01555487009`

**Method** : `GET`

#### Resposta sucesso

**Code** : `200 OK`

```json
[
  {
    "id": 1,
    "user id": 1,
    "item_description": "teste description3",
    "item_quantity": 2.0,
    "item_price": 2.25,
    "total_value": 4.5,
    "created_at": "Sun, 03 Jul 2022 15:10:22 GMT",
    "updated_at": null
  }
]
```

#### Erro

**Condição** : CPF não encontrado

**Code** : `404 NOT FOUND`

```json
{
  "Error": "Cpf not found"
}
```

#### Editar ordem:

**URL** : `http://localhost:5002/order/1`

**Method** : `PATCH`

```json
{
  "item_description": "teste description3333",
  "item_quantity": 4,
  "item_price": 1
}
```

#### Resposta sucesso

**Code** : `200 OK`

```json
{
  "id": 1,
  "user id": 1,
  "item_description": "teste description3333",
  "item_quantity": 4.0,
  "item_price": 1.0,
  "total_value": 4.0,
  "created_at": "Sun, 03 Jul 2022 15:35:47 GMT",
  "updated_at": "Sun, 03 Jul 2022 15:35:59 GMT"
}
```

#### Erro

**Condição** : Ordem não encontrada

**Code** : `404 NOT FOUND`

```json
{
  "Error": "Order not found."
}
```

#### Deletar ordem:

**URL** : `http://localhost:5002/order/1`

**Method** : `DELETE`

#### Resposta sucesso

**Code** : `200 OK`

#### Erro

**Condição** : Ordem não encontrada

**Code** : `404 NOT FOUND`

```json
{
  "Error": "Order not found."
}
```
