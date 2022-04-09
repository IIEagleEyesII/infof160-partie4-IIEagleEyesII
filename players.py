from abc import ABCMeta, abstractmethod
from random import choice

from const import *
from move import Move

class Player(metaclass=ABCMeta):
    '''
    Classe abstraite (ne peut pas être instanciée) représentant un joueur générique.

    Args:
        player_id (int): PLAYER1 ou PLAYER2
        board (Board): plateau sur lequel jouer
    '''
    def __init__(self, player_id, board):
        self.player_id_ = player_id
        self.board_ = board

    def play(self):
        '''
        Demande au joueur de choisir et son coup et de l'effectuer sur le plateau.
        '''
        move = self._play()
        assert isinstance(move, Move)
        self.board_.move(move)

    @abstractmethod
    def _play(self):
        '''
        Choisit le coup à jouer.

        Returns:
            Move: le coup que le joueur va effectuer.
        '''
        pass

class AiPlayer(Player):
    '''
    Classe abstraite représentant un joueur AI.
    '''
    def __init__(self, player_id, board):
        super().__init__(player_id, board)

class RandomAiPlayer(AiPlayer):
    '''
    Joueur AI jouant au hasard parmi tous les coups disponibles.
    '''
    def __init__(self, player_id, board):
        super().__init__(player_id, board)

    def _play(self):
        return choice(self.board_.possible_moves(self.player_id_))

class GreedyAiPlayer(AiPlayer):
    '''
    Joueur AI glouton : joue toujours un coup lui permettant possiblement d'atteindre
    la ligne d'arrivée en le moins de mouvements possibles.

    Attribute:
        winning_row (int): indice de la ligne à atteindre pour gagner
    '''
    def __init__(self, player_id, board):
        super().__init__(player_id, board)
        self.winning_row = 0 if player_id == PLAYER1 else board.m

    def _play(self):
        source = self.find_best_peg()
        return choice(
            list(self.board_.possible_moves_from_source(source, self.player_id_))
        )

    def find_best_peg(self):
        '''
        Détermine le pion à déplacer.

        Returns:
            Pos2D: position du pion à jouer.
        '''
        pegs = self.board_.pegs[self.player_id_-1]
        best_peg = None
        best_distance = POS_INF
        for peg in pegs:
            current_distance = abs(peg.y - self.winning_row)
            if current_distance < best_distance:
                best_peg = peg
                best_distance = current_distance
            elif current_distance == best_distance and peg.x < best_peg.x:
                best_peg = peg
        return best_peg

class MinimaxAiPlayer(AiPlayer):
    '''
    Joueur IA appliquant l'algorithme minimax.
    '''
    DEPTH = 3

    def __init__(self, player_id, board):
        super().__init__(player_id, board)

    def _play(self):
        move, _ = self.minimax(MinimaxAiPlayer.DEPTH)
        return move

    def minimax(self, depth, maximizing=True):
        '''
        Implémentation de l'algorithme minimax.

        Args:
            depth (int): le nombre de "couches" restantes à parcourir
            maximizing (bool): True si le coup à chercher à cette étape
                               vient du joueur `self.player_id`
        Returns:
            Tuple[Move,int]: paire contenant le meilleur coup et le score associé
        '''
        winner = self.board_.winner  # pour vérifier si l'état est final
        if winner is not None:  # s'il l'est, on calcule le score associé
            score = WIN+depth if winner == self.player_id_ else LOSS-depth
            return None, score
        # sinon on regarde si on est sur une feuille ou si on continue d'explorer
        if depth == 0:  # si feuille, on renvoie le score d'un état non final
            return None, DRAW
        current_player = self.player_id_
        other_player = (PLAYER1+PLAYER2)-current_player
        if not maximizing:
            current_player, other_player = other_player, current_player
        # ici current_player et other_player représentent respectivement
        # le joueur qui va effectuer le coup *à cette étape-ci* et le
        # joueur adverse
        best_moves = []
        best_reward = NEG_INF if maximizing else POS_INF  # l. 5
        possible_moves = self.board_.possible_moves(current_player)
        # S'il n'y a aucun coup jouable, on considère que l'autre joueur déclare forfait
        if not possible_moves:
            return None, WIN+depth if current_player == other_player else LOSS-depth
        for move in possible_moves:  #                           l. 6
            self.board_.move(move)  #                            l. 7
            _, reward = self.minimax(depth-1, not maximizing)  # l. 8
            self.board_.undo()  #                                l. 9
            if reward == best_reward:  #                         l. 13
                best_moves.append(move)  #                       l. 14
            elif (maximizing and (reward > best_reward)) or \
                 (not maximizing and (reward < best_reward)):  # l. 10
                best_moves = [move]  #                           l. 12
                best_reward = reward  #                          l. 11
        return choice(best_moves), best_reward  #                l. 17

############### Joueur Humain ###############

class PegPicker:
    '''
    Représentation interne des pions d'un joueur humain pour le I/O de sélection.

    Args:
        height (int): nombre de lignes du plateau
        pegs (PegsList): pions du joueur

    Attributes:
        current (Pos2D): position du choix actuel
    '''
    def __init__(self, height, pegs):
        self.pegs_ = [list() for y in range(height)]
        for peg in pegs:
            self.pegs_[peg.y].append(peg)
        # Remarque : sorted(peg_row) va renvoyer une liste triée, ce qui implique
        # une relation d'ordre sur les éléments dans peg_row, i.e. sur des Pos2D.
        # C'est pour cela que la méthode spéciale __lt__ (surcharge de l'opérateur <)
        # est définie dans Pos2D.
        self.pegs_ = [sorted(peg_row) for peg_row in self.pegs_ if peg_row]
        self.row_idx_ = 0
        self.peg_idx_ = 0

    @property
    def current(self):
        return self.pegs_[self.row_idx_][self.peg_idx_]

    def left(self):
        '''
        Passe au premier pion disponible à gauche (et cycle en revenant à droite
        si nécessaire).
        '''
        self.peg_idx_ = (self.peg_idx_-1) % len(self.pegs_[self.row_idx_])

    def right(self):
        '''
        Passe au premier pion disponible à droite (et cycle en revenant à gauche 
        si nécessaire).
        '''
        self.peg_idx_ = (self.peg_idx_+1) % len(self.pegs_[self.row_idx_])

    def up(self):
        '''
        Passe au premier pion disponible en haut (le plus proche du pion actuel)
        '''
        previous = self.current
        self.row_idx_ = (self.row_idx_-1) % len(self.pegs_)
        self._find_closest(previous)

    def down(self):
        '''
        Passe au premier pion disponible en bas (le plus proche du pion actuel)
        '''
        previous = self.current
        self.row_idx_ = (self.row_idx_+1) % len(self.pegs_)
        self._find_closest(previous)

    def _find_closest(self, target):
        '''
        Détermine le pion de la ligne actuelle le plus proche d'une position donnée.

        Args:
            target (Pos2D): position par rapport à laquelle on compare les distances
        '''
        self.peg_idx_ = PegPicker.argmin(
            [peg.dist_to(target, True) for peg in self.pegs_[self.row_idx_]]
        )

    @staticmethod
    def argmin(array):
        '''
        Détermine l'indice de la valeur minimale d'un tableau donné.

        Args:
            array (List[int/float]): tableau de valeurs numériques

        Returns:
            int: indice i s.t. array[i] <= array[j] pour tout j != i
        '''
        idx = 0
        min_value = None
        for i, value in enumerate(array):
            if min_value is None or value < min_value:
                min_value = value
                idx = i
        return idx

class HumanPlayer(Player):
    '''
    Joueur humain déterminant ses coups par des I/O.
    '''
    def __init__(self, player_id, board):
        super().__init__(player_id, board)

    def _play(self):
        idx = 0
        peg = self.select_peg()
        return self.select_move(peg)

    def select_peg(self):
        '''
        Choisit le pion à déplacer.

        Returns:
            Pos2D: position du pion à jouer
        '''
        peg_picker = PegPicker(
            self.board_.n,
            filter(
                self.board_.can_move_from,
                self.board_.pegs[self.player_id_-1]
            )
        )
        choice = None
        while choice != YES:
            self.board_.print(peg_picker.current)
            choice = input('Sélectionner ce pion ?\n'
                           '"y": oui, "j": <, "l": >, "i": ^, "k": v    ')
            if choice == LEFT:
                peg_picker.left()
            elif choice == RIGHT:
                peg_picker.right()
            elif choice == UP:
                peg_picker.up()
            elif choice == DOWN:
                peg_picker.down()
        return peg_picker.current

    def select_move(self, peg):
        '''
        Choisit où déplacer le pion sélectionné.

        Args:
            peg (Pos2D): position de départ du pion à déplacer

        Returns:
            Move: déplacement du pion
        '''
        possible_destinations = list(
            self.board_.possible_moves_from_source(
                peg, self.player_id_
            )
        )
        idx = 0
        choice = None
        while choice != YES:
            self.board_.print(possible_destinations[idx].dest)
            choice = input('Déplacer le pion ici ?\n'
                           '"y": oui, "j": <, "l": >    ')
            if choice == LEFT:
                idx -= 1
            elif choice == RIGHT:
                idx += 1
            idx %= len(possible_destinations)
        return possible_destinations[idx]


