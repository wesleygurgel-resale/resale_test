import requests


class TestImoveis:
    headers = {'Authorization': 'Token d776c5b95f51ca8bef372ba9d0b3ba4515134cb9'}
    imoveis_url_base = 'https://resale-test-wg.herokuapp.com/api/v1/imoveis/'

    def test_get_imoveis(self):
        imoveis = requests.get(url=self.imoveis_url_base, headers=self.headers)

        assert imoveis.status_code == 200

    def test_get_imovel(self):
        imovel = requests.get(url=f'{self.imoveis_url_base}1/', headers=self.headers)

        assert imovel.status_code == 200

    def test_post_imovel(self):
        novo_imovel = {
            "imobiliaria": 1,
            "nome": "Terezinha Galvão IV",
            "endereco": "Av. Jucelino, 93, 5 e 6 bloco único - Condomínio Terezinha Galvão IV, Natal, RN, 59152-301",
            "tipo": 1,
            "finalidade": "Escritorio",
            "descricao": "Inscrição Prefeitura Oficial de Registro de Imóveis, Títulos e Documentos e Civil de Pessoa Jurídica de Natal. Valor avaliado R$200.773,78.",
            "caracteristica": "Área privativa 75,32m²",
            "ativo": True
        }

        response = requests.post(url=self.imoveis_url_base, headers=self.headers, data=novo_imovel)

        self.imovel_criado_post = response.json()['id']

        assert response.status_code == 201

        assert response.json()['nome'] == novo_imovel['nome']

    def test_put_imovel(self):
        atualizar_imovel = {
            "imobiliaria": 1,
            "nome": "Terezinha Galvão III",
            "endereco": "Av. Jucelino, 93, 5 e 6 bloco único - Condomínio Terezinha Galvão III, Natal, RN, 59152-301",
            "tipo": 1,
            "finalidade": "Residencial",
            "descricao": "Inscrição Prefeitura Oficial de Registro de Imóveis, Títulos e Documentos e Civil de Pessoa Jurídica de Natal. Valor avaliado R$200.773,78.",
            "caracteristica": "02 Dormitórios e 01 Banheiro",
            "ativo": True
        }

        response = requests.put(url=f'{self.imoveis_url_base}1/', headers=self.headers, data=atualizar_imovel)

        assert response.status_code == 200

        assert response.json()['nome'] == atualizar_imovel['nome']

    def test_delete_imovel(self):
        response = requests.delete(url=f'{self.imoveis_url_base}8/', headers=self.headers)

        assert response.status_code == 200
        assert len(response.text) == 0
