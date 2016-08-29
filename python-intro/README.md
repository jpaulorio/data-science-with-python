## Instalação
A maneira mais simples de instalar um ambiente Python pronto para uso em análise de dados é instalar uma _distribuição_ que contenha o 
interpretador Python e as bibliotecas necessárias. Duas das distribuições mais conhecidas são a [Anaconda](https://www.continuum.io) e 
a [Enthought](https://www.enthought.com/). Nesse tutorial, usaremos Anaconda devido à sua licença permissiva para uso comercial:

1. Baixe o instalador do Anaconda para o seu sistema operacional [aqui](https://www.continuum.io/downloads) e siga as instruções de instalação. Lembre-se de escolher o instalador contendo a versão 3.x.x do Python;
2. Siga as instruções do instalador após baixá-lo;
3. Teste sua instalação abrindo um terminal e digitando `python --version`. Se a saída for algo como

  ```
  Python 3.x.x :: Anaconda x.x.x (x86_64)
  ```
  
  isso indica que o Anaconda foi instalado corretamente.
  
## Hello world
Para executar um código Python, invoque o interpretador através do comando `python` e passe um arquivo de script como argumento. 
Por exemplo, para imprimir a string "Hello World!", crie um arquivo chamado `hello.py` com o conteúdo abaixo:
```python
print("Hello World!")
```

e execute o comando `python hello.py`. A string "Hello World!" deve ser exibida no terminal.

## Python básico
O arquivo *python_basics.py* contém exemplos básicos de uso da linguagem Python. Para mais detalhes da linguagem, os seguites recursos podem ser usados:

 * [Tutorial oficial de Python3(em inglês)](https://docs.python.org/3/tutorial/)
 * [Dive into Python3](http://www.diveintopython3.net/)

## Numpy
[Numpy](http://www.numpy.org) é uma biblioteca otimizada para manipulação de vetores e matrizes em Python. Seu uso é bastante frequente em computação científica para se manipular dados e criar estruturas que são usadas por outras bibliotecas para processamento de informações.

O arquivo *numpy_examples.py* possui exemplos de operações que costumam ser realizadas quando se trabalha com Numpy. Para mais detalhes a respeito do uso da biblioteca, pode-se consultar os links abaixo:

* [Numpy quickstart tutorial](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html)
* [CS321n Numpy tutorial](https://cs231n.github.io/python-numpy-tutorial/)
