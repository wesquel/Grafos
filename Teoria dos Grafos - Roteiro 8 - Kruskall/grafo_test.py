import unittest
from grafo_adj_nao_dir import Grafo


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        # {'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'}
        self.g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('J-C', 3)
        self.g_p.adicionaAresta('C-E', 1)
        self.g_p.adicionaAresta('C-E', 1)
        self.g_p.adicionaAresta('C-P', 2)
        self.g_p.adicionaAresta('C-P', 2)
        self.g_p.adicionaAresta('C-M', 3)
        self.g_p.adicionaAresta('C-T', 3)
        self.g_p.adicionaAresta('M-T', 2)
        self.g_p.adicionaAresta('T-Z', 2)

        # Grafos completos

        self.g_c = Grafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('J-C', 2)
        self.g_c.adicionaAresta('J-E', 3)
        self.g_c.adicionaAresta('J-P', 5)
        self.g_c.adicionaAresta('C-E', 7)
        self.g_c.adicionaAresta('C-P', 2)
        self.g_c.adicionaAresta('E-P', 1)

        self.g_c3 = Grafo(['J'])

        # Grafos com laco
        # self.g_l1 = Grafo(['A', 'B', 'C', 'D'], {'a1':'A-A', 'a2':'B-A', 'a3':'A-A'})
        self.g_l1 = Grafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('A-A', 1)
        self.g_l1.adicionaAresta('A-A', 1)
        self.g_l1.adicionaAresta('B-A', 3)
        # self.g_l2 = Grafo(['A', 'B', 'C', 'D'], {'a1':'A-B', 'a2':'B-B', 'a3':'B-A'})
        self.g_l2 = Grafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('A-B', 1)
        self.g_l2.adicionaAresta('B-B', 1)
        self.g_l2.adicionaAresta('B-A', 1)

        # self.g_l3 = Grafo(['A', 'B', 'C', 'D'], {'a1':'C-A', 'a2':'C-C', 'a3':'D-D'})
        self.g_l3 = Grafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('C-A', 1)
        self.g_l3.adicionaAresta('C-C', 1)
        self.g_l3.adicionaAresta('D-D', 1)


        # Grafos criados por nós

        self.g_1 = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])

        self.g_1.adicionaAresta('A-B', 2)
        self.g_1.adicionaAresta('B-C', 6)
        self.g_1.adicionaAresta('C-D', 2)
        self.g_1.adicionaAresta('D-E', 1)
        self.g_1.adicionaAresta('E-F', 4)
        self.g_1.adicionaAresta('F-G', 1)
        self.g_1.adicionaAresta('G-E', 8)
        self.g_1.adicionaAresta('E-C', 4)
        self.g_1.adicionaAresta('C-A', 2)

        self.g_2 = Grafo(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

        self.g_2.adicionaAresta('1-2', 2)
        self.g_2.adicionaAresta('1-5', 4)
        self.g_2.adicionaAresta('1-4', 2)
        self.g_2.adicionaAresta('4-5', 1)
        self.g_2.adicionaAresta('5-2', 9)
        self.g_2.adicionaAresta('2-3', 2)
        self.g_2.adicionaAresta('3-9', 6)
        self.g_2.adicionaAresta('6-8', 4)
        self.g_2.adicionaAresta('8-7', 2)
        self.g_2.adicionaAresta('7-6', 1)

        self.g_3 = Grafo(['A', 'B', 'C', 'D', 'E', 'F'])

        self.g_3.adicionaAresta('A-B', 4)
        self.g_3.adicionaAresta('A-C', 5)
        self.g_3.adicionaAresta('B-D', 7)
        self.g_3.adicionaAresta('B-E', 1)
        self.g_3.adicionaAresta('C-E', 2)
        self.g_3.adicionaAresta('C-F', 5)
        self.g_3.adicionaAresta('D-E', 3)
        self.g_3.adicionaAresta('E-F', 7)
        self.g_3.adicionaAresta('B-C', 2)

        self.g_4 = Grafo(['A', 'B', 'C', 'D', 'E', 'F'])

        self.g_4.adicionaAresta('A-D', 3)
        self.g_4.adicionaAresta('A-B', 1)
        self.g_4.adicionaAresta('C-A', 4)
        self.g_4.adicionaAresta('C-F', 5)
        self.g_4.adicionaAresta('C-D', 8)
        self.g_4.adicionaAresta('D-F', 5)
        self.g_4.adicionaAresta('B-D', 5)
        self.g_4.adicionaAresta('E-A', 2)
        self.g_4.adicionaAresta('E-C', 1)

        self.g_5 = Grafo(['A', 'B', 'C', 'D', 'E'])

        self.g_5.adicionaAresta('A-B', 7)
        self.g_5.adicionaAresta('A-C', 5)
        self.g_5.adicionaAresta('A-D', 2)
        self.g_5.adicionaAresta('C-D', 1)
        self.g_5.adicionaAresta('B-D', 1)
        self.g_5.adicionaAresta('B-E', 2)
        self.g_5.adicionaAresta('D-E', 3)

        self.g_7 = Grafo(['A', 'B', 'C', 'D', 'E'])

        self.g_7.adicionaAresta('A-B', 3)
        self.g_7.adicionaAresta('A-C', 2)
        self.g_7.adicionaAresta('A-D', 1)
        self.g_7.adicionaAresta('B-D', 3)
        self.g_7.adicionaAresta('D-C', 6)
        self.g_7.adicionaAresta('B-E', 7)
        self.g_7.adicionaAresta('C-E', 1)

        # Grafos Dijkstra
        self.g_8 = Grafo(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'])

        self.g_8.adicionaAresta('A-B', 2)
        self.g_8.adicionaAresta('B-D', 5)
        self.g_8.adicionaAresta('D-E', 2)
        self.g_8.adicionaAresta('E-C', 4)
        self.g_8.adicionaAresta('C-A', 10)
        self.g_8.adicionaAresta('A-T', 2)
        self.g_8.adicionaAresta('B-P', 1)
        self.g_8.adicionaAresta('D-F', 8)
        self.g_8.adicionaAresta('E-G', 5)
        self.g_8.adicionaAresta('C-Q', 2)
        self.g_8.adicionaAresta('T-R', 3)
        self.g_8.adicionaAresta('R-P', 6)
        self.g_8.adicionaAresta('P-J', 4)
        self.g_8.adicionaAresta('J-F', 6)
        self.g_8.adicionaAresta('F-H', 2)
        self.g_8.adicionaAresta('H-G', 9)
        self.g_8.adicionaAresta('G-K', 1)
        self.g_8.adicionaAresta('K-Q', 5)
        self.g_8.adicionaAresta('Q-S', 2)
        self.g_8.adicionaAresta('S-T', 3)
        self.g_8.adicionaAresta('R-O', 8)
        self.g_8.adicionaAresta('J-M', 1)
        self.g_8.adicionaAresta('H-I', 1)
        self.g_8.adicionaAresta('K-L', 5)
        self.g_8.adicionaAresta('S-N', 4)
        self.g_8.adicionaAresta('M-O', 2)
        self.g_8.adicionaAresta('O-N', 5)
        self.g_8.adicionaAresta('N-L', 9)
        self.g_8.adicionaAresta('L-I', 7)
        self.g_8.adicionaAresta('I-M', 2)

        self.g_10 = Grafo(['A', 'U', 'D', 'I', 'E', 'F', 'O', 'H', 'S', 'M', 'L', 'K', 'N'])

        self.g_10.adicionaAresta('A-U', 1)
        self.g_10.adicionaAresta('A-D', 2)
        self.g_10.adicionaAresta('U-D', 4)
        self.g_10.adicionaAresta('U-N', 2)
        self.g_10.adicionaAresta('D-K', 1)
        self.g_10.adicionaAresta('A-E', 2)
        self.g_10.adicionaAresta('I-E', 2)
        self.g_10.adicionaAresta('E-F', 5)
        self.g_10.adicionaAresta('F-K', 1)
        self.g_10.adicionaAresta('F-H', 1)
        self.g_10.adicionaAresta('F-O', 3)
        self.g_10.adicionaAresta('O-H', 2)
        self.g_10.adicionaAresta('H-S', 1)
        self.g_10.adicionaAresta('H-M', 3)
        self.g_10.adicionaAresta('K-L', 1)
        self.g_10.adicionaAresta('L-M', 4)
        self.g_10.adicionaAresta('N-M', 2)
        self.g_10.adicionaAresta('K-H', 2)
        self.g_10.adicionaAresta('I-S', 9)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         ['J-J', 'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-C', 'C-Z', 'E-E', 'E-P', 'E-M', 'E-T', 'E-Z',
                          'P-P', 'P-M', 'P-T', 'P-Z', 'M-M', 'M-Z', 'T-T', 'Z-Z'])

        self.assertEqual(self.g_c.vertices_nao_adjacentes(), ['J-J', 'C-C', 'E-E', 'P-P'])

        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), ['J-J'])


    def test_kruskall(self):
        self.assertEqual(self.g_p.algoritimo_kruskal(), ['C-E', 'C-M', 'M-T', 'T-Z', 'J-C', 'C-P'])
        self.assertEqual(self.g_1.algoritimo_kruskal(), ['D-E', 'C-D', 'A-B', 'A-C', 'E-F', 'F-G'])
        self.assertFalse(self.g_2.algoritimo_kruskal())
        self.assertEqual(self.g_3.algoritimo_kruskal(), ['B-E', 'B-C', 'D-E', 'A-B', 'C-F'])
        self.assertEqual(self.g_4.algoritimo_kruskal(), ['A-B', 'A-E', 'C-E', 'A-D', 'C-F'])
        self.assertEqual(self.g_5.algoritimo_kruskal(), ['B-D', 'C-D', 'A-D', 'B-E'])
        self.assertEqual(self.g_7.algoritimo_kruskal(), ['A-D', 'A-C', 'C-E', 'A-B'])
        self.assertEqual(self.g_8.algoritimo_kruskal(), ['B-P', 'A-B', 'A-T', 'R-T', 'S-T', 'C-Q', 'Q-S', 'C-E', 'D-E', 'J-P', 'H-I', 'F-H', 'I-M', 'J-M', 'M-O', 'N-S', 'E-G', 'G-K', 'K-L'])
        self.assertEqual(self.g_10.algoritimo_kruskal(), ['A-U', 'A-D', 'D-K', 'F-K', 'F-H', 'H-S', 'L-K', 'A-E', 'I-E', 'O-H', 'U-N', 'M-N'])


    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertTrue((self.g_c.eh_completo()))
        # self.assertTrue((self.g_c2.eh_completo())) não existe referência.
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
