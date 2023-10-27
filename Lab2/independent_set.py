from graph import * 
from experiments import generate_random_graph


"""
Checks that no two vertices in the subset form an edge in G
"""
def is_independent_set(G, subset):
    for start in G.adj: 
        for end in G.adj[start]:
            if(start in subset and end in subset):
                return False
    return True 

"""
Constructs the maximum independent set by iterating over the powerset of all nodes
to find the largest subset that satisfies the criteria for an independent set 
"""
def MIS(G):
    nodes = [i for i in range(G.number_of_nodes())]
    subsets = power_set(nodes)
    max_independent_set = set() 

    for subset in subsets:
        if is_independent_set(G, subset):
            if len(subset) > len(max_independent_set):
                max_independent_set = subset 

    return max_independent_set


"""
Tests the hypothesis that V-MIS is an MVC and vice versa. 
"""
def independent_set_experiment(V, E):

    graph = generate_random_graph(V, E)
    independent_set = MIS(graph)
    vertex_cover = MVC(graph)
    all_nodes = set([i for i in range(graph.number_of_nodes())])

    MIS_difference =  all_nodes.difference(independent_set)
    MVC_difference =  all_nodes.difference(vertex_cover)

    print('G=(V,E) Adjacency Lists: ')
    for i in range(graph.number_of_nodes()):
        print('\t', i, ': ', graph.adjacent_nodes(i))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('MVC of G: ', vertex_cover)
    print('MIS of G: ', independent_set)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('(V - MIS): ', MIS_difference,  (' is a vertex cover of G' if (is_vertex_cover(graph, MIS_difference))  else ' is not a vertex cover of G' )    )
    print('|V - MIS| = ' , len(MIS_difference), ' = |MVC| = ', len(vertex_cover), ' ∴ (V - MIS) is a miniml vertex cover of G' )
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('V - MVC: ', MVC_difference,  (' is an independent set of G' if (is_independent_set(graph, MVC_difference))  else ' is not an independent set of G' )    )
    print('|V - MVC| = ' , len(MVC_difference), ' = |MIS| = ', len(independent_set), ' ∴ (V - MVC) is a maximum independent set of G' )

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



independent_set_experiment(1,0)