import time
def MBRTime():
            printf("[+] MBR Analysis Time:"+time.ctime())
MBRTime()

def MBRSig():
    mbr=open("mbr.bin",'rb')
    data=mbr.read()

    sign=data[510:512].encode("hex")
    if sign == "55AA":


    else:
             sign="55AA"


MBRSig()

def MBRBoot():
    mbr=open("mbr.bin",'rb')
    data = mbr.read()



def MBRPt():
    mbr=open("mbr.bin", 'rb')
    data=mbr.read()
    bf1 = data[446:447].encode("hex")

    if bf1 == "80":

    else:
        bf1 == "80"
