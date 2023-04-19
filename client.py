import socket
import os
import subprocess
import time

s = socket.socket()
host = '192.168.236.114'
port = 9999

s.connect((host, port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0 and data[:1].decode("utf-8")!="@":
        cmd = subprocess.Popen(data[3:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,"utf-8")
        currentWD = os.getcwd() + "> "
        s.send(str.encode(output_str + currentWD))

        print(output_str)
    if len(data) > 0 and data[:1].decode("utf-8")=="@":
        file = open("blocks.txt", "a")
        file.write(data.decode("utf-8"))
        file.close()

    if len(data) > 0 and data[:2].decode("utf-8")=="##":
        file = open("reducer.py", "w")
        file.write(data.decode("utf-8"))
        file.close()
        cmd = subprocess.Popen("python reducer.py result.txt",shell=True)
        # time.sleep(2)
        # file = open("result.txt", "r")
        # data = file.read()
        # print(data)
        # s.send(data.encode("utf-8"))
        # file.close()

    elif len(data) > 0 and data[:1].decode("utf-8")=="#":
        file = open("mapper.py", "w")
        file.write(data.decode("utf-8"))
        file.close()
        cmd = subprocess.Popen("python mapper.py blocks.txt",shell=True)
        # time.sleep(2)
        # file = open("result.txt", "r")
        # data = file.read()
        # print(data)
        # s.send(data.encode("utf-8"))
        # file.close()

        


