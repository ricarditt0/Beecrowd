class AFN:
    def __init__(self):
        self.transicoes = {}
        self.proximo_estado = 0

    def novo_estado(self):
        estado = self.proximo_estado
        self.proximo_estado += 1
        self.transicoes[estado] = []
        return estado

    def adicionar_transicao(self,origem,simbolo,destino):
        self.transicoes[origem].append((simbolo,destino))

class Parser:
    def __init__(self,regex):
        self.regex = regex
        self.pos = 0
        self.afn = AFN()

    def build(self):
        inicio,fim = self.parse()
        if self.pos != len(self.regex):
            raise ValueError("regex invalida")
        return inicio, fim, self.afn

    def parse(self):
        c = self.regex[self.pos]
        # caso basico a ou b
        if c == 'a' or c == 'b':
            self.pos += 1
            inicio = self.afn.novo_estado()
            fim = self.afn.novo_estado()
            self.afn.adicionar_transicao(inicio,c,fim)
            return inicio,fim
        #casos compostos (P.S),(P|S),(P*)
        if c == '(':
            self.pos += 1
            inicio_p,fim_p = self.parse()

            if self.regex[self.pos] == '*':
                self.pos += 1
                inicio = self.afn.novo_estado()
                fim = self.afn.novo_estado()
                
                self.afn.adicionar_transicao(inicio,None,inicio_p)
                self.afn.adicionar_transicao(inicio, None, fim)
                self.afn.adicionar_transicao(fim_p,None,inicio_p)
                self.afn.adicionar_transicao(fim_p,None,fim)
                inicio_p, fim_p = inicio, fim

            operator = self.regex[self.pos]
            self.pos += 1
            
            #une final de P com inicio de S
            if operator == '.':

                inicio_s ,fim_s = self.parse()
                            
                if self.regex[self.pos] != ')':
                    raise ValueError("Regex inválida")
                            
                self.pos += 1

                self.afn.adicionar_transicao(fim_p,None,inicio_s)
                return inicio_p,fim_s
            # liga novo inicio com o inicio antigo e finais antigos no novo final
            if operator == '|':

                inicio_s ,fim_s = self.parse()
                            
                if self.regex[self.pos] != ')':
                    raise ValueError("Regex inválida")
                            
                self.pos += 1
                
                inicio = self.afn.novo_estado()
                fim = self.afn.novo_estado()                
                self.afn.adicionar_transicao(inicio,None,inicio_s)
                self.afn.adicionar_transicao(inicio,None,inicio_p)
                self.afn.adicionar_transicao(fim_s,None,fim)
                self.afn.adicionar_transicao(fim_p,None,fim)
                return inicio,fim

            if operator == ')':
                return inicio_p, fim_p
            
            raise ValueError('Operador invalido')
        raise ValueError('Regex invalido')

def movimento_vazio(afn,estados):
    pilha = list(estados)
    visitados = set(estados)

    while pilha:
        estado = pilha.pop()
        for simbolo, destino in afn.transicoes[estado]:
            if simbolo == None and destino not in visitados:
                visitados.add(destino)
                pilha.append(destino)
    return visitados


def reconhece(afn,inicio,fim,palavra):
    estados = movimento_vazio(afn,{inicio})

    for char in palavra:
        proximo = set()
        for estado in estados:
            for simbolo,destino in afn.transicoes[estado]:
                if simbolo == char:
                    proximo.add(destino)
        estados = movimento_vazio(afn,proximo)

        if not estados:
            return False
        
    return fim in movimento_vazio(afn,estados)


while True:

    regex = ''

    try:
        regex = str(input())
    except EOFError:
        break

    n = int(input())
    palavras = []

    for _ in range(n):
        palavra = str(input())
        palavras.append(palavra)

    parser = Parser(regex)
    inicio, fim, afn = parser.build()

    for palavra in palavras:
        resultado = reconhece(afn, inicio, fim, palavra)
        print(f"{'Y' if resultado else 'N'}")
    print('')


