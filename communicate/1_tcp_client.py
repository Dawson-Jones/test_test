import socket
import time


def main():
    while True:
        # 1. 创建tcp的套接字
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2. 链接服务器
        # tcp_socket.connect(("119.3.33.86", 80))
        tcp_socket.connect(("127.0.0.1", 8080))
        # tcp_socket.connect(("tcp_server", 33445))
        # 3. 发送/接受数据
        send_data = input("请输入要发送的数据:")
        # send_data = """
        #            GET / HTTP/1.1
        #            Host: www.bilibili.com
        #            Connection: keep-alive
        #            Upgrade-Insecure-Requests: 1
        #            User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36
        #             """
        tcp_socket.send(send_data.encode("utf-8"))
        print(tcp_socket.recv(1024).decode())
        # print("is end")
        # 4. 关闭套接字
        time.sleep(2)
        tcp_socket.close()
        break


if __name__ == "__main__":
    main()
