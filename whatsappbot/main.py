import pywhatkit
from datetime import datetime

from pywhatkit.core.exceptions import CountryCodeException, InternetException, CallTimeException


def enviar_mensagem_para_whatsapp():
    horario_local_atual = datetime.now()
    numero_telefone = input('Digite o número de telefone que receberá a mensagem : ')
    mensagem_a_ser_enviada = input('Digite a mensagem : ')
    hora = int(horario_local_atual.strftime("%H"))
    minutos = int(horario_local_atual.strftime("%M")) + 1

    pywhatkit.sendwhatmsg(numero_telefone, mensagem_a_ser_enviada, hora, minutos)


sair = ''

while sair != 'sair':
    try:
        enviar_mensagem_para_whatsapp()
    except CountryCodeException:
        print('< Por favor informe o código do país correto >')
        continue
    except CallTimeException:
        print('< O tempo foi muito curto para se conectar ao Whatsapp web >')
        continue
    except InternetException:
        print('< Por favor conecte-se á internet >')
        continue
    sair = input('Digite sair pra encerrar o programa : ')
