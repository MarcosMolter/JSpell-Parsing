# JSpell-Parsing

JSpell Parsing é uma biblioteca que implementa o dicionário  [JSpell](http://natura.di.uminho.pt/wiki/doku.php?id=ferramentas:jspell "JSpell") para linguagem de programação [Python](https://www.python.org/ "Python").
O Jspell é um analisador morfológico derivado do corrector ortográfico ispell. (jspell = ispell++). 
O seu principal desenvolvimento tem sido com vista à sua utilização para a língua portuguesa. 
No entanto, existem dicionários para outras línguas.

Em [Python](https://www.python.org/ "Python") pode ser utilizado como dicionário, correção ortográfica e em associado à biblioteca [NLTK](http://www.nltk.org/ "NLTK")
apresenta-se como estrutura para analise textual, lemmatizing, tokenize e stem

***
##Instalação

Utilize um programa de gerenciamento de repositório para instanciar um clone deste [Link](https://github.com/MarcosMolter/JSpell-Parsing "JSpell-Parsing") para a pasta \<path\>\Python27\Lib\site-packages ou acesse diretamente o repositório https://github.com/MarcosMolter/JSpell-Parsing para donwload

##Utilização
<code> import jspellparsing </code>
##Exemplos
<pre>
  <code>
        jspell = jspellparsing.jspell
        linhas = jspell.load_data('aff')
        rules_obj = jspell.rules_dict(linhas)       
        linhas = jspell.load_data('dic')
        dict_obj = jspell.jspell_dict(linhas) 
  </code>
</pre>  
