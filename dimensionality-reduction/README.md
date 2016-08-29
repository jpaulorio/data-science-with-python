# Redução de dimensionalidade

Diversos algoritmos de aprendizado de máquina sofrem com um fenômeno bastante conhecido como maldição da dimensionalidade [1] [2]. Em linhas gerais, dado um número fixo de amostras de treino, o poder preditivo de um algoritmo de aprendizado de máquina piora conforme a quantidade de atributos - *a dimensionalidade* - da base de dados aumenta. Em termos computacionais, o aumento de atributos faz com que os algoritmos tenham que processar um volume de dados muito maior.

Para resolver este problema, existem diversas técnicas para realizar a redução de dimensionalidade de uma base de dados [3]. Uma das técnicas mais conhecidas é a *Principal Component Analysis* (PCA).

O PCA é capaz de extrair as informações mais importantes de uma base de dados e realizar uma compressão, mantendo apenas essas informações importantes.

Essa compressão e redução do hiperespaço de atributos possui diversas aplicações, dentre as quais:
* economia de espaço para armazenamento
* redução de tempo para transmissão
* redução da influência de ruídos ou outliers
* **visualização dos dados (3D, 2D)**
* **aceleração do aprendizado dos algoritmos de AM**

É importante ressaltar, no entanto, que a redução de dimensionalidade pode prejudicar o desempenho dos algoritmos de aprendizado de máquina e, além disso, uma base de dados comprimida não poderá ser totalmente projetada/recuperada para a base de dados original.

-----

O script `plot_digits_pipe.py` [4] demonstra a utilização do PCA para reduzir a dimensionalidade da base de dados `digits`. A base de dados possui originalmente 64 atributos e foi testada aplicando PCA e regressão logística. O número de atributos foi ajustado com *grid search*, utlizando 20, 40 e 64 atributos. A base comprimida com 40 atributos obteve resultados superiores.

-----

[1] https://en.wikipedia.org/wiki/Curse_of_dimensionality

[2] https://stats.stackexchange.com/questions/169156/explain-curse-of-dimensionality-to-a-child

[3] https://mineracaodedados.wordpress.com/2015/06/13/7-tecnicas-para-reducao-da-dimensionalidade/

[4] http://scikit-learn.org/stable/auto_examples/plot_digits_pipe.html
