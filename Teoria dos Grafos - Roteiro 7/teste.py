from grafo_adj_nao_dir import *

g_1 = Grafo([], [])
for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g']:
    g_1.adicionaVertice(i)
for i in ['A-B', 'A-M', 'A-L', 'B-C', 'B-D', 'C-V', 'V-B', 'D-E', 'E-F', 'E-X', 'F-G', 'G-g', 'G-H', 'H-I', 'I-J',
          'J-K', 'J-a', 'K-a', 'M-N', 'N-W', 'N-V', 'N-P', 'V-W', 'W-D', 'W-U', 'U-Y', 'U-T', 'U-X', 'X-Y', 'X-c',
          'c-d', 'c-b', 'd-e', 'd-J', 'e-X', 'Y-Z', 'Y-F', 'Z-e', 'Z-f', 'Z-g', 'L-M', 'L-O', 'O-N', 'O-Q', 'Q-S',
          'S-T', 'T-X', 'P-R', 'R-X']:
    g_1.adicionaAresta(i)

print(g_1.dijkstra('A', 'a', ['Q', 'X', 'G', 'I', 'J'], 3,4))

g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
# {'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'}
g_p.adicionaAresta('J-C')
g_p.adicionaAresta('C-E')
g_p.adicionaAresta('C-E')
g_p.adicionaAresta('C-P')
g_p.adicionaAresta('C-P')
g_p.adicionaAresta('C-M')
g_p.adicionaAresta('C-T')
g_p.adicionaAresta('M-T')
g_p.adicionaAresta('T-Z')

print(g_p.dijkstra('J', 'Z', ['M'], 2,2))
