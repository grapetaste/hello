f = open('\\\\.\\PhysicalDrive1','rb')
f.seek(0) #커서를 맨처음으로 이동

def HtoD(a, b, c):  #Hex to Dec(해당 위치, 기준점, 해당 크기)
    f.seek(a, b)   #해당 위치 이동
    str = f.read(c).hex()   #해당 크기 만큼 읽기
    conv = ''.join([str[i-2:i] for i in range(len(str), 0, -2)])  #little-endian 변환
    result = int(conv, 16)  #10진수 변환
    return result

st = 512    #sector

VBR_l = HtoD(0x1c6, 0, 4)

f.seek(VBR_l*st)    #VBR 섹터로 이동
S_o_M = HtoD(0x30, 1, 8)   #Start Cluster for $MFT

f.seek(HtoD(0x1c6, 0, 4)*st)    #VBR 섹터로 이동
S_p_C = HtoD(0x0D, 1, 2)   #Sector per Cluster

MFT_l = S_o_M * S_p_C + VBR_l   #MBT 위치

F_N = 48    #$File_Name
f.seek((MFT_l + F_N) * st)    #$File_Name 위치로 이동
print(f.tell()/512)
S_o_f = HtoD(0x30, 1, 8)

offset = 0
f_size = getsize(f) #파일 사이즈 얻는 코드

while f_size = offset:  #파일사이즈가 0이 될 때까지 반복
    Read_file(test.001)    #파일 읽기

index = 0

while data_size == 0:
    if data[:16] == 'd0cf11e0a1b11ae1':    #hwp
        변수선언=한글시그니처위치부터 데이터크기
        파일을 따로 하나 만들기 .hwp로 저장
        for i in range(0, [파일크기])
            liness[i] = lines[i].split("숫자", % n번째 숫자) #전체 파일에서 저장된 한글파일 빼는 코드

    elif data[:8] == '504b0304':    #피피티, 엑셀, 워드 시그니처가 같기 때문에 각 시그니처 위치를 분리시키기 위한 코드
        if '707074' in data:    #pptx
            변수선언=index1위치부터 데이터크기
            파일을 따로 하나 만들기 .pptx로 저장->if os.path.isdir(파이썬 파일내용 크기별로 저장)
            for i in range(0, [파일크기])
            liness[i] = lines[i].split("숫자", % n번째 숫자)

        elif '776f7264' in data:    #docx
            변수선언=index2위치부터 데이터크기
            파일을 따로 하나 만들기 .docx로 저장
            for i in range(0, [파일크기])
            liness[i] = lines[i].split("숫자", % n번째 숫자)


        elif '776f726b626f6f6b' in data or '776f726b626f6f6b' in data:    #xlsx
            변수선언=index3위치부터 데이터크기
            파일 생성 .xlsx로 저장
            for i in range(0, [파일크기])
            liness[i] = lines[i].split("숫자", % n번째 숫자)
