import socket
import threading


HOST = '127.0.0.1'
PORT = 8080


def handle_client(conn, addr):
    with conn:
        print(f"{addr=}")
        request_data = conn.recv(1024).decode()
        print(f"{request_data=}")
        import time
        # time.sleep(10)
        response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n<h1>Hello, World!</h1>"
        conn.sendall(response.encode()) 


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        print(f"Server listening on {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

    
if __name__ == "__main__":
    start_server()