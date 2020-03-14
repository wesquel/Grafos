## Dupla (Weslley Addson e Filipe Miranda)
from grafo import Grafo
from Casos import TestGrafo
g = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'})

print(g.vertices_nao_adjacentes())
print(g.ha_laco())
print(g.ha_paralelas())
print(g.grau("C"))
print(g.arestas_sobre_vertice("C"))
print(g.eh_completo())



