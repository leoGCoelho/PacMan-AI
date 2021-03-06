# Pac-Man-AI
#### pt/BR | <a href="https://github.com/leoGCoelho/PacMan-AI/blob/master/README.md">en/US</a>
<img src="http://ai.berkeley.edu/projects/release/search/v1/001/maze.png" width="auto">

## Resumo
Projeto criado em python2 implementando um A.I. que desempenha Pac-Man usando:
   - Algoritmo A*;
   - Subida de Encosta;
   - Têmpera Simulada;
   - Custo Uniforme;
  
 Esses algoritmos serão usados para controlar o personagem até o fim do jogo.
 
 <img src="http://ai.berkeley.edu/images/pacman_game.gif" width="auto">
 
## Comandos de Execução (pelo terminal)

### Mapa Principal (não utilizado nos testes)
    - python2 pacman.py -p searchAgent -a fn=NOME_DO_AGENTE

### Outros Mapas de Teste
    - python2 pacman.py -l tinyMaze -p SearchAgent -a fn=NOME_DO_AGENTE
    - python2 pacman.py -l mediumMaze -p SearchAgent -a fn=NOME_DO_AGENTE
    - python2 pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=NOME_DO_AGENTE
    - python2 pacman.py -l tinyScaryMaze -p SearchAgent -a fn=NOME_DO_AGENTE
    - python2 pacman.py -l mediumScaryMaze -p SearchAgent -a fn=NOME_DO_AGENTE
    - python2 pacman.py -l bigScaryMaze -z .5 -p SearchAgent -a fn=NOME_DO_AGENTE

### Nomes dos Agentes de Busca Disponíveis
    - hcs = Subida de Encosta
    - sas = Têmpera Simulada
    - ucs = Custo Uniforme
    - astar,heuristic=HEURISTICA_DESEJADA = Busca A*

#### Heurísticas Usadas
    - manhattanHeuristic = Heurística Manhattan
    - foodHeuristic = Food Problem Heuristic
    
## Observações (em PT-BR)
    - Se a versão do seu python for menor que a 3.0, não é necessario a terminologia 2 após o comando de chamada do python.
