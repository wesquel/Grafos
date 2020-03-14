import unittest
from grafo import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'})

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {'a1': 'J-C', 'a3': 'C-E', 'a4': 'C-P', 'a6': 'C-M', 'a7': 'C-T', 'a8': 'M-T', 'a9': 'T-Z'})

        # Grafos completos
        self.g_c = Grafo(['J', 'C', 'E', 'P'], {'a1':'J-C', 'a3':'J-E', 'a4':'J-P', 'a6':'C-E', 'a7':'C-P', 'a8':'E-P'})
        self.g_c2 = Grafo(['J', 'C', 'E', 'P'], {'a1':'J-C', 'a3':'E-J', 'a4':'J-P', 'a6':'E-C', 'a7':'C-P', 'a8':'P-E'})
        self.g_c3 = Grafo(['J'])

        # Grafos com laco
        self.g_l1 = Grafo(['A', 'B', 'C', 'D'], {'a1':'A-A', 'a2':'B-A', 'a3':'A-A'})
        self.g_l2 = Grafo(['A', 'B', 'C', 'D'], {'a1':'A-B', 'a2':'B-B', 'a3':'B-A'})
        self.g_l3 = Grafo(['A', 'B', 'C', 'D'], {'a1':'C-A', 'a2':'C-C', 'a3':'D-D'})
        self.g_l4 = Grafo(['D'], {'a2':'D-D'})
        self.g_l5 = Grafo(['C', 'D'], {'a2':'D-C', 'a3':'C-C'})

        #Grafos para testar DFS
        self.g1 = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'],
                   {'a1': 'J-C', 'a2': 'C-E', 'a3': 'C-E', 'a4': 'C-P', 'a5': 'C-P', 'a6': 'C-M', 'a7': 'C-T',
                    'a8': 'M-T', 'a9': 'T-Z'})
        self.g2 = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'],
                   {'1': 'A-B', '2': 'A-G', '3': 'A-J', '4': 'G-K', '5': 'J-K', '6': 'G-J', '7': 'J-I', '8': 'G-I',
                    '9': 'G-H', '10': 'H-F', '11': 'F-B', '12': 'B-G', '13': 'B-C', '14': 'C-D', '15': 'D-E',
                    '16': 'D-B', '17': 'E-B'})
        self.g3 = Grafo(['A', 'B', 'C'], {'1': 'A-B', '2': 'B-B', '3': 'B-C', '4': 'C-A'})  # Triangulo com laço
        self.g4 = Grafo(['A', 'B', 'C'], {'a1': 'A-B', 'a2': 'B-C', 'a3': 'C-A'})  # Triangulo
        self.g5 = Grafo(['A', 'B', 'C', 'D'],
                   {'a1': 'A-B', 'a2': 'B-C', 'a3': 'C-A'})  # Triangulo com um vértice isolado (Não conexo)
        self.g6 = Grafo(['A', 'B', 'C', 'D', 'E'],
                   {'a1': 'A-D', 'a2': 'A-E', 'a3': 'B-D', 'a4': 'B-E', 'a5': 'C-D', 'a6': 'C-E'})  # Grafo bijetor 3/2
        self.g7 = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'],
                   {'a1': 'A-B', 'a2': 'B-C', 'a3': 'C-D', 'a4': 'D-E', 'a5': 'E-C', 'a6': 'C-A', 'a7': 'B-G',
                    'a8': 'G-F', 'a9': 'G-F'})

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(), ['J-J', 'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-C', 'C-Z', 'E-J', 'E-E', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-J', 'P-E', 'P-P', 'P-M', 'P-T', 'P-Z', 'M-J', 'M-E', 'M-P', 'M-M', 'M-Z', 'T-J', 'T-E', 'T-P', 'T-T', 'Z-J', 'Z-C', 'Z-E', 'Z-P', 'Z-M', 'Z-Z'])

        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         ['J-J', 'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-C', 'C-Z', 'E-J', 'E-E', 'E-P', 'E-M', 'E-T',
                          'E-Z', 'P-J', 'P-E',
                          'P-P', 'P-M', 'P-T', 'P-Z', 'M-J', 'M-E', 'M-P', 'M-M', 'M-Z', 'T-J', 'T-E', 'T-P', 'T-T',
                          'Z-J', 'Z-C', 'Z-E',
                          'Z-P', 'Z-M', 'Z-Z'])

        self.assertEqual(self.g_c.vertices_nao_adjacentes(), ['J-J', 'C-C', 'E-E', 'P-P'])

        self.assertEqual(self.g_c2.vertices_nao_adjacentes(), ['J-J', 'C-C', 'E-E', 'P-P'])

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
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), set(['a1']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')), set(['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')), set(['a6', 'a8']))

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertTrue((self.g_l4.eh_completo()))
        self.assertTrue((self.g_l5.eh_completo()))

    def test_dfs(self):
        self.assertEqual(set(self.g1.dfs('J')), set(['J', 'a1', 'C', 'a2', 'E', 'a4', 'P', 'a6', 'M', 'a8', 'T', 'a9', 'Z']))
        self.assertEqual(set(self.g2.dfs('K')),
                set(['K', '4', 'G', '2', 'A', '1', 'B', '11', 'F', '10', 'H', '13', 'C', '14', 'D', '15', 'E', '3', 'J', '7', 'I']))
        self.assertEqual(set(self.g3.dfs('A')),
                         set(['A', '1', 'B', '3', 'C']))
        self.assertEqual(set(self.g4.dfs('A')),
                         set(['A', 'a1', 'B', 'a2', 'C']))
        self.assertEqual(set(self.g5.dfs('A')),
                         set(['A', 'a1', 'B', 'a2', 'C']))
        self.assertEqual(set(self.g6.dfs('A')),
                         set(['A', 'a1', 'D', 'a3', 'B', 'a4', 'E', 'a6', 'C']))
        self.assertEqual(set(self.g7.dfs('A')),
                         set(['A', 'a1', 'B', 'a2', 'C', 'a3', 'D', 'a4', 'E', 'a7', 'G', 'a8', 'F']))

