# TIR (TAXA INTERNA DE RETORNO)

## Instruções de instalação:

Digite no seu terminal o seguinte comando para iniciar o GIT:
```
git init
```

Após a inicialização do GIT, clone o repositório com o seguinte comando:
```
git clone https://github.com/jasonrosa92/TIR-Ulend
```

Após o clone da aplicação, para criar sua variável de ambiente digite o comando:
(lembre se de estar no diretório correto)
```
python3 -m venv (nomedavariavel)
```
Logo após a criação, digite o seguinde código para ativar:
(Se você estiver usando linux)
```
source (nomedavariavel)/bin/activate
```
Com a sua variável de ambiente ativa, vamos instalar as bibliotecas necessárias para aplicação com o seguinte comando:
```
pip install -r requirements.txt
```
Após as instalações rode o seguinte comando para exibir todos os dados da aplicação:
```
streamlit run tir_app.py
```
