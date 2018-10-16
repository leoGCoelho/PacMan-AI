# Comandos para Executar (via terminal):

## Mapa Principal (não usado nos testes):
    - python pacman.py -p searchAgent -a fn=NOME_DO_AGENTE_DE_BUSCA

## Outros Mapas Usados para Teste:
    - python pacman.py -l tinyMaze -p searchAgent -a fn=NOME_DO_AGENTE_DE_BUSCA
    - python pacman.py -l mediumMaze -p searchAgent -a fn=NOME_DO_AGENTE_DE_BUSCA
    - python pacman.py -l bigMaze -z .5 -p searchAgent -a fn=NOME_DO_AGENTE_DE_BUSCA
    - python pacman.py -l tinyScaryMaze -p searchAgent -a fn=NOME_DO_AGENTE_DE_BUSCA
    - python pacman.py -l mediumScaryMaze -p searchAgent -a fn=NOME_DO_AGENTE_DE_BUSCA
    - python pacman.py -l bigScaryMaze -z .5 -p searchAgent -a fn=NOME_DO_AGENTE_DE_BUSCA

## Nomes de Agentes de Busca Válidos:
    - hcs = Hill Climbing Search
    - sas = simmulated Annealing Search
    - ucs = Uniform Cost Search
    - astar,heuristic=HEURISTICA_DESEJADA = A* Search

## Heurísticas Usadas ao Algoritmo A*:
    - manhattanHeuristic = Heuristica de Manhattan
    - foodHeuristic = Heuristica para o Problema da Comida 
