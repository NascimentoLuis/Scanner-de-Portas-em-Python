import socket
import threading
import time 


def scan_port(target, port):
 try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # Correção do erro de indentação
            s.settimeout(1)  # Define um tempo limite para a conexão
            result = s.connect_ex((target, port))  # Tenta conectar à porta
            if result == 0:
                print(f"[+] Porta {port} está aberta")
 except Exception as e:
        print(f"Erro ao escanear a porta {port}: {e}")


def scan_ports(target, ports):
    open_ports = [] # Lista para armaezenar as portas abertas
    print(f"Escaneando {target}...")
    threads = [] 
    start_time = time.time() # Marca o início do escaneamento
     
    
    for port in ports:
         thread = threading.Thread(target=scan_port, args=(target, port, open_ports))
         threads.append(thread)
         threads.append(thread)
         thread.start()
         
         
    for thread in threads:
         thread.join()
         
         
    end_time = time.time()  # Marca o fim do escaneamento
    elapsed_time = end_time - start_time # Calcula o tempo total     
     
     # Informações adicionais ao final do escaneamento
     
    print(f"\nEscaneamento concluído para {target}")  
    print(f"Total de {len(ports)} portas escaneadas.")
    print(f"Portas abertas: {len(open_ports)}")
    print(f"Tempo total de escanamento: {elapsed_time:.2f} segundos")
     
         
     

if __name__ == "__main__":
     target_ip = input("Digite o IP ou domínio do alvo: ")
     port_range = range(1, 1025) # Escaneia portas de 1 a 1024
     scan_ports(target_ip, port_range)                      