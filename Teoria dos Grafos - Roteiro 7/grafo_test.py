import unittest
from grafo_adj_nao_dir import Grafo


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        # {'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'}
        self.g_p.adicionaAresta('J-C')
        self.g_p.adicionaAresta('C-E')
        self.g_p.adicionaAresta('C-E')
        self.g_p.adicionaAresta('C-P')
        self.g_p.adicionaAresta('C-P')
        self.g_p.adicionaAresta('C-M')
        self.g_p.adicionaAresta('C-T')
        self.g_p.adicionaAresta('M-T')
        self.g_p.adicionaAresta('T-Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('J-C')
        self.g_p_sem_paralelas.adicionaAresta('C-E')
        self.g_p_sem_paralelas.adicionaAresta('C-P')
        self.g_p_sem_paralelas.adicionaAresta('C-M')
        self.g_p_sem_paralelas.adicionaAresta('C-T')
        self.g_p_sem_paralelas.adicionaAresta('M-T')
        self.g_p_sem_paralelas.adicionaAresta('T-Z')

        # Grafos completos
        # self.g_c = Grafo(['J', 'C', 'E', 'P'], {'a1':'J-C', 'a3':'J-E', 'a4':'J-P', 'a6':'C-E', 'a7':'C-P', 'a8':'E-P'})
        self.g_c = Grafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('J-C')
        self.g_c.adicionaAresta('J-E')
        self.g_c.adicionaAresta('J-P')
        self.g_c.adicionaAresta('C-E')
        self.g_c.adicionaAresta('C-P')
        self.g_c.adicionaAresta('E-P')

        self.g_c3 = Grafo(['J'])

        # Grafos com laco
        # self.g_l1 = Grafo(['A', 'B', 'C', 'D'], {'a1':'A-A', 'a2':'B-A', 'a3':'A-A'})
        self.g_l1 = Grafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('A-A')
        self.g_l1.adicionaAresta('A-A')
        self.g_l1.adicionaAresta('B-A')

        # self.g_l2 = Grafo(['A', 'B', 'C', 'D'], {'a1':'A-B', 'a2':'B-B', 'a3':'B-A'})
        self.g_l2 = Grafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('A-B')
        self.g_l2.adicionaAresta('B-B')
        self.g_l2.adicionaAresta('B-A')

        # self.g_l3 = Grafo(['A', 'B', 'C', 'D'], {'a1':'C-A', 'a2':'C-C', 'a3':'D-D'})
        self.g_l3 = Grafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('C-A')
        self.g_l3.adicionaAresta('C-C')
        self.g_l3.adicionaAresta('D-D')

        # self.g_l4 = Grafo(['D'], {'a2':'D-D'})
        self.g_l4 = Grafo(['D'])
        self.g_l4.adicionaAresta('D-D')

        # self.g_l5 = Grafo(['C', 'D'], {'a2':'D-C', 'a3':'C-C'})
        self.g_l5 = Grafo(['C', 'D'])
        self.g_l5.adicionaAresta('D-C')
        self.g_l5.adicionaAresta('C-C')

        # Grafos criados por nós

        self.g_1 = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])

        self.g_1.adicionaAresta('A-B')
        self.g_1.adicionaAresta('B-C')
        self.g_1.adicionaAresta('C-D')
        self.g_1.adicionaAresta('D-E')
        self.g_1.adicionaAresta('E-F')
        self.g_1.adicionaAresta('F-G')
        self.g_1.adicionaAresta('G-E')
        self.g_1.adicionaAresta('E-C')
        self.g_1.adicionaAresta('C-A')

        self.g_2 = Grafo(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

        self.g_2.adicionaAresta('1-2')
        self.g_2.adicionaAresta('1-5')
        self.g_2.adicionaAresta('1-4')
        self.g_2.adicionaAresta('4-5')
        self.g_2.adicionaAresta('5-2')
        self.g_2.adicionaAresta('2-3')
        self.g_2.adicionaAresta('3-9')
        self.g_2.adicionaAresta('6-8')
        self.g_2.adicionaAresta('8-7')
        self.g_2.adicionaAresta('7-6')

        self.g_3 = Grafo(['A', 'B', 'C', 'D', 'E', 'F'])

        self.g_3.adicionaAresta('A-B')
        self.g_3.adicionaAresta('A-C')
        self.g_3.adicionaAresta('B-D')
        self.g_3.adicionaAresta('B-E')
        self.g_3.adicionaAresta('C-E')
        self.g_3.adicionaAresta('C-F')
        self.g_3.adicionaAresta('D-E')
        self.g_3.adicionaAresta('E-F')
        self.g_3.adicionaAresta('B-C')

        self.g_4 = Grafo(['A', 'B', 'C', 'D', 'E', 'F'])

        self.g_4.adicionaAresta('A-D')
        self.g_4.adicionaAresta('A-B')
        self.g_4.adicionaAresta('C-A')
        self.g_4.adicionaAresta('C-F')
        self.g_4.adicionaAresta('C-D')
        self.g_4.adicionaAresta('D-F')
        self.g_4.adicionaAresta('B-D')
        self.g_4.adicionaAresta('E-A')
        self.g_4.adicionaAresta('E-C')

        self.g_5 = Grafo(['A', 'B', 'C', 'D', 'E'])

        self.g_5.adicionaAresta('A-B')
        self.g_5.adicionaAresta('A-C')
        self.g_5.adicionaAresta('A-D')
        self.g_5.adicionaAresta('C-D')
        self.g_5.adicionaAresta('B-D')
        self.g_5.adicionaAresta('B-E')
        self.g_5.adicionaAresta('D-E')

        self.g_7 = Grafo(['A', 'B', 'C', 'D', 'E'])

        self.g_7.adicionaAresta('A-B')
        self.g_7.adicionaAresta('A-C')
        self.g_7.adicionaAresta('A-D')
        self.g_7.adicionaAresta('B-D')
        self.g_7.adicionaAresta('D-C')
        self.g_7.adicionaAresta('B-E')
        self.g_7.adicionaAresta('C-E')

        # Grafos Dijkstra

        self.g_D1 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g']:
            self.g_D1.adicionaVertice(i)
        for i in ['A-B', 'A-M', 'A-L', 'B-C', 'B-D', 'C-V', 'V-B', 'D-E', 'E-F', 'E-X', 'F-G', 'G-g', 'G-H', 'H-I',
                  'I-J', 'J-K', 'J-a', 'K-a', 'M-N', 'N-W', 'N-V', 'N-P', 'V-W', 'W-D', 'W-U', 'U-Y', 'U-T', 'U-X',
                  'X-Y', 'X-c', 'c-d', 'c-b', 'd-e', 'd-J', 'e-X', 'Y-Z', 'Y-F', 'Z-e', 'Z-f', 'Z-g', 'L-M', 'L-O',
                  'O-N', 'O-Q', 'Q-S', 'S-T', 'T-X', 'P-R', 'R-X']:
            self.g_D1.adicionaAresta(i)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         ['J-J', 'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-C', 'C-Z', 'E-E', 'E-P', 'E-M', 'E-T', 'E-Z',
                          'P-P', 'P-M', 'P-T', 'P-Z', 'M-M', 'M-Z', 'T-T', 'Z-Z'])

        self.assertEqual(self.g_c.vertices_nao_adjacentes(), ['J-J', 'C-C', 'E-E', 'P-P'])

        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), ['J-J'])

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta uma única vez por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 3)
        self.assertEqual(self.g_l2.grau('B'), 3)
        self.assertEqual(self.g_l4.grau('D'), 1)

    def test_arestas_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        # {'a1': 'J-C', 'a2': 'C-E', 'a3': 'C-E', 'a4': 'C-P', 'a5': 'C-P', 'a6': 'C-M', 'a7': 'C-T', 'a8': 'M-T',
        # 'a9': 'T-Z'}
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), set(['J-C']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')),
                         set(['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')), set(['C-M', 'M-T']))

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        # self.assertTrue((self.g_c2.eh_completo())) não existe referência.
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertTrue((self.g_l4.eh_completo()))
        self.assertTrue((self.g_l5.eh_completo()))

    def test_caminhoEuleriano(self):
        self.assertFalse(self.g_p.caminhoEuleriano())
        self.assertTrue(self.g_1.caminhoEuleriano())
        self.assertFalse(self.g_2.caminhoEuleriano())
        self.assertTrue(self.g_3.caminhoEuleriano())
        self.assertTrue(self.g_4.caminhoEuleriano())
        self.assertTrue(self.g_5.caminhoEuleriano())
        self.assertFalse(self.g_p_sem_paralelas.caminhoEuleriano())
        self.assertFalse(self.g_c.caminhoEuleriano())
        self.assertTrue(self.g_l1.caminhoEuleriano())
        self.assertFalse(self.g_l2.caminhoEuleriano())
        self.assertTrue(self.g_l3.caminhoEuleriano())

    def test_fleury(self):
        self.assertEqual(self.g_1.fleury(), ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'E', 'C', 'A'])
        self.assertFalse(self.g_2.fleury())
        self.assertEqual(self.g_3.fleury(), ['A', 'B', 'C', 'E', 'D', 'B', 'E', 'F', 'C', 'A'])
        self.assertEqual(self.g_4.fleury(), ['B', 'A', 'C', 'D', 'F', 'C', 'E', 'A', 'D', 'B'])
        self.assertEqual(self.g_5.fleury(), ['A', 'B', 'D', 'C', 'A', 'D', 'E', 'B'])
        self.assertFalse(self.g_p.fleury())
        self.assertFalse(self.g_p_sem_paralelas.fleury())
        self.assertFalse(self.g_c.fleury())
        self.assertEqual(self.g_l1.fleury(), ['A', 'B'])
        self.assertFalse(self.g_l2.fleury())
        self.assertEqual(self.g_l3.fleury(), ['A'])

    def test_ciclo_hamiltoniano(self):
        self.assertFalse(self.g_1.ciclo_hamiltoniano())
        self.assertFalse(self.g_2.ciclo_hamiltoniano())
        self.assertEqual(self.g_3.ciclo_hamiltoniano(), ['A', 'B', 'D', 'E', 'F', 'C', 'A'])
        self.assertEqual(self.g_4.ciclo_hamiltoniano(), ['A', 'B', 'D', 'F', 'C', 'E', 'A'])
        self.assertEqual(self.g_5.ciclo_hamiltoniano(), ['A', 'B', 'E', 'D', 'C', 'A'])
        self.assertEqual(self.g_7.ciclo_hamiltoniano(), ['A', 'B', 'E', 'C', 'D', 'A'])
        self.assertEqual(self.g_c.ciclo_hamiltoniano(), ['J', 'C', 'E', 'P', 'J'])
        self.assertFalse(self.g_l1.ciclo_hamiltoniano())
        self.assertFalse(self.g_l2.ciclo_hamiltoniano())
        self.assertFalse(self.g_l3.ciclo_hamiltoniano())

    def test_dijkstra(self):
        self.assertEqual(self.g_D1.dijkstra('A', 'a', ['Q', 'X', 'G', 'I', 'J'], 3,4),
                         ['A', 'L', 'O', 'Q', 'S', 'T', 'X', 'c', 'd', 'J', 'a'])
        self.assertEqual(self.g_D1.dijkstra('A', 'a', ['G', 'I'], 5,5),
                         ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'a'])
        self.assertEqual(self.g_p.dijkstra('J', 'Z', ['M'], 2, 2), ['J', 'C', 'M', 'T', 'Z'])
        self.assertEqual(self.g_7.dijkstra('A', 'E', ['D'], 1, 2), ['A', 'D', 'B', 'E'])
        self.assertEqual(self.g_4.dijkstra('F', 'B', ['C'], 1, 2), ['F', 'C', 'A', 'B'])
        self.assertEqual(self.g_1.dijkstra('B', 'G', ['A', 'D'], 1, 2), ['B', 'A', 'C', 'E', 'G'])
