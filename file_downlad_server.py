"""
目标文件：确定文件来源路径
下载到：确定下载后存放地址路径

1.导入模块
2.创建套接字
*3.绑定端口
*4.设置监听，设置套接字由主动为被动
*5.接受客户端连接
6.接收客户端发来的数据（文件名）
   捕获异常（如果要下载的文件名不存在的情况下）
7.查找文件（根据文件名读取内容）
8.向客户端发送数据（循环）
9.关闭和当前客户端的连接
*10.关闭服务器
加*的这几步都是自己仿写时遗漏的

仍存在的问题是：
多个客户端下载是同步的，必须是一个下载完成后，另一个客户端才能连接下载，就是说要排队

"""
import socket

Server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

Server_socket.bind(("",8080))

Server_socket.listen(128)

#接收客户端连接
#加循环，可以一次性接收多个文件
while True:
    ReciveCilentSocket,ip_port = Server_socket.accept()
    print("欢迎新客户端：",ip_port)

    #接收客户端发来的文件名
    Recive_data = ReciveCilentSocket.recv(1024)
    Recive_name = Recive_data.decode()
    print(Recive_name)

    #异常捕获
    try:
        #根据文件名读取文件内容
        #rb是指read binary，读二进制
        with open(Recive_name,"rb") as file:
            #把读取的内容发送给客户端（循环(因为每次能读1024个字节，所以需要循环多读几次)）
                while True:
                    file_date = file.read(1024)
                    #如果filedate把文件内容读取完了，那么再读取的内容就是空的了
                    #if filedate：表示如果filedate不为零（空，false），就是说filedate为真
                    if file_date:
                    #发送文件
                        ReciveCilentSocket.send(file_date)
                    else:
                        break
    except Exception as e:
        print("文件%s下载失败" %Recive_name)
    else:
        print("文件%s下载成功" %Recive_name)

    #关闭与当前客户端的连接
    ReciveCilentSocket.close()


#服务器
#说服务器关闭套接字这句永远不会执行，永不执行是可以的，因为服务器除了断电，时刻在提供服务
Server_socket.close()