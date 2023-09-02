import requests
from bs4 import *
import time
from dadossensiveis import *
import smtplib
import email.message
from movi import *


def enviar_email_prot():

    EMAILS = ['andrewdias2016@gmail.com','arthurnascifar@outlook.com','arthurnascimentotj@outlook.com','thaissa_o.soares@hotmail.com','douradomarcella@gmail.com','yasmimvnb@gmail.com',
              'gersonlima8021@gmail.com','leandror.cruz2015@gmail.com']

    for mail in EMAILS:
        corpo_email = f"""
        <p>OLÁ,</p>
        <p>A última movimentação foi na lista de protocolos: {movi_protocolo(ListaDeProtocolo)}.</p>
        """

        msg = email.message.Message()
        msg['Subject'] = "ANDAMENTO NO SEI"
        msg['From'] = 'andrewdias2016@gmail.com'
        msg['To'] = mail
        password = senha 
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        # Login Credentials for sending the mail
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print(f'Email enviado para {mail}')

def enviar_email_and():

    EMAILS = ['andrewdias2016@gmail.com','arthurnascifar@outlook.com','arthurnascimentotj@outlook.com','thaissa_o.soares@hotmail.com','douradomarcella@gmail.com','yasmimvnb@gmail.com',
              'gersonlima8021@gmail.com','leandror.cruz2015@gmail.com']

    for mail in EMAILS:
        corpo_email = f"""
        <p>OLÁ,</p>
        <p>A última movimentação foi na lista de andamentos: {movi_andamento(ListaDeAndamento)}.</p>
        """

        msg = email.message.Message()
        msg['Subject'] = "ANDAMENTO NO SEI"
        msg['From'] = 'andrewdias2016@gmail.com'
        msg['To'] = mail
        password = senha 
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        # Login Credentials for sending the mail
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print(f'Email enviado para {mail}')



try:
    ANDAMENTO = []

    req = requests.get("https://www10.tjrj.jus.br/sei/modulos/pesquisa/md_pesq_processo_exibir.php?LyFApQuxweZlHTLXUD6u1y7tX4d3oMBqI068jRzh-jmD6lRsMfC_MSxrkq7qMXzIfz0u57sxCObxfxX7102s0OPclxe8lW1cZe2v7-DLgdDvkB0gDy6lhfwnU-GWM4wV")

    html = req.text
    soup = BeautifulSoup(html, "html.parser")
    tags_a = soup.findAll("caption")




    for tag in tags_a:
        for i in tag:
            try:
                numeros = "".join(char for char in i if char.isdigit())
                ANDAMENTO.append(numeros)
            except:
                pass



    valores = []
    for val in ANDAMENTO:
        valores.append(int(val))

        
    ListaDeProtocoloInicial = valores[0]
    ListaDeAndamentoInicial = valores[1]

    print("Procurando...")

    while True:
        try:
            andamento = []
            TEOR = []
            reqs = requests.get("https://www10.tjrj.jus.br/sei/modulos/pesquisa/md_pesq_processo_exibir.php?LyFApQuxweZlHTLXUD6u1y7tX4d3oMBqI068jRzh-jmD6lRsMfC_MSxrkq7qMXzIfz0u57sxCObxfxX7102s0OPclxe8lW1cZe2v7-DLgdDvkB0gDy6lhfwnU-GWM4wV")

            htmls = reqs.text
            soups = BeautifulSoup(htmls, "html.parser")
            tags = soups.findAll("caption")


            for t in tags:
                for i in t:
                    try:
                        numero = "".join(char for char in i if char.isdigit())
                        andamento.append(numero)
                    except:
                        pass



            VALORES = []
            for val in andamento:
                VALORES.append(int(val))

                
            ListaDeProtocolo = VALORES[0]
            ListaDeAndamento = VALORES[1]

            if ListaDeAndamento != ListaDeAndamentoInicial:
                ListaDeAndamentoInicial = ListaDeAndamento
                enviar_email_and()


            if ListaDeProtocolo != ListaDeProtocoloInicial:
                ListaDeProtocoloInicial = ListaDeProtocolo
                enviar_email_prot()

                
                
                
            time.sleep(60)

        except:
            pass

except Exception as e:
    print(e)
    pass





