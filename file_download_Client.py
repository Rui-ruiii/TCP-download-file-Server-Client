"""
1.导入模块
2.创建套接字
3.建立连接
4.接收用户输入的文件名
5.发送文件名到服务端
6.创建文件并且准备保存
7.接受服务端发送的数据，保存到本地（循环）
8.关闭套接字
"""

#1.导入模块
import socket

#2.建立套接字
Download_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#3.建立连接
Server_ip = input("请输入服务器地址：")
Server_port =input("请输入服务器端口号：")
Download_client.connect((Server_ip,Server_port))

#4.接收用户输入的文件名
Download_filename = input("请输入要下载的文件名：")

#5.发送文件名到服务端
Download_client.send(Download_filename.encode())

#6.创建文件并且准备保存(w是文件不存在就不创建)
with open("E:\TCP"+Download_filename,"w") as file:
    #7.接收数据并且保存到本地（循环）
    file_data = Download_client.recv(1024)
    #判断数据是否传送完毕
    if file_data:
        file.write(file_data)
    else:
        break
#8.关闭套接字
Download_client.close()