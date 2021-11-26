from requests_html import HTMLSession
from tkinter import *

s = HTMLSession()

lista = ['vale3', 'mglu3', 'petr4', 'itub3']
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/5'
}

def consultar_cotacoes():
    resultado = ''
    for consulta in lista:
        url = f'https://www.google.com/search?q=cotacao+{consulta}'
        req = s.get(url, headers=headers)

        sigla = req.html.find('div.HfMth.PZPZlf span.WuDkNe', first=True).text
        nome = req.html.find('div.E65Bx span.aMEhee.PZPZlf', first=True).text
        cotacao = req.html.find('div.PZPZlf span.IsqQVc.NprOob.wT3VGc', first=True).text
        moeda = req.html.find('div.PZPZlf span.knFDje', first=True).text

        '''
        print(f'Sigla = {sigla}', end=' |')
        print(f'Nome = {nome}', end=' |')
        print(f'Cotação = {cotacao}', end=' |')
        print(f'Moeda = {moeda}')
        print("-*" * 10)
        '''
        divisor = ('-*' * 20)
        resultado += f'Sigla = {sigla} |Nome = {nome} |Cotação = {cotacao} |Moeda = {moeda}\n{divisor}\n'

    texto_cotacoes['text'] = resultado


janela = Tk()
janela.title('Cotações')

texto = Label(janela, text='Clique no Botão para buscar cotações')
texto.grid(column=0, row=0, padx=15, pady=10)

botao = Button(janela, text='Buscar cotação', command=consultar_cotacoes)
botao.grid(column=0, row=1, padx=15, pady=10)

texto_cotacoes = Label(janela, text='')
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()