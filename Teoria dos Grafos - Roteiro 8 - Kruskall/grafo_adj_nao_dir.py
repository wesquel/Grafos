# -*- coding: utf-8 -*-
import math
from copy import deepcopy


class VerticeInvalidoException(Exception):
    pass


class ArestaInvalidaException(Exception):
    pass


class MatrizInvalidaException(Exception):
    pass


class Grafo:
    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'
    __maior_vertice = 0

    def __init__(self, V=None, M=None):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param V: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma matriz de adjacência que guarda as arestas do grafo. Cada entrada da matriz tem um inteiro que indica a quantidade de arestas que ligam aqueles vértices
        '''

        if V == None:
            V = list()
        if M == None:
            M = list()

        for v in V:
            if not (Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

        self.N = list(V)

        if M == []:
            for k in range(len(V)):
                M.append(list())
                for l in range(len(V)):
                    if k > l:
                        M[k].append('-')
                    else:
                        M[k].append(0)

        if len(M) != len(V):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in M:
            if len(c) != len(V):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for i in range(len(V)):
            for j in range(len(V)):
                '''
                Verifica se os índices passados como parâmetro representam um elemento da matriz abaixo da diagonal principal.
                Além disso, verifica se o referido elemento é um traço "-". Isso indica que a matriz é não direcionada e foi construída corretamente.
                '''
                if i > j and not (M[i][j] == '-'):
                    raise MatrizInvalidaException('A matriz não representa uma matriz não direcionada')

                aresta = V[i] + Grafo.SEPARADOR_ARESTA + V[j]
                if not (self.arestaValida(aresta)):
                    raise ArestaInvalidaException('A aresta ' + aresta + ' é inválida')

        self.M = list(M)

    def arestaValida(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um string com o formato a-b, onde:
        a é um substring de aresta que é o nome de um vértice adjacente à aresta.
        - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Além disso, uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''

        # Não pode haver mais de um caractere separador
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        if not (self.existeVertice(aresta[:i_traco])) or not (self.existeVertice(aresta[i_traco + 1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def __primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice X
        :param a: a aresta a ser analisada
        :return: O primeiro vértice da aresta
        '''
        return a[0:a.index(Grafo.SEPARADOR_ARESTA)]

    def __segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice Y
        :param a: A aresta a ser analisada
        :return: O segundo vértice da aresta
        '''
        return a[a.index(Grafo.SEPARADOR_ARESTA) + 1:]

    def __indice_primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice X na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do primeiro vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__primeiro_vertice_aresta(a))

    def __indice_segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice Y na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do segundo vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__segundo_vertice_aresta(a))

    def existeAresta(self, a: str):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, a):
            for i in range(len(self.M)):
                for j in range(len(self.M)):
                    if self.M[self.__indice_primeiro_vertice_aresta(a)][self.__indice_segundo_vertice_aresta(a)]:
                        existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Inclui um vértice no grafo se ele estiver no formato correto.
        :param v: O vértice a ser incluído no grafo.
        :raises VerticeInvalidoException se o vértice já existe ou se ele não estiver no formato válido.
        '''
        if v in self.N:
            raise VerticeInvalidoException('O vértice {} já existe'.format(v))

        if self.verticeValido(v):
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

            self.N.append(v)  # Adiciona vértice na lista de vértices
            self.M.append([])  # Adiciona a linha

            for k in range(len(self.N)):
                if k != len(self.N) - 1:
                    self.M[k].append(0)  # adiciona os elementos da coluna do vértice
                    self.M[self.N.index(v)].append('-')  # adiciona os elementos da linha do vértice
                else:
                    self.M[self.N.index(v)].append(0)  # adiciona um zero no último elemento da linha
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, a, n):
        '''
        Adiciona uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''

        if self.arestaValida(a):
            i_a1 = self.__indice_primeiro_vertice_aresta(a)
            i_a2 = self.__indice_segundo_vertice_aresta(a)
            if i_a1 < i_a2:
                self.M[i_a1][i_a2] += n
            else:
                self.M[i_a2][i_a1] += n
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def remove_aresta(self, a):
        '''
        Remove uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.arestaValida(a):
            if self.existeAresta(a):
                i_a1 = self.__indice_primeiro_vertice_aresta(a)
                i_a2 = self.__indice_segundo_vertice_aresta(a)
                if i_a1 < i_a2:
                    self.M[i_a1][i_a2] -= 1
                else:
                    self.M[i_a2][i_a1] -= 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''

        # Dá o espaçamento correto de acordo com o tamanho do string do maior vértice
        espaco = ' ' * (self.__maior_vertice)

        grafo_str = espaco + ' '

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca o espaço se não for o último vértice
                grafo_str += ' '

        grafo_str += '\n'

        for l in range(len(self.M)):
            grafo_str += self.N[l] + ' '
            for c in range(len(self.M)):
                grafo_str += str(self.M[l][c]) + ' '
            grafo_str += '\n'

        return grafo_str

    def vertices_nao_adjacentes(self):  # Não adicionamos a adjacência inversa
        lista = []
        for x in range(len(self.N)):
            for y in range(len(self.M[x])):
                if self.M[x][y] == 0:
                    string = self.N[x] + '-' + self.N[y]
                    lista.append(string)
        return lista

    def ha_laco(self):
        for x in range(len(self.N)):
            if self.M[x][x] > 0:
                return True
        return False

    def ha_paralelas(self):
        for x in range(len(self.N)):
            for y in range(len(self.M[x])):
                if self.M[x][y] != '-' and self.M[x][y] > 1:
                    return True
        return False

    def grau(self, v):
        valor_grau = 0
        for x in range(len(self.N)):
            if self.N[x] == v:
                # horizontal
                for y in range(len(self.M[x])):
                    if self.M[x][y] != '-' and self.M[x][y] > 0:
                        valor_grau += self.M[x][y]
                # vertical
                for y2 in range(len(self.M[x])):
                    if y2 != x and self.M[y2][x] != '-' and self.M[y2][x] > 0:
                        valor_grau += self.M[y2][x]
        return valor_grau

    def arestas_sobre_vertice(self, v):
        lista = []
        for x in range(len(self.N)):
            if self.N[x] == v:

                # vertical
                for y2 in range(len(self.M[x])):
                    if self.M[y2][x] != '-' and self.M[y2][x] > 0:
                        string2 = self.N[y2] + '-' + self.N[x]
                        for x2 in range(self.M[y2][x]):
                            lista.append(string2)

                # horizontal
                for y in range(len(self.M[x])):
                    if self.M[x][y] != '-' and self.M[x][y] > 0:
                        string = self.N[x] + '-' + self.N[y]
                        for x1 in range(self.M[x][y]):
                            lista.append(string)
        return lista

    def eh_completo(self):
        # Em alguns conceitos vimos que laço não era permitido, porém nos casos de teste eram válidos.
        if self.ha_paralelas():
            return False

        for x in range(len(self.N)):
            for y in range(len(self.M[x])):
                if x != y:
                    if self.M[x][y] != '-' and self.M[x][y] != 1:
                        return False
        return True

    def vizinho(self, vertice):
        vizinhos = []
        peso = []
        for x in range(len(self.N)):
            if self.N[x] == vertice:
                for y in range(len(self.M[x])):
                    if self.M[x][y] != 0 and self.M[x][y] != '-':
                        vizinhos.append(self.N[y])
                        peso.append(self.M[x][y])
                    if self.M[y][x] != 0 and self.M[y][x] != '-':
                        vizinhos.append(self.N[y])
                        peso.append(self.M[y][x])
        lista = [vizinhos, peso]
        return lista

    def concatenando(self, lista):
        for x in range(len(lista)):
            for y in range(len(lista)):
                aux = lista[x] + lista[y]
                if x != y and len(aux) != len(set(aux)):
                    lista.pop(x)
                    lista.pop(y - 1)
                    lista.append(list(set(aux)))
                    return self.concatenando(lista)
        return lista

    def eh_conexo(self):
        lista = []
        for x in range(len(self.N)):
            v = self.vizinho(self.N[x])[0]
            v.append(self.N[x])
            lista.append(v)
        concatenado = self.concatenando(lista)
        contador = 0
        for x in range(len(concatenado)):
            if len(concatenado[x]) > 1:
                contador += 1
        if contador > 1:
            return False
        return True

    def remove_vertice(self, vertice):
        v_main = None
        for x in range(len(self.N)):
            if self.N[x] == vertice:
                v_main = x
                break
        if v_main is None:
            return False
        for y in range(len(self.N)):
            self.M[y].pop(v_main)
        self.M.pop(v_main)
        self.N.pop(v_main)


    def fila_prioridade(self):
        lista = []
        for x in range(len(self.N)):
            for y in range(len(self.N)):
                if self.M[x][y] != '-' and self.M[x][y] > 0:
                    lista.append([self.M[x][y], self.N[x] + '-' + self.N[y]])
        lista.sort()
        return lista

    def algoritimo_kruskal(self):
        fila_p = self.fila_prioridade()
        lista_pop = []
        for x in range(len(fila_p)):
            if fila_p[x][1][0] == fila_p[x][1][2]:
                lista_pop.append(x)
        for x1 in range(len(lista_pop)):
            fila_p.pop(x1)
        ad = fila_p[0][1]
        fila_p.pop(0)

        if len(fila_p) < 2:
            return False

        if not self.eh_conexo():
            return False
        return self.caminho_kruskall(fila_p, [[ad]])

    def caminho_kruskall(self, fila_p, arvorer):

        chk = False
        for x in range(len(arvorer)):
            for y in range(len(arvorer[x])):
                if fila_p[0][1][0] in arvorer[x][y] or fila_p[0][1][2] in arvorer[x][y]:
                    arvorer[x].append(fila_p[0][1])
                    chk = True
                    break

        v_r = fila_p[0][1]

        if not chk:
            arvorer.append([fila_p[0][1]])
        fila_p.pop(0)

        for t in range(len(arvorer)):
            if self.verificar(arvorer[t]):
                for t1 in range(len(arvorer)):
                    if v_r in arvorer[t1]:
                        arvorer[t1].remove(v_r)
                break

        if len(self.N) == len(self.separar_vertices(arvorer[0])) or len(fila_p) == 0:
            lista = []
            for j in arvorer[0]:
                if j not in lista:
                    lista.append(j)
            return lista

        teste = False
        for z0 in range(len(arvorer)):
            for z1 in range(len(arvorer)):
                if z1 != z0 and not teste:
                    for z2 in range(len(arvorer[z1])):
                        if arvorer[z1][z2] in arvorer[z0]:
                            arvorer[z0].extend(arvorer[z1])
                            arvorer.pop(z1)
                            teste = True
                            break

        return self.caminho_kruskall(fila_p, arvorer)

    def verificar(self, arvorer):
        vertices = self.separar_vertices(arvorer)
        g = Grafo(vertices)
        for x in arvorer:
            g.adicionaAresta(x, 1)
        g.check_ciclo()
        return g.check_ciclo()

    def separar_vertices(self, v):
        vertices = []
        for x in range(len(v)):
            if v[x][0] not in vertices:
                vertices.append(v[x][0])
            if v[x][2] not in vertices:
                vertices.append(v[x][2])
        return vertices

    def check_ciclo(self):
        dic = {}
        for x in self.N:
            dic[x] = []
        dic = list(dic.items())
        return self.p_ciclo(self.N[0], [self.N[0]], dic)

    def p_ciclo(self, v, caminho, items):
        if len(caminho) >= 3:
            if caminho[-1] == caminho[-3]:
                caminho.pop(-1)
                v = caminho[-1]
        for x in self.N:
            if caminho.count(x) > 1 and len(caminho) > 3:
                return True

        Lvizinho = self.vizinho(v)[0]
        i = self.N.index(v)

        for x1 in range(len(Lvizinho)):
            if self.N[i] == v:
                if Lvizinho[x1] not in items[i][1]:
                    if len(caminho) > 2 and Lvizinho[x1] == caminho[-2]:
                        pass
                    else:
                        items[i][1].append(Lvizinho[x1])
                        next = Lvizinho[x1]
                        caminho.append(next)
                        return self.p_ciclo(next, caminho, items)

        for x in range(len(items[i][1])):
            items[i][1].pop(0)

        if len(caminho) == 1:
            return False

        caminho.pop(-1)

        return self.p_ciclo(caminho[-1], caminho, items)
