# Pac-Man-AI
<img src="http://ai.berkeley.edu/projects/release/search/v1/001/maze.png" width="auto">

## Resume
Project created in python2 implementing an A.I. who plays Pac-Man using:
  - A* search algorithm;
  - Hill Climbing;
  - Simulated Annealing;
  - Uniform Cost;
  
 All this algorithms are used to control the character to finish the game.
 
 <img src="http://ai.berkeley.edu/images/pacman_game.gif" width="auto">
 
## Execution Commands (by terminal)

### Main Map (not used in the tests)
    - python2 pacman.py -p searchAgent -a fn=SEARCH_AGENT_NAME

### Others Test Maps
    - python2 pacman.py -l tinyMaze -p SearchAgent -a fn=SEARCH_AGENT_NAME
    - python2 pacman.py -l mediumMaze -p SearchAgent -a fn=SEARCH_AGENT_NAME
    - python2 pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=SEARCH_AGENT_NAME
    - python2 pacman.py -l tinyScaryMaze -p SearchAgent -a fn=SEARCH_AGENT_NAME
    - python2 pacman.py -l mediumScaryMaze -p SearchAgent -a fn=SEARCH_AGENT_NAME
    - python2 pacman.py -l bigScaryMaze -z .5 -p SearchAgent -a fn=SEARCH_AGENT_NAME

### Search Agent Names Avaliable
    - hcs = Hill Climbing Search
    - sas = simmulated Annealing Search
    - ucs = Uniform Cost Search
    - astar,heuristic=HEURISTICA_DESEJADA = A* Search

#### Heuristics Used
    - manhattanHeuristic = Manhattan Heuristic
    - foodHeuristic = Food Problem Heuristic
    
## Observation (in PT-BR)
    - Se a versão do seu python for menor que a 3.0, não é necessario a terminologia 2 após o comando de chamada do python.
