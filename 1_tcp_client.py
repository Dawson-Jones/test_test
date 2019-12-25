import socket


def main():
    # 1. 创建tcp的套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 链接服务器
    tcp_socket.connect(("192.168.1.104", 8080))
    # 3. 发送/接受数据
    send_data = input("请输入要发送的数据:")
    tcp_socket.send(send_data.encode("utf-8"))
    # 4. 关闭套接字
    tcp_socket.close()


if __name__ == "__main__":
    main()
