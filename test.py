import hashlib
import time

def MBRTime():  #분석 시간
    print("[+] MBR Analysis Time:"+time.ctime())
MBRTime()

def MBRSig():
    mbr = open("mbr.bin", 'rb')    #덤프 파일 열기

    data = mbr.read()   #읽은 파일 저장

    print("[-] MBR Dump sha256: "+hashlib.sha256(data).hexdigest())
    print("[-] MBR Dump SHA1: "+hashlib.sha1(data).hexdigest())
#MD5는 보안 관련 위험성(?) 때문에 이젠 잘 안 쓴다고 하여 sha256으로 바꿔봤습니다
    mbr.close()
