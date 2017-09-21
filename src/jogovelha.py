TAB = []

def inicializar() :
  TAB.append(['.','.','.'])
  TAB.append(['.','.','.'])
  TAB.append(['.','.','.'])
  
def jogar(jogador, linha, coluna):
  if jogador !='X' and jogador != 'O':
    raise RuntimeError('Jogador invalido')
  valores = list(range(0,3))
  if linha not in valores:
    raise RuntimeError('Linha invalida')
  if coluna not in valores:
    raise RuntimeError('Coluna invalida')  
  if TAB[linha][coluna] != '.':
    raise RuntimeError('Jogada invalida, posicao ja esta ocupada')
  else:
    TAB[linha][coluna] = jogador  
  
def tabuleiro():
  return TAB
  
def main():
  inicializar()
  jogar('X', 1, 1)
  for t in tabuleiro():
    print(t)
  
if __name__ == "__main__":
  main()

