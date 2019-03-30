import hashlib

# трафик между клиентом и NAS server
secret = "DEAF99"
secret_dec = [68, 69, 65, 70, 57, 57]
ID = 0x02   # Request
password = 0  # 42CA11
#Request
Auth = [0xff, 0x97, 0x9f, 0xae, 0x4f, 0xba, 0x32, 0x74, 0x60, 0x5b, 0x88, 0x7c, 0x4e, 0x92, 0xc1, 0x01]
Send_Val = "8804a297678e813c88fca0cd3dd499e3" #Responce

def GetHash(str):
    hash = hashlib.md5(bytes(str))
    dec_mess = hash.hexdigest()
    return dec_mess

def GenNum(list, i):
    for n in range(48, 71):
        list[i] = n
        if(i > 0):
            GenNum(list, i - 1)
        mess = []
        mess.append(ID)
        mess += list + Auth
        decr = GetHash(mess)

        if (decr == Send_Val):
            print(list)

def GetPassword():
    for i in range(6):
        GenNum([0 for i in range(i+1)], i)


GetPassword()
