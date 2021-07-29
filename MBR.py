import hashlib
import time

def MBRTime():  #분석 시간
    print("[+] MBR Analysis Time:"+time.ctime())
MBRTime()

def MBRSig():
    mbr = open("mbr.bin", 'rb')    #덤프 파일 열기

    data = mbr.read()   #읽은 파일 저장
    print("[-] MBR Dump MD5: "+hashlib.MD5(data).hexdigest())
    print("[-] MBR Dump SHA1: "+hashlib.sha1(data).hexdigest())
    print("[-] MBR Dump sha256: "+hashlib.sha256(data).hexdigest())
    mbr.close()

import time
def MBRTime():
            printf("[+] MBR Analysis Time:"+time.ctime())
MBRTime()

def MBRSig():
        mbr=open("mbr.bin",'rb')
        data=mbr.read()

        sign=data[510:512].encode("hex")
        if sign == '55AA':


        else:
            data[510:512].encode("hex")="55AA"


MBRSig()

def MBRBoot():
    mbr=open("mbr.bin",'rb')
    data = mbr.read()

    offset=data[440:444].encode("hex")
            if offset == '63 7B 9A':


            else:
               data[440:444].encode("hex")="63 7B 9A"

    devicesig=data[437:440].encode("hex")
            if devicesig == '20 1B 50 E7':


            else:
                data[437:440].encode("hex")="20 1B 50 E7"

MBRBoot()


def MBRPt():
   mbr=open("mbr.bin", 'rb')
   data=mbr.read()
   bf1 = data[446:447].encode("hex")

   if   bf1 == "80":

   else:
        data[446:447].encode("hex") == "80"

MBRPt()
