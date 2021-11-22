import requests
import pandas as pd
import json

url = "https://www.webmotors.com.br/api/search/car"
count = 0

arq = open('relatorio.txt', "w")

for page in range(1, 20):
    querystring = {"url":"https://www.webmotors.com.br/carros^%^2Festoque^%^3F","actualPage":f"{page}","displayPerPage":"24","order":"1","showMenu":"true","showCount":"true","showBreadCrumb":"true","testAB":"false","returnUrl":"false"}
    headers = {
        "Connection": "keep-alive",
        "sec-ch-ua": "'Not A;Brand';v='99', 'Chromium';v='96', 'Google Chrome';v='96'",
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        "sec-ch-ua-platform": "Windows",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.webmotors.com.br/carros/estoque?idcmpint=t1:c17:m07:webmotors:busca::verofertas",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "pt-BR,pt;q=0.9",
        "Cookie": "at_check=true; AMCVS_3ADD33055666F1A47F000101%40AdobeOrg=1; __gads=ID=6c03acadb41b5a7a-22dc4269cacc0022:T=1637341298:S=ALNI_MYkL6eK8EkyG9u-osXwCajI63sTlA; s_cc=true; blueID=adf19058-d67b-4159-993d-5f5e0b8192e1; _gcl_au=1.1.132582708.1637341304; _fbp=fb.2.1637341304795.1251813777; pxcts=6077f000-495a-11ec-becc-77b15cabac5b; _pxvid=6077b4de-495a-11ec-a519-456c64587169; _hjSessionUser_278928=eyJpZCI6IjhjOWYwZGRiLWVlNWEtNTNhNS1hMWQ5LTM3NDNkMjAyYzg5OCIsImNyZWF0ZWQiOjE2MzczNDEzMDU5NDIsImV4aXN0aW5nIjp0cnVlfQ==; WebMotorsVisitor=1; AMCV_3ADD33055666F1A47F000101%40AdobeOrg=-1124106680%7CMCIDTS%7C18951%7CMCMID%7C43845425244463386702555944261390676016%7CMCAAMLH-1638044223%7C4%7CMCAAMB-1638044223%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1637446623s%7CNONE%7CMCSYNCS%7C1083-18958*1085-18958*1086-18958*1087-18958*1088-18958*19913-18958*83349-18958%7CMCSYNCSOP%7C411-18958%7CvVersion%7C5.2.0; _hjSession_278928=eyJpZCI6ImRlN2IyYWIxLTc0OGEtNGVlNS1iNmEwLTIwMWU5MDQ1YzQzOSIsImNyZWF0ZWQiOjE2Mzc0Mzk0MjU4NDR9; _hjAbsoluteSessionInProgress=0; cto_bundle=sHRBQ19VT252WUVObEQ3bERUNG5rNDVJdlkwTnVjVkhFWDRpMUJUZ0pOT2pPTmhQRDJ0d0dIYWcwTXdBQ0lrNkFCZTVwaFQxJTJGek04UlJJZnVDQjZVZFNTQUFLS3l1aHhsRURwcjNYNm5YZldRVGxBNFBUd21ka0VxajJISXklMkYwQjNKSTg; _px3=72f901e2a9a3ae16694edf1a316fbe839520b4f14b301b0d4bee4e03244419a9:RRIL/5qfFfM4yoU8MA2jtU49d6VqOUUod+XJTMXQn6pM0szoZPxPGPXs+e+R4aLfBRc1qFI91Ev7H3pe20tqmw==:1000:u7v7f9mqJFOYu7hYpfe6qtjVmbgDrg7qf+rxSb865XaUEZsY7txjKmc7VDaa+wMKBfnamSqdj+LeZghL/98JL8uOj2xtieFXiWMw4lPRVU8Lm54GKGOho7EdXvn9iJcclHwFjNx/JPbJX7SDhfvgjMygPvf2ZudRtUclCRMyk/THWRbYmUUGgOJduLlr4L0ZdFd6q1A40istJIu220USOg==; WMLastFilterSearch=%7B%22car%22%3A%22carros%2Festoque%3Fidcmpint%3Dt1%3Ac17%3Am07%3Awebmotors%3Abusca%3A%3Averofertas%22%2C%22bike%22%3A%22motos%2Festoque%22%2C%22estadocidade%22%3A%22estoque%22%2C%22lastType%22%3A%22car%22%2C%22cookie%22%3A%22v3%22%2C%22ano%22%3A%7B%7D%2C%22preco%22%3A%7B%7D%2C%22marca%22%3A%22%22%2C%22modelo%22%3A%22%22%7D; WebMotorsSearchDataLayer=%7B%22search%22%3A%7B%22location%22%3A%7B%7D%2C%22ordination%22%3A%7B%22name%22%3A%22Mais%20relevantes%22%2C%22id%22%3A1%7D%2C%22pageNumber%22%3A1%2C%22totalResults%22%3A334415%2C%22vehicle%22%3A%7B%22type%22%3A%7B%22id%22%3A1%2C%22name%22%3A%22carro%22%7D%7D%2C%22cardExhibition%22%3A%7B%22id%22%3A%221%22%2C%22name%22%3A%22Cards%20Grid%22%7D%2C%22eventType%22%3A%22buscaRealizada%22%7D%7D; gpv_v39=%2Fwebmotors%2Fcomprar%2Fresultado; s_sq=%5B%5BB%5D%5D; mbox=PC#abb7dee6c7f84070929000350fd0060d.34_0#1700684246|session#9d395fcaf4b24f6a98311b669f719f4b#1637441279; WebMotorsTrackingFrom=paginacaoRealizada"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)
    jsondata = json.loads(response.text)

    for carro in jsondata['NewSearchResults']:
        count += 1

        nome = carro['make']
        marca = carro['model']
        ano = carro['year']
        preco = carro['price']
        local = carro['location']

        arq.write('/*' * 30)
        # arq.write(f'\n({nome}')
        # arq.write(f' {marca})')
        # arq.write(f'| {ano} |')
        # arq.write(f' {preco} |')
        # arq.write(f' ({local})\n')
        arq.write(f'\n({nome} {marca}) | {ano} | {preco} | ({local})\n\n')

        # print('/*' * 30)
        # print(f'({nome}', f'{marca})', f'| {ano} |', f'{preco} |', f'({local})')

    print(f'QTD = {count}')

print(f'QTD FINAL = {count}')

arq.close()