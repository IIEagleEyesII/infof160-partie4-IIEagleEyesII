from Timer import Minuterie
# main function for the Monte Carlo Tree Search
def monte_carlo_tree_search(racine):
    while not Minuterie().run():
        feuille = traverse(racine)
        result = rollout(feuille)
        retropropagation(feuille, result)
    return best_child(racine)

def traverse(node):
    while fully_expanded(node):
        node = best_uct(node)
    #si aucin enfant n'est present, le noeud est terminal
    return pick_unvisited(node.children) or node


# resultat de la simulation
def simulation(node):
    while non_terminal(node):
        node = rollout_policy(node)
    return result(node)

# fonction fqui choisis aleatoirement un fils noeud
def rollout_policy(node):
    return pick_random(node.children)


def retropropagation(node, result):
    if is_root(node) :
        return
    node.stats = update_stats(node, result)
    rétropropagation(node.parent)


# function for selecting the best child
# node with highest number of visits
#def best_child(node):
  #  pick child with highest number of visits

