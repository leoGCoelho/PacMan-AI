# Comandos para Executar (via terminal)

## Mapa Principal (não usado nos testes)
    - python2 pacman.py -p searchAgent -a fn=NOME_DO_AGENTE_DE_BUSCA

## Outros Mapas Usados para Teste
    - python2 pacman.py -l tinyMaze -p searchAgent -a fn=NOME_DO_AGENTE_DE_BUSCA
    - python2 pacman.py -l mediumMaze -p searchAgent -a fn=NOME_DO_AGENTE_DE_BUSCA
    - python2 pacman.py -l bigMaze -z .5 -p searchAgent -a fn=NOME_DO_AGENTE_DE_BUSCA
    - python2 pacman.py -l tinyScaryMaze -p searchAgent -a fn=NOME_DO_AGENTE_DE_BUSCA
    - python2 pacman.py -l mediumScaryMaze -p searchAgent -a fn=NOME_DO_AGENTE_DE_BUSCA
    - python2 pacman.py -l bigScaryMaze -z .5 -p searchAgent -a fn=NOME_DO_AGENTE_DE_BUSCA

## Nomes de Agentes de Busca Válidos
    - hcs = Hill Climbing Search
    - sas = simmulated Annealing Search
    - ucs = Uniform Cost Search
    - astar,heuristic=HEURISTICA_DESEJADA = A* Search

###     Heurísticas Usadas ao Algoritmo A*
    - manhattanHeuristic = Heuristica de Manhattan
    - foodHeuristic = Heuristica para o Problema da Comida
    
### Observação:
    - Se a versão do seu python for menorm que a 3.0, não é necessario a terminologia 2 após o comando de chamada do python.
