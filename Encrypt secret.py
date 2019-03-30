import hashlib
# трафик между NAS и сервером
# Accounting-Response
Code = 0x05
ID = 0x2e
Length = 0x00
leng2 = 0x14
# Accounting-Request
Auth = [0x8e, 0xad, 0x44, 0x0e, 0xcc, 0x45, 0x1a, 0xf7, 0x94, 0xcb, 0xc6, 0x41, 0x51, 0x78, 0x88, 0x17]
secret = []  # DEAF99
mess_for_hash = []
Chall_Auth = "f91afe56c6f36e69893cf4c41baae06e" # Accounting-Response

count = 0

mess_for_hash.append(Code)
mess_for_hash.append(ID)
mess_for_hash.append(Length)
mess_for_hash.append(leng2)
mess_for_hash += Auth

def GetHash(str):
    hash = hashlib.md5(bytes(str))
    dec_mess = hash.hexdigest()
    return dec_mess

def GenNum(list, i):
    for n in range(48, 71):
        list[i] = n
        if(i > 0):
            GenNum(list, i - 1)
        mess = GetHash(mess_for_hash + list)

        if (mess == Chall_Auth):
            print(list)

def GetSecret():
    for i in range(6):
        GenNum([0 for i in range(i+1)], i)

GetSecret()
