import socket


def main():
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 绑定本地信息
    tcp_server_socket.bind(("", 7890))
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
                new_client_socket.send(input("请输入要发送的信息:").encode("utf-8"))
            else:
                break
        # 5. 关闭套接字
        print("已经服务完成, 等待一个新的客户端的到来")
        new_client_socket.close()
    tcp_server_socket.close()

    """
    recv_data:
    ------------------------------------------
    GET / HTTP/1.1
    Host: 127.0.0.1:7890
    Connection: keep-alive
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36
    Sec-Fetch-User: ?1
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    Sec-Fetch-Site: none
    Sec-Fetch-Mode: navigate
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
    Cookie: session=71b54e08-72ce-40e9-a69e-58b67b5c36c0.mKreyeIiLJSkuoCFFsvG7vICXtA; csrf_token=ImY0OWVkMTEzNTkzMDZkNWU3NTQ2YzFmZjVmOTJmNThhYjk5MTBkYTIi.XXotFg.iROj2P4Y-8vmr_ivcjeYUQG8caY; csrftoken=84v60WIxx3xvp50tEA9ZpkPk1faUfYJ16h14T7wSHp07t2IkP7ibX6MyVOOh6Iui

    !!!: 注意这里还有一个空行
    """


if __name__ == "__main__":
    main()
