# Imobiliaria API - Resale (Processo Seletivo)

Backend de uma aplicação web criada usando Django Rest Framework como parte de um teste.

___
## Código

#### Models - Criei dois models a mais do que os especificados nos objetivos.

O model **Base** com a finalidade de um melhor controle sobre os dados, realiza a função de guardar as datas em que os Models foram criados e também a data que foram  atualizados pela última vez. 
```py

class Base(models.Model):
    """
    Model Base para criação dos demais.
    """
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
```

O model **Tipo**, analisando a página da própria **[Resale](https://resale.com.br/busca)** percebi que alguns campos como *Finalidade e Tipo de Imóvel* são utilizados para Filtragem. 

```py

class Tipo(models.Model):
    """
    Model que define o Tipo de Imóvel.
    """
    tipo = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Tipo de Imóvel"
        verbose_name_plural = "Tipos de Imóveis"
        ordering = ['id']

    def __str__(self):
        return self.tipo
        
```

Então tomei a liberdade de criar um Model para **Tipo** para que eu pudesse utilizar de forma mais clara como método de Filtragem.

**OBS**: Deixei o campo **Finalidade** na `class Imovel(Base):` como um VARCHAR usando *choices* para ter as duas formas.
```py
finalidade = models.CharField(null=True, max_length=255, choices=FINALIDADE_IMOVEL)       
```

#### Serializers
Para `ImobiliariaSerializer`criei um campo `propriedades = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='imovel-detail')` que retorna na uma lista contendo todas as propriedades relacionadas a aquela Imobiliária.

Para `ImovelSerializer` existe uma função de validação para descrição. ```def validate_descricao(self, descricao):```

#### Views
Views criadas usando `viewSets` e detalhe para a view de **Imobiliaria** onde criei uma `action` que ao acessar determinada Imobiliaria pela URL, temos a opção de listar todos os imóveis da mesma.
```py
@action(detail=True, methods=['GET'])
    def listar_imoveis(self, request: HttpRequest, pk=None):
```
___
### URL's
A API pode ser acessada através desse **[link](https://resale-test-wg.herokuapp.com/)**, onde caimos em uma página "ROOT" para acessarmos as Views.

#### Imobiliarias URL
##### Filtros
O filtro disponível para Imobiliaria é apenas o de Nome.

##### Acessando Imobiliarias Específicas
Para acessar uma Imobiliaria específica basta passarmos o ID da mesma como parâmetro na URL.

`https://resale-test-wg.herokuapp.com/api/v1/imobiliarias/{id}`

##### Acessando Imóveis de Imobiliarias
Podemos visualizar os Imóveis de duas formas:
- URL: `https://resale-test-wg.herokuapp.com/api/v1/imobiliarias/1/listar_imoveis/` - Isso para a Imobiliaria com ID = 1.
- Botão Extra Actions ao lado de Filtros

#### Imóveis URL
##### Filtros
Para Imóveis temos três tipos de Filtros:
- Nome
- Tipo
- Imobiliaria

#### Acessando Imóveis Específicos
Para acessar um Imóvel específico basta passarmos o ID do mesmo como parâmetro na URL.

`https://resale-test-wg.herokuapp.com/api/v1/imoveis/{id}`
___
### Banco de Dados (PostgreSQL)
Atualmente existem duas instâncias de Databases, uma que eu rodo localmente em minha máquina para testar as coisas e outra que está sendo usada em **Deploy** no **[Heroku](https://resale-test-wg.herokuapp.com/)**.

![image](https://user-images.githubusercontent.com/39765254/130641673-97f31805-9649-4595-a3a4-3763e9e4e779.png)

Caso tenham interesse em acessar o DB que está rodando em Produção:
```
Host: ec2-3-214-136-47.compute-1.amazonaws.com
Database: d3gr05t7sebgmn
User: jzpyfpeafhcowa
Port: 5432
Password: 2af7c8f95abab44a46f309309cc6cec6b5bcf1cac8cb95f82e40b924efaba3a4
```

___
### Propriedades do Django REST Framework
#### Habilitei duas formas de autenticação:
- Token
- Session

#### As permissões para métodos diferente do 'GET' estão desabilitadas para usúarios que não são autenticados.
#### Configurações sobre Schema e Paginação.

```py
# DRF
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2
}
```

___
### Documentação
Você pode checar a **documentação** em **[/docs/](https://resale-test-wg.herokuapp.com/docs/)**

___
### Como realizar Login para obter permissões
Através da **[URL](https://resale-test-wg.herokuapp.com/admin/)** ou através do próprio botão de Login na página da API.

O token para uso através de plataformas como o Insomnia ou PostMan, pode ser encontrado no **[/admin/](https://resale-test-wg.herokuapp.com/admin/authtoken/tokenproxy/)**

#### Conta
```
Usuario = rafael
Senha = 123456
```

___
## Formas de Contato
- ![icons8-whatsapp-24](https://user-images.githubusercontent.com/39765254/130647237-2f0245b8-6360-496a-921a-6eab2da175e2.png) **[(84) 98861-4565](https://api.whatsapp.com/send?phone=5584988614565)**

- ![icons8-aplicação-telegrama-24](https://user-images.githubusercontent.com/39765254/130647892-8b5f4855-2d98-41ae-8e5f-f412e631c238.png)  **https://t.me/wesleygurgel**

- ![icons8-gmail-24](https://user-images.githubusercontent.com/39765254/130647628-2bcb6945-f467-4e46-a991-8e9e313213f8.png)  **wesleygurgel27@gmail.com**



___
## Tecnologias usada

### API Rest
![Django Logo in a shields.io badge with "Django Rest" label](https://img.shields.io/badge/Django%20Rest-gray.svg?logo=django&style=for-the-badge&color=092E20&logoColor=white)

### Database
![PostgreSQL Logo in a shields.io badge](https://img.shields.io/badge/PostgreSQL-gray.svg?logo=postgresql&style=for-the-badge&color=4169E1&logoColor=white)

### Deployed
[![Heroky Logo in a shields.io badge](https://img.shields.io/badge/Heroku-gray.svg?logo=heroku&style=for-the-badge&color=430098&logoColor=white)](hhttps://product-stock-manager.herokuapp.com/api/)
