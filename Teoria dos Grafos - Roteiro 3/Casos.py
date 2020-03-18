import unittest
from grafo import *


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'],
                         {'a1': 'J-C', 'a2': 'C-E', 'a3': 'C-E', 'a4': 'C-P', 'a5': 'C-P', 'a6': 'C-M', 'a7': 'C-T',
                          'a8': 'M-T', 'a9': 'T-Z'})

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'],
                                       {'a1': 'J-C', 'a3': 'C-E', 'a4': 'C-P', 'a6': 'C-M', 'a7': 'C-T', 'a8': 'M-T',
                                        'a9': 'T-Z'})

        # Grafos completos
        self.g_c = Grafo(['J', 'C', 'E', 'P'],
                         {'a1': 'J-C', 'a3': 'J-E', 'a4': 'J-P', 'a6': 'C-E', 'a7': 'C-P', 'a8': 'E-P'})
        self.g_c2 = Grafo(['J', 'C', 'E', 'P'],
                          {'a1': 'J-C', 'a3': 'E-J', 'a4': 'J-P', 'a6': 'E-C', 'a7': 'C-P', 'a8': 'P-E'})
        self.g_c3 = Grafo(['J'])

        # Grafos com laco
        self.g_l1 = Grafo(['A', 'B', 'C', 'D'], {'a1': 'A-A', 'a2': 'B-A', 'a3': 'A-A'})
        self.g_l2 = Grafo(['A', 'B', 'C', 'D'], {'a1': 'A-B', 'a2': 'B-B', 'a3': 'B-A'})
        self.g_l3 = Grafo(['A', 'B', 'C', 'D'], {'a1': 'C-A', 'a2': 'C-C', 'a3': 'D-D'})
        self.g_l4 = Grafo(['D'], {'a2': 'D-D'})
        self.g_l5 = Grafo(['C', 'D'], {'a2': 'D-C', 'a3': 'C-C'})

        # Grafos para testar DFS
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
                        {'a1': 'A-D', 'a2': 'A-E', 'a3': 'B-D', 'a4': 'B-E', 'a5': 'C-D',
                         'a6': 'C-E'})  # Grafo bijetor 3/2
        self.g7 = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'],
                        {'a1': 'A-B', 'a2': 'B-C', 'a3': 'C-D', 'a4': 'D-E', 'a5': 'E-C', 'a6': 'C-A', 'a7': 'B-G',
                         'a8': 'G-F', 'a9': 'G-F'})
        self.g8 = Grafo(['AAA', 'BBB', 'CCC', 'DDD', 'EEE', 'FFF', 'GGG'],
                        {'a1': 'AAA-BBB', 'a2': 'BBB-CCC', 'a3': 'BBB-DDD', 'a4': 'AAA-EEE', 'a5': 'EEE-FFF',
                         'a6': 'EEE-GGG'})

        self.g9 = Grafo(['V1', 'V2', 'V3', 'V4', 'V5'],
                   {'a1': 'V1-V2', 'a2': 'V1-V3', 'a3': 'V1-V3', 'a4': 'V2-V3', 'a5': 'V2-V5', 'a6': 'V5-V5',
                    'a7': 'V5-V3', 'a8': 'V3-V4'})  # grafo com paralelos

        self.g10 = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'],
                    {'a1': 'B-C', 'a2': 'C-D', 'a3': 'D-E', 'a4': 'E-I', 'a5': 'I-M', 'a6': 'I-L', 'a7': 'E-H',
                     'a8': 'D-A', 'a9': 'A-F', 'a10': 'F-J', 'a11': 'F-K', 'a12': 'A-G'})  # arvore normal

        self.g11 = Grafo(['A'], {'1': 'A-A'})  # Grafo com 1 só vertice, que em laço

        self.g12 = Grafo(['H', 'J', 'K', 'L'], {'1': 'H-K', '2': 'H-J', '3': 'J-L', '4': 'L-H', '5': 'L-K'})

        self.g13 = Grafo(['V1', 'V2', 'V3', 'V4'],
                    {'a1': 'V1-V2', 'a2': 'V2-V3', 'a3': 'V3-V4', 'a4': 'V4-V1', 'a5': 'V1-V3', 'a6': 'V2-V4'})  # k4

        self.g14 = Grafo(['V1', 'V2', 'V3', 'V4', 'V5'],
                    {'a1': 'V1-V2', 'a2': 'V2-V3', 'a3': 'V3-V4', 'a4': 'V4-V5', 'a5': 'V5-V1', 'a7': 'V1-V3',
                     'a8': 'V1-V4', 'a9': 'V2-V5', 'a10': 'V2-V4', 'a6': 'V5-V3'})  # k5

        # Grafos Teste Ciclo.

        self.g15 = Grafo(['A', 'B', 'C', 'D'],
                    {'a0': 'D-A', 'a1': 'A-B', 'a2': 'B-C', 'a3': 'C-A'})  # Triangulo com uma ponta
        self.g17 = Grafo(['A', 'B', 'C', 'D', 'E', 'F'],
                    {'a0': 'D-A', 'a1': 'A-B', 'a2': 'B-C', 'a3': 'C-A', 'a4': 'D-E',
                     'a5': 'D-F'})  # Triangulo com 2 pontas
        self.g18 = Grafo(['A', 'B', 'C'],
                    {'a1': 'A-B', 'a2': 'A-B', 'a3': 'A-C', 'a4': 'A-C'})  # Grafo somente com paralelas
        self.g19 = Grafo(('A', 'B', 'C'), {'a1': 'A-B', 'a2': 'A-C'})  # Arvore simples
        self.g20 = Grafo(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'),
                    {'a1': 'A-B', 'a2': 'A-C', 'a3': 'D-E', 'a4': 'E-F', 'a5': 'F-G', 'a6': 'G-D',
                     'a7': 'A-H'})  # NÃO CONEXO COM CICLO EM UM SUB GRAFO
        self.g21 = Grafo(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'),
                    {'a1': 'A-B', 'a2': 'A-C', 'a3': 'D-E', 'a4': 'E-F', 'a5': 'F-G', 'a7': 'A-H', 'a8': 'I-J',
                     'a9': 'J-K',
                     'a10': 'K-I'})  # NÃO CONEXO EM 2 SUBGRAFOS E COM CICLO EM UM SUB GRAFO

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         ['J-J', 'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-C', 'C-Z', 'E-J', 'E-E', 'E-P', 'E-M', 'E-T',
                          'E-Z', 'P-J', 'P-E', 'P-P', 'P-M', 'P-T', 'P-Z', 'M-J', 'M-E', 'M-P', 'M-M', 'M-Z', 'T-J',
                          'T-E', 'T-P', 'T-T', 'Z-J', 'Z-C', 'Z-E', 'Z-P', 'Z-M', 'Z-Z'])

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
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), {'a1'})
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')), {'a6', 'a8'})

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
        self.assertEqual(set(self.g1.dfs('J')),
                         {'J', 'a1', 'C', 'a2', 'E', 'a4', 'P', 'a6', 'M', 'a8', 'T', 'a9', 'Z'})
        self.assertEqual(set(self.g2.dfs('K')),
                         {'K', '4', 'G', '2', 'A', '1', 'B', '11', 'F', '10', 'H', '13', 'C', '14', 'D', '15', 'E', '3',
                          'J', '7', 'I'})
        self.assertEqual(set(self.g3.dfs('A')),
                         {'A', '1', 'B', '3', 'C'})
        self.assertEqual(set(self.g4.dfs('C')),
                         {'C', 'a2', 'B', 'a1', 'A'})
        self.assertEqual(self.g5.dfs('A'), -1)
        self.assertEqual(set(self.g6.dfs('A')),
                         {'A', 'a1', 'D', 'a3', 'B', 'a4', 'E', 'a6', 'C'})
        self.assertEqual(set(self.g7.dfs('A')),
                         {'A', 'a1', 'B', 'a2', 'C', 'a3', 'D', 'a4', 'E', 'a7', 'G', 'a8', 'F'})
        self.assertEqual(set(self.g8.dfs('EEE')),
                         {'EEE', 'a4', 'AAA', 'a1', 'BBB', 'a2', 'CCC', 'a3', 'DDD', 'a5', 'FFF', 'a6', 'GGG'})
        self.assertEqual(set(self.g9.dfs('V1')),
                         {'V1', 'a1', 'V2', 'a4', 'V3', 'a7', 'V5', 'a8', 'V4'})
        self.assertEqual(set(self.g10.dfs('B')),
                         {'B', 'a1', 'C', 'a2', 'D', 'a3', 'E', 'a4', 'I', 'a5', 'M', 'a6', 'L', 'a7', 'H', 'a8', 'A',
                          'a9', 'F', 'a10', 'J', 'a11', 'K', 'a12', 'G'})
        self.assertEqual(self.g11.dfs('A'), -1)
        self.assertEqual(set(self.g12.dfs('L')), {'L', '3', 'J', '2', 'H', '1', 'K'})
        self.assertEqual(set(self.g13.dfs('V2')),
                         {'V2', 'a1', 'V1', 'a4', 'V4', 'a3', 'V3'})
        self.assertEqual(set(self.g14.dfs('V4')),{'V4', 'a3', 'V3', 'a2', 'V2', 'a1', 'V1', 'a5', 'V5'})

    def test_ha_ciclo(self):
        self.assertEqual(set(self.g_p.ha_ciclo()), {'C', 'a2', 'E', 'a3', 'C'})
        self.assertEqual(set(self.g2.ha_ciclo()), {'A', '1', 'B', '11', 'F', '10', 'H', '9', 'G', '2', 'A'})
        self.assertEqual(set(self.g3.ha_ciclo()), {'B', '2', 'B'})
        self.assertEqual(set(self.g4.ha_ciclo()), {'A', 'a1', 'B', 'a2', 'C', 'a3', 'A'})
        self.assertEqual(set(self.g5.ha_ciclo()), {'A', 'a1', 'B', 'a2', 'C', 'a3', 'A'})
        self.assertEqual(set(self.g6.ha_ciclo()), {'A', 'a1', 'D', 'a3', 'B', 'a4', 'E', 'a2', 'A'})
        self.assertEqual(set(self.g7.ha_ciclo()), {'G', 'a8', 'F', 'a9', 'G'})
        self.assertEqual(set(self.g15.ha_ciclo()), {'A', 'a1', 'B', 'a2', 'C', 'a3', 'A'})
        self.assertEqual(set(self.g17.ha_ciclo()), {'A', 'a1', 'B', 'a2', 'C', 'a3', 'A'})
        self.assertEqual(set(self.g18.ha_ciclo()), {'A', 'a1', 'B', 'a2', 'A'})
        self.assertEqual(set(self.g20.ha_ciclo()), {'D', 'a3', 'E', 'a4', 'F', 'a5', 'G', 'a6', 'D'})
        self.assertEqual(set(self.g21.ha_ciclo()), {'I', 'a8', 'J', 'a9', 'K', 'a10', 'I'})

    def test_conexo(self):
        self.assertTrue(self.g1.conexo())
        self.assertTrue(self.g2.conexo())
        self.assertFalse(self.g20.conexo())
        self.assertFalse(self.g21.conexo())


