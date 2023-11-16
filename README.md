#Notes: Heroku project is down. Need money :-/

# The concept behind this project
This API / Website was built based on the concept of [MKFBR](httpss://github.com/darkmathew/make_a_fake_brazilian) (Make a fake Brazilian). I recommend you take a look there, to find out more about the origin of things.

# Website Version

https://mkfbr-api.herokuapp.com/site/ 



# Api Usage


**API URL:** https://mkfbr-api.herokuapp.com/api/ 


**https Method:** GET 


**Response Format:** JSON


##  Simple Person Data
`GET https://mkfbr-api.herokuapp.com/api/`

Output Example
```
{
   "address":"Avenida Rondonópolis, s/n Edifício Boing",
   "age":39,
   "bairro":"Centro",
   "birthday":"05/03/1983",
   "city":"Nova Monte Verde",
   "cnpj":"",
   "cpf":"05291378522",
   "logradouro":"",
   "name":"Fausto Majewski Ferro",
   "rg":"446738760",
   "state":"Mato Grosso",
   "state_abbreviation":"MT"
}
```
## Get person with RG with punctuation
`GET https://mkfbr-api.herokuapp.com/api/custom/rg`

Output Example
```
{
   "address":"Rua Principal, s/n",
   "age":32,
   "bairro":"Centro",
   "birthday":"22/04/1990",
   "city":"Frei Paulo",
   "cnpj":"",
   "cpf":"66174944581",
   "logradouro":"",
   "name":"Raruama Neumann Rosa",
   "rg":"65.007.867-5",
   "state":"Sergipe",
   "state_abbreviation":"SE"
}
```
## Get person with CPF with punctuation
`GET https://mkfbr-api.herokuapp.com/api/custom/cpf`

Output Example
```
{
   "address":"Praça do Mercado, s/n",
   "age":24,
   "bairro":"Centro",
   "birthday":"18/09/1998",
   "city":"Itabaianinha",
   "cnpj":"",
   "cpf":"603.285.006-40",
   "logradouro":"",
   "name":"Risa Furtado Kassia",
   "rg":"407685707",
   "state":"Sergipe",
   "state_abbreviation":"SE"
}
```

## Get person with CNPJ with punctuation OR NOT.

 `GET https://mkfbr-api.herokuapp.com/api/custom/cnpj/null`  generate CNPJ without punctuation.

Output Example
```
{
   "address":"Avenida Adolf John Terry 1572",
   "age":52,
   "bairro":"Centro",
   "birthday":"26/04/1970",
   "city":"Corrente",
   "cnpj":"76645793000168",
   "cpf":"01873462913",
   "logradouro":"",
   "name":"Cajaty Callegario Morais",
   "rg":"533060745",
   "state":"Piauí",
   "state_abbreviation":"PI"
}
```

`GET https://mkfbr-api.herokuapp.com/api/custom/cnpj/points`  generate CNPJ with punctuation.

Output Example
```
{
   "address":"Rua Central, s/n",
   "age":25,
   "bairro":"Distrito de Lagoas",
   "birthday":"03/12/1997",
   "city":"Dormentes",
   "cnpj":"29.303.543/0001-60",
   "cpf":"09597577402",
   "logradouro":"",
   "name":"Ross Lourenco Lira",
   "rg":"070687358",
   "state":"Pernambuco",
   "state_abbreviation":"PE"
}
```



## Get person with CPF, RG and CNPJ with punctuation 
`GET https://mkfbr-api.herokuapp.com/api/full`

Output Example
```
{
   "address":"Rua Luis Teixeira Costa 181",
   "age":98,
   "bairro":"Centro",
   "birthday":"12/05/1924",
   "city":"Cajueiro",
   "cnpj":"70.247.176/0001-28",
   "cpf":"053.212.764-12",
   "logradouro":"",
   "name":"Donatelo Monroe Forwille",
   "rg":"65.051.610-9",
   "state":"Alagoas",
   "state_abbreviation":"AL"
}
```

## Get a full customized person
`GET https://mkfbr-api.herokuapp.com/api/custom/all/<cpf_mode>/<cnpj_mode>/<gen_cnpj>/<rg_mode>/<gender_name>`

`cpf_mode` , `cnpj_mode`, `rg_mode`   - Set to "points" to get a punctuated value, or enter anything to generate a non-punctuated value.

`gen_cnpj` - true or yes or sim or s or si, that you can generate a CNPJ. Any other value will not generate the CNPJ.

`gender_name` - Set it to "R" for random gender, or "F" for female gender or "M" for male gender names.

Final Example: `GET https://mkfbr-api.herokuapp.com/api/custom/all/points/points/true/points/F`

Output Example: 
```
{
   "address":"Avenida Amazonas 135",
   "age":98,
   "bairro":"Centro",
   "birthday":"26/04/1924",
   "city":"Eldorado dos Carajás",
   "cnpj":"99.933.064/0001-02",
   "cpf":"087.713.356-50",
   "logradouro":"",
   "name":"Ametista Quinzeiro Nunes",
   "rg":"17.601.762-3",
   "state":"Pará",
   "state_abbreviation":"PA"
}
```
