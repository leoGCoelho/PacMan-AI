# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
from random import randrange

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).

  You do not need to change anything in this class, ever.
  """

  def getStartState(self):
     """
     Returns the start state for the search problem
     """
     util.raiseNotDefined()

  def isGoalState(self, state):
     """
       state: Search state

     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state

     For a given state, this should return a list of triples,
     (successor, action, stepCost), where 'successor' is a
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take

     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()


def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].

  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].

  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:

  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def uniformCostSearch(problem):
    # fila dos nodos, acoes(caminhos ou direcoes) e primeiro nodo((nodo, direcao, custo), caminho percorrido, custo do caminho)
    queue = util.PriorityQueue()
    action = []
    firstNode = ((problem.getStartState(), None, 0), [], 0)

    # coloca na fila um conjunto contendo o nodo e o caminho
    queue.push(firstNode, 0)
    while not queue.isEmpty():  # Enquanto a fila nao for vazia
        # retira o nodo atual da fila
        p = queue.pop()
        # inicializa variaveis auxiliares com os valores do nodo atual
        node = p[0][0]
        dir = p[0][1]
        mov = p[1]
        costUpdated = p[2]

        # se o nodo atual foi acessado, passa para o proximo
        if node in action:
            continue

        # senao, adiciona ele aos acessados
        action.append(node)

        # se o nodo for o nodo objetivo, retorna o caminho ate ele
        if problem.isGoalState(node):
            return mov

        # senao, vai para o proximo nodo
        next = problem.getSuccessors(node)
        listN = list(next)
        cost = problem.getCostOfActions(mov) # custo ate o momento

        for x in listN:
            if x[0] not in action: # se o proximo nodo nao foi acessado
                if problem.isGoalState(x[0]): # e eh o nodo objetivo, retorna o caminho ate ele
                    return mov+[x[1]]

                #senao, adiciona na fila o nodo atual e volta a verificar
                nextNode = (x, mov + [x[1]], x[2] + costUpdated)
                queue.push(nextNode, costUpdated + x[2])

    # se nao encontrou um caminho, retorna nada
    return []

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def hillClimbingSearch(problem, heuristic=nullHeuristic):
    # caminho ate o objetivo, variavel inicial(nodo), custo atual e custo do filho com valores iniciais e fila
    path = []
    node = ((problem.getStartState(), []), heuristic(problem.getStartState(), problem))
    cost = 1
    costSucc = 0
    queue = util.PriorityQueue()

    while cost > costSucc:     # Loop enquanto nao encontrar o menor caminho
        # custo atual = heuristica do nodo atual
        cost = heuristic(node, problem)

        # se o nodo atual for o nodo objetivo, retorna o caminho
        if problem.isGoalState(node):
            return path

        # senao
        next = problem.getSuccessors(node[0][0]) # proximo nodo

        for i in next:
            # atualiza valor do custo
            costUpdated = problem.getCostOfActions([i[1]]) + heuristic(i[0], problem)
            # coloca na fila infos do nodo
            queue.push((i[0], i[1]), costUpdated)

        nodeNext = queue.pop()  # proximo nodo recebe o que esta na fila
        costSucc = problem.getCostOfActions([nodeNext[1]]) + heuristic(nodeNext[0], problem) -1 # custo do filho
        path.append(nodeNext[1])    # nodo eh adicionado aos caminhos atuais
        node = ((nodeNext[0], nodeNext[1]), costSucc)

    return path # retorna o caminho atual


def simmulatedAnnealingSearch(problem, heuristic=nullHeuristic):
    # fila dos nodos, nodos expandidos e caminho ate o objetivo
    queue = util.PriorityQueue()
    exp = set()
    path = []

    # variaveis iniciais(nodo e custo)
    firstNode = problem.getStartState()
    cost = 0

    # coloca na fila um conjunto contendo o nodo, o caminho e o custo
    queue.push((firstNode, path, cost), heuristic(firstNode, problem))
    while not queue.isEmpty():  # Enquanto a fila nao for vazia
        # Cria uma variavel para guardar o pop feito na fila, e variaveis para o nodo, movimentos ate esse no e o custo ate o momento
        p = queue.pop()
        node = p[0]
        mov = p[1]
        costUpdated = p[2]

        # Se o nodo atual e o nodo objetivo, achou o objetivo e retorna os movimentos
        if problem.isGoalState(node):
            return mov

        # Se o nodo atual tive sido expandido, continua a procura no proximo
        if node in exp:
            continue

        # Parametros do proximo nodos
        exp.add(node)
        next = problem.getSuccessors(node)
        listN = list(next)

        # Procura pelo nodo seguinte ao atual e se ja foi expandido, continua para o proximo e assim sucessivamente
        for n in listN:
            if n[0] in exp:
                continue

            # Coloca no nodo da fila primeiro um conjunto contendo o nodo atual, o movimento ate ele e seu custo + custos anteriores
            # Depois um conjunto com o custo dele + a heuristica do nodo + os custos anteriores somados
            queue.push((n[0], mov+[n[1]], costUpdated+n[2]), heuristic(n[0], problem))

        # Se nao encontrou um caminho, retorna p melhor caminho achado
    return mov

def aStarSearch(problem, heuristic=nullHeuristic):
    # fila dos nodos, nodos expandidos e caminho ate o objetivo
    queue = util.PriorityQueue()
    exp = set()
    path = []

    # variaveis iniciais(nodo e custo)
    firstNode = problem.getStartState()
    cost = 0

    # coloca na fila um conjunto contendo o nodo, o caminho e o custo
    queue.push((firstNode, path, cost),0)
    while not queue.isEmpty():  # Enquanto a fila nao for vazia
        # Cria uma variavel para guardar o pop feito na fila, e variaveis para o nodo, movimentos ate esse no e o custo ate o momento
        p = queue.pop()
        node = p[0]
        mov = p[1]
        costUpdated = p[2]

        # Se o nodo atual eh o nodo objetivo, achou o objetivo e retorna os movimentos
        if problem.isGoalState(node):
            return mov

        # Se o nodo atual tive sido expandido, continua a procura no proximo
        if node in exp:
            continue

        # Parametros do proximo nodos
        exp.add(node)
        next = problem.getSuccessors(node)
        listN = list(next)

        # Procura pelo nodo seguinte ao atual e se ja foi expandido, continua para o proximo e assim sucessivamente
        for n in listN:
            if n[0] in exp:
                continue

            # Coloca no nodo da fila primeiro um conjunto contendo o nodo atual, o movimento ate ele e seu custo + custos anteriores
            # Depois um conjunto com o custo dele + a heuristica do nodo + os custos anteriores somados
            queue.push((n[0], mov+[n[1]], costUpdated+n[2]), costUpdated+n[2]+heuristic(n[0], problem))

    # Se nao encontrou um caminho, retorna nada
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
sas = simmulatedAnnealingSearch
hcs = hillClimbingSearch
