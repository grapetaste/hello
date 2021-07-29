import hashlib
import time

def MBRTime():  #분석 시간
    print("MBR Analysis Time:"+time.ctime())

mbr = open("test.bin", 'rb')    #덤프 파일 열기
data = mbr.read()   #읽은 파일 저장

def MBRSig():
    print("")
    #print("MBR Dump MD5:"+hashlib.md5(data).hexdigest())
    #print("MBR Dump SHA1:"+hashlib.sha1(data).hexdigest())
    print("MBR Dump SHA256:"+hashlib.sha256(data).hexdigest())
    #MD5, SHA1은 취약점, 위험성 때문에 잘 안 쓴다고 하여 sha256을 추가해봤습니다

    sign1 = data[511:512].hex() #.encode("hex") -> Attribute error -> .hex()로 변경
    sign2 = data[510:511].hex()

    print("\nMBR Safety Check:")

    print("- MBR Signature: 0x" +sign1+sign2)

    sign = data[510:512].hex()  #signature 값(16진수)

    if sign == "55aa":  #signature 기본값 0x55AA 판별
        print("- Check: Safety\n")   
    else:
        print("- Check: Warning\n")


def MBRBoot():
    print("MBR ETC Information:")
    print("- MBR Device Signature: 0x"+data[440:444].hex())
    print("- MBR Error Message Offset: 0x"+data[437:440].hex())

MBRTime()
MBRSig()
MBRBoot()

mbr.close()
