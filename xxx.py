import socket


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(("", 5678))
    # 3. 让默认的套接字由主动变为被动 linsen
    tcp_server_socket.listen(128)
    print("---1---")
    while True:
        # 4. 等待客户端的链接 accept
        new_client_socket, client_address = tcp_server_socket.accept()
        while True:
            recv_data = new_client_socket.recv(1024).decode("utf-8")
            print(f"{recv_data}\t来自于:{client_address}")
            if recv_data:
                with open("test.json", "a") as f:
                    f.write(recv_data)
            else:
                break
        # 5. 关闭套接字
        print("已经服务完成, 等待一个新的客户端的到来")
        new_client_socket.close()


if __name__ == "__main__":
    main()
