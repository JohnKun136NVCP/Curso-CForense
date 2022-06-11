import binascii
from base64 import encode
import base64
import code
import struct
import re

code_ass = []
decoe_ass = []
doc = []

def toAscii(letra):
    number = ord(letra)
    return number

def loopThrough(mensaje):
    for n in mensaje:
        #print(n)
        code_ass.append(int('{0:b}'.format(toAscii(n))))

def decodeBinary (code):
    file = open('roma.txt','a')
    for i in code:
        #print(str(i))
        a = int(str(i),2)
        b = a.bit_length() + 7 // 8
        c =  a.to_bytes(b,"big")
        ascii_text = c.decode('utf-8')
        mensaje = ascii_text.replace('\x00','')
        decoe_ass.append(mensaje)
        file.write(str(mensaje))
    file.close()

def decodebinaryfile():
    colist = []
    with open('binary.txt','r') as file:
        lineas = file.readlines()
        for x in lineas:
            colist.append(x.replace("\n",""))
    return colist


def decodeMensage(bas64list):
    clean = []
    x= 0
    with open('japon.txt','a') as jp:
        while x<=1:
            clean = bas64list.remove(bas64list[0])
            x+=1
        clean =bas64list.pop()
        base64_message = "".join(bas64list)
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
        message = message.replace('[',"")
        message = message.replace("]","")
        message = message.replace("'","")
        message = message.replace(",","")
        jp.write(message)
    jp.close()



def archivoT():
    with open('normal.txt','r') as file:
        linea = file.read()
        lineas = linea.split("\n")
        return str(lineas)


def archivoB64(code):
    with open('b64.txt','a') as file:
        file.write(str(code))
def archivobin(codebi):
    with open('binary.txt','a') as file:
        for x in codebi:
            file.write(str(x)+' '+"\n")
    file.close()


def main():
    
    decodeBinary(decodebinaryfile())
    decodeMensage(decoe_ass)
    

main()