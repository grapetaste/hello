def MBRsignature():
    mbr=open("mbr.bin",'rb')
    mbr_data=mbr.read()

    sig1=mbr_data[511:512].encode("hex")
    sig2=mbr_data[510:511].encode("hex")

    print("[+} MBR Signature Sheck")
    print("[-] MBR Signature: 0x"+sig1+sig2)

    sig =mbr_data[510:512].encode("hex")

    if sig == '55aa':
        print("[-] Safety Check : Safety\n")

    else:
        print("[-] Safety Check : Warning\n")

    mbr.close()

MBRsignature()








