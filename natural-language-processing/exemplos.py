"""
Exemplos de Processamento de Linguagem Natural.

Fonte: https://github.com/andressa/clustering-defects/blob/ipython-notebook/notebooks/PoC.ipynb
"""
import nltk
from nltk.corpus import stopwords
"""
Carregando stopwords do NLTK

Stopwords é um conjunto de palavras, tais como "e", "que" ou "pois", que não possuem nenhum significado relevante em uma frase.
Trata-se portanto de conectores em textos.
É possível estender esta lista adicionando palavras que no contexto da aplicação também não possuam significado relevante.
"""
extended_stopwords = []
extended_stopwords.extend(stopwords.words('portuguese'))

"""
Aplicando tokenizing

Tokenize implica no processo de separar sentenças em uma lista de palavras. Neste processo, pode-se excluir pontuação,
ou não. Como queremos agrupar os incidentes em conjuntos, manter a pontuação não é relevante.
"""
import string

def get_tokens(text):
    lowers = text.lower()
    no_punctuation = lowers.translate(str.maketrans({key: None for key in string.punctuation}))
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens

"""
Aplicando steamming

Steamming consiste em reduzir palavras ao seu radical.
"""
from nltk.stem.snowball import *

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

"""
Pre-processando o texto. Um pre-processamento consiste em:

Obter palavras a partir das sentenças excluindo pontuação (tokenize)
Reduzir as palavras para os respectivos radicais (steamming)
"""
def clean_item(text):
    try:
        tokens = get_tokens(text)
    except AttributeError:
        print(text)
    filtered = [w for w in tokens if not w in extended_stopwords]
    stemmer = SnowballStemmer('portuguese')
    stemmed = stem_tokens(filtered, stemmer)
    return ' '.join(stemmed)


"""
Exemplo de processamento de texto.
"""
print(clean_item("As Memórias Póstumas de Brás Cubas são um romance? Macedo Soares, em carta que me escreveu por esse tempo, recordava amigamente as Viagens na minha terra. Ao primeiro respondia já o defunto Brás Cubas (como o leitor viu e verá no prólogo dele que vai adiante) que sim e que não, que era romance para uns e não o era para outros. "))
