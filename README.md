![Lucree](https://lucreestatic.s3.us-east-2.amazonaws.com/dashboard/assets/img/brand/logo-lucree-horizontal.png)

# Desafio Backend

O desafio consiste em criar uma API REST para uma Conta Digital, onde o usuário poderá realizar pagamentos para seus amigos e adicionar cartões de crétido, que será consumida por um aplicativo (Android e iOS). Onde o usuário irá cadastrar/listar/editar/apagar um cartão quando desejar e transferir e listar o extrato de pagamentos.

O candidato deve dar **fork** neste repositório e após o termino do desenvolvimento, realizar um **pull request** para análise do time.

O candidato deve realizar a implementação buscando utilizar a linguagem Python ou Go. Demais Frameworks/Libs ficam por conta do candidato.

Deverá informar quais tecnologias foram usadas, como instalar, rodar e efetuar os acessos no arquivo [`details.txt`](https://github.com/Lucree-Dev/desafio-backend/blob/master/details.txt) (se necessário) para análise do desafio.

### Extra
- Autenticação nas requisições
- Utilizar Docker


### POST `/account/person`
Esse método deve receber um novo usuário e inseri-lo em um banco de dados para ser consumido pela própria API.
```json
{
   "first_name":"João",
   "last_name": "das Neves",
   "birthday": "1991-09-91",
   "password": "*****",
   "username": "joao_das_neves",
   "user_id": "70c881d4a26984ddce795f6f71817c9cf4480e79"
}
```
| Campo       | Tipo   |
|-------------|--------|
| first_name  | String |
| last_name   | String |
| birthday    | String |
| password    | String |
| username    | String |

### GET `/account/friends`
Esse método da API deve retornar o seguinte JSON com os amigos do usuário
```json
[
  {
   "first_name":"João",
   "last_name": "das Neves",
   "birthday": "1991-09-91",
   "username": "joao_das_neves",
   "user_id": "70c881d4a26984ddce795f6f71817c9cf4480e79"
  },
  {
   "first_name":"João",
   "last_name": "das Neves",
   "birthday": "1991-09-91",
   "username": "joao_das_neves",
   "user_id": "70c881d4a26984ddce795f6f71817c9cf4480e79"
  },
  {
   "first_name":"João",
   "last_name": "das Neves",
   "birthday": "1991-09-91",
   "username": "joao_das_neves",
   "user_id": "70c881d4a26984ddce795f6f71817c9cf4480e79"
  }
]
```

| Campo       | Tipo   |
|-------------|--------|
| first_name  | String |
| last_name   | String |
| birthday    | String |
| username    | String |

### POST `/account/card`
Esse método deve receber um cartão novo e inseri-lo em um banco de dados para ser consumido pela própria API.
```json
{
   "card_id": "70c881d4a26984ddce795f6f71817c9cf4480e79"
   "title": "Cartão 1",
   "pan": "5527952393064634",
   "expiry_mm": "03",
   "expiry_yyyy": "2022",
   "security_code": "656",
   "date":"26/11/2015"
}
```
| Campo       | Tipo   |
|-------------|--------|
| title       | String |
| pan         | String |
| expiry_mm   | String |
| expiry_yyy  | String |
| security_code | String |
| date        | String |


### GET `/account/cards`
Esse método da API deve retornar o seguinte JSON com os cartões cadastrados pelo usuário
```json
[
  {
    "title":"Cartão 1",
    "pan": "5527952393064634",
    "expiry_mm": "03",
    "expiry_yyyy": "2022",
    "security_code": "656",
    "date":"26/11/2015"
  },
  {
     "title":"Cartão 2",
     "pan": "5527952393064634",
     "expiry_mm": "03",
     "expiry_yyyy": "2022",
     "security_code": "656",
     "date":"26/11/2015"
  },
  {
     "title":"Cartão 2",
     "pan": "5527952393064634",
     "expiry_mm": "03",
     "expiry_yyyy": "2022",
     "security_code": "656",
     "date":"26/11/2015"
  }
]
```

| Campo       | Tipo   |
|-------------|--------|
| title       | String |
| pan         | String |
| expiry_mm   | String |
| expiry_yyy  | String |
| security_code | String |
| date        | String |



Após o usuário adicionar todos os cartões e localizar seus amigos, ele poderá realizar uma transferência.
Para isso, você precisará fazer o método `transfer` na sua API.

### POST `/account/transfer`
Esse método irá receber os dados da compra, junto com os dados do usuário.
```json
{
   "friend_id": "70c881d4a26984ddce795f6f71817c9cf4480e79",
   "total_to_transfer": 100,
   "billing_card": {
      "card_id": "70c881d4a26984ddce795f6f71817c9cf4480e79"
   }
}

```

+ Transfer

| Campo        | Tipo       |
|--------------|------------|
| friend_id    | String     |
| total_to_pay | int (in cents)|
| billing_card  | CreditCard |

+ BillingCard

| Campo            | Tipo   |
|------------------|--------|
| card_id          | String |


### GET `/account/bank-statement`
Esse método deve retornar todas as transferencias realizadas entre os amigos na API
```json
[
   {
      "user_id":"70c881d4a26984ddce795f6f71817c9cf4480e79",
      "friend_id":"70c881d4a26984ddce795f6f71817c9cf4480e79",
      "value":1234,
      "date":"19/08/2016",
      "from_card":"70c881d4a26984ddce795f6f71817c9cf4480e79"
   },
   {
      "user_id":"70c881d4a26984ddce795f6f71817c9cf4480e79",
      "friend_id":"70c881d4a26984ddce795f6f71817c9cf4480e79",
      "value":1234,
      "date":"19/08/2016",
      "from_card":"70c881d4a26984ddce795f6f71817c9cf4480e79"
   },
   {
      "user_id":"70c881d4a26984ddce795f6f71817c9cf4480e79",
      "friend_id":"70c881d4a26984ddce795f6f71817c9cf4480e79",
      "value":1234,
      "date":"19/08/2016",
      "from_card":"70c881d4a26984ddce795f6f71817c9cf4480e79"
   },
]
```
| Campo            | Tipo   |
|------------------|--------|
| user_id          | String |
| friend_id        | String |
| value            | int (in cents)    |
| date             | String |
| from_card        | String |

### GET `/account/bank-statement/{usertId}`
Esse método deve retornar todos as transferencias realizadas na API por um usuário específico
```json
[
   {
      "user_id":"70c881d4a26984ddce795f6f71817c9cf4480e79",
      "friend_id":"70c881d4a26984ddce795f6f71817c9cf4480e79",
      "value":1234,
      "date":"19/08/2016",
      "from_card":"70c881d4a26984ddce795f6f71817c9cf4480e79"
   },
   {
      "user_id":"70c881d4a26984ddce795f6f71817c9cf4480e79",
      "friend_id":"70c881d4a26984ddce795f6f71817c9cf4480e79",
      "value":1234,
      "date":"19/08/2016",
      "from_card":"70c881d4a26984ddce795f6f71817c9cf4480e79"
   },
]
```




---
#### LICENSE
```
MIT License

Copyright (c) 2020 Lucree Soluções Inteligentes.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```


