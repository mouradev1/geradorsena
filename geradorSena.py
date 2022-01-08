import random
import pandas as pd
import json
from menu import menu 
class Gerador:
    def __init__(self,listaGeral,listaVirada) -> None:
        self.listaGeral = listaGeral
        self.listaVirada = listaVirada

    def listaNumeros(self):
        with open("numeros.json","r", encoding='utf-8') as f:
         dado = json.load(f)
         self.listaGeral = dado[self.listaGeral]
         self.listaVirada = dado[self.listaVirada]
         return 
    def resultado(self):
        print(" ------------------ LISTA GERAL ------------------ ")
        for i in range(3):
          ListaGeralAtualizada = random.sample(self.listaGeral, 6)
          print(ListaGeralAtualizada)
        print('____________________________________________________')
        print(" ------------------ LISTA VIRADA ------------------ ")
        for i in range(7):
          ListaViradaAtualizada = random.sample(self.listaVirada, 6)
          print(ListaViradaAtualizada)

def main():
    escolhar = menu()
    if escolhar == "1":
        jogos = Gerador('listaGeral','listaVirada')
        jogos.listaNumeros()
        jogos.resultado()
        main()
    elif escolhar == '2':
        exit()
    else:
        print("Escolhar invalida.")
        main()

main()