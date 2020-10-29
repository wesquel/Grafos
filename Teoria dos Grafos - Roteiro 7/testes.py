from grafo_test import Grafo


g_1 = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])

g_1.adicionaAresta('A-B')
g_1.adicionaAresta('B-C')
g_1.adicionaAresta('C-D')
g_1.adicionaAresta('D-E')
g_1.adicionaAresta('E-F')
g_1.adicionaAresta('F-G')
g_1.adicionaAresta('G-E')
g_1.adicionaAresta('E-C')
g_1.adicionaAresta('C-A')

g_2 = Grafo(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

g_2.adicionaAresta('1-2')
g_2.adicionaAresta('1-5')
g_2.adicionaAresta('1-4')
g_2.adicionaAresta('4-5')
g_2.adicionaAresta('5-2')
g_2.adicionaAresta('2-3')
g_2.adicionaAresta('3-9')
g_2.adicionaAresta('6-8')
g_2.adicionaAresta('8-7')
g_2.adicionaAresta('7-6')

g_3 = Grafo(['A', 'B', 'C', 'D', 'E', 'F'])

g_3.adicionaAresta('A-B')
g_3.adicionaAresta('A-C')
g_3.adicionaAresta('B-D')
g_3.adicionaAresta('B-E')
g_3.adicionaAresta('C-E')
g_3.adicionaAresta('C-F')
g_3.adicionaAresta('D-E')
g_3.adicionaAresta('E-F')
g_3.adicionaAresta('B-C')

g_4 = Grafo(['A', 'B', 'C', 'D', 'E', 'F'])

g_4.adicionaAresta('A-D')
g_4.adicionaAresta('A-B')
g_4.adicionaAresta('C-A')
g_4.adicionaAresta('C-F')
g_4.adicionaAresta('C-D')
g_4.adicionaAresta('D-F')
g_4.adicionaAresta('B-D')
g_4.adicionaAresta('E-A')
g_4.adicionaAresta('E-C')

g_5 = Grafo(['A', 'B', 'C', 'D', 'E'])


g_5.adicionaAresta('A-B')
g_5.adicionaAresta('A-C')
g_5.adicionaAresta('A-D')
g_5.adicionaAresta('C-D')
g_5.adicionaAresta('B-D')
g_5.adicionaAresta('B-E')
g_5.adicionaAresta('D-E')

g_6 = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
g_6.adicionaAresta('J-C')
g_6.adicionaAresta('C-E')
g_6.adicionaAresta('C-E')
g_6.adicionaAresta('C-P')
g_6.adicionaAresta('C-P')
g_6.adicionaAresta('C-M')
g_6.adicionaAresta('C-T')
g_6.adicionaAresta('M-T')
g_6.adicionaAresta('T-Z')


#print(g_1.fleury())
#print(g_2.fleury())
#print(g_3.fleury())
#print(g_4.fleury())
#print(g_5.fleury())
#print(g_6.fleury())

g_7 = Grafo(['A', 'B', 'C', 'D', 'E'])

g_7.adicionaAresta('A-B')
g_7.adicionaAresta('A-C')
g_7.adicionaAresta('A-D')
g_7.adicionaAresta('B-D')
g_7.adicionaAresta('D-C')
g_7.adicionaAresta('B-E')
g_7.adicionaAresta('C-E')

#print(g_1.ciclo_hamiltoniano())
#print(g_2.ciclo_hamiltoniano())
#print(g_3.ciclo_hamiltoniano())
#print(g_4.ciclo_hamiltoniano())
#print(g_5.ciclo_hamiltoniano())
#print(g_7.ciclo_hamiltoniano())

g_c = Grafo(['J', 'C', 'E', 'P'])
g_c.adicionaAresta('J-C')
g_c.adicionaAresta('J-E')
g_c.adicionaAresta('J-P')
g_c.adicionaAresta('C-E')
g_c.adicionaAresta('C-P')
g_c.adicionaAresta('E-P')

g_l1 = Grafo(['A', 'B', 'C', 'D'])
g_l1.adicionaAresta('A-A')
g_l1.adicionaAresta('A-A')
g_l1.adicionaAresta('B-A')

g_l2 = Grafo(['A', 'B', 'C', 'D'])
g_l2.adicionaAresta('A-B')
g_l2.adicionaAresta('B-B')
g_l2.adicionaAresta('B-A')

g_l3 = Grafo(['A', 'B', 'C', 'D'])
g_l3.adicionaAresta('C-A')
g_l3.adicionaAresta('C-C')
g_l3.adicionaAresta('D-D')


print(g_c.ciclo_hamiltoniano())
print(g_l1.ciclo_hamiltoniano())
print(g_l2.ciclo_hamiltoniano())
print(g_l3.ciclo_hamiltoniano())


