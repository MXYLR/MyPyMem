import ctypes as crt
global rpm
global op
global wpm
rpm = crt.windll.LoadLibrary('kernel32.dll').ReadProcessMemory
wpm= crt.windll.LoadLibrary('kernel32.dll').WriteProcessMemory
op = crt.windll.LoadLibrary('kernel32.dll').OpenProcess
class Read:
    """
   Read系列函数实现基类
   """
    
    @classmethod
    def ReadData(cls, pid, addr, length):
        """
       读取数据
       :param pid:进程id
       :param addr:地址,字符串描述，数值为16进制，包含0x
       :param length:二进制数据的长度

       :return:返回读取到的数据bytes
       """
       
        addr0 = int(addr,base=16)
        buffer = crt.create_string_buffer(length)
        re = crt.c_uint32()         
        HANDLE = crt.c_uint32(op(crt.c_uint32(0xffff), crt.c_bool(False), crt.c_uint32(pid)))
        rpm(HANDLE, crt.c_void_p(addr0), crt.byref(buffer), crt.c_uint32(length), crt.byref(re))
        return  buffer.value

    @classmethod
    def ReadDouble(cls, pid, addr):
        """
       读取Double
       :param pid:进程id
       :param addr:地址,字符串描述，数值为16进制，包含0x
       :return:返回读取到的数据bytes
       """
        addr0 = int(addr,base=16)
        buffer = crt.create_string_buffer(8)
        re = crt.c_uint32()         
        HANDLE = crt.c_uint32(op(crt.c_uint32(0xffff), crt.c_bool(False), crt.c_uint32(pid)))
        rpm(HANDLE, crt.c_void_p(addr0), crt.byref(buffer), crt.c_uint32(8), crt.byref(re))
        return  buffer.value
    @classmethod
    def ReadFloat(cls, pid, addr):
        """
        读取float
        :param pid:进程id
        :param addr:地址,字符串描述，数值为16进制，包含0x
        :return:返回读取到的数据bytes
        """
        addr0 = int(addr,base=16)
        buffer = crt.create_string_buffer(4)
        re = crt.c_uint32()         
        HANDLE = crt.c_uint32(op(crt.c_uint32(0xffff), crt.c_bool(False), crt.c_uint32(pid)))
        rpm(HANDLE, crt.c_void_p(addr0), crt.byref(buffer), crt.c_uint32(4), crt.byref(re))
        return  buffer.value
    @classmethod
    def ReadInt(cls, pid, addr, mytype):
        """
       读取Int
       :param pid:进程id
       :param addr:地址,字符串描述，数值为16进制，包含0x
       :param mytype:0：4字节,1:2字节,2:1字节
       :return:返回读取到的数据bytes
       """
        addr0 = int(addr,base=16)
        if mytype==0:
            length=4
        elif mytype==1:
            length=2
        else:
            length=1
        buffer = crt.create_string_buffer(length)
        re = crt.c_uint32()         
        HANDLE = crt.c_uint32(op(crt.c_uint32(0xffff), crt.c_bool(False), crt.c_uint32(pid)))
        rpm(HANDLE, crt.c_void_p(addr0), crt.byref(buffer), crt.c_uint32(4), crt.byref(re))
        return  buffer.value


class Write:
    """
    Write系列函数实现基类
    """

    @classmethod
    def WriteData(cls, pid, addr, data):
        """
        读取数据
        :param pid:进程id
        :param addr:地址,字符串描述，数值为16进制，包含0x
        :param data:二进制数据16进制字符串
        :return:true或者false
        """
        addr0 = int(addr,base=16)
        bdata=bytes(data,encoding='ascii')
        length=len(bdata)
        re = crt.c_uint32()         
        HANDLE = crt.c_uint32(op(crt.c_uint32(0xffff), crt.c_bool(False), crt.c_uint32(pid)))
        r=wpm(HANDLE, crt.c_void_p(addr0), crt.byref(bdata), crt.c_uint32(length), crt.byref(re))
        if r!=0:
            return True
        else:
            return False
    @classmethod
    def WriteDouble(cls, pid, addr, v):
        """
        写入Double
        :param pid:进程id
        :param addr:地址,字符串描述，数值为16进制，包含0x
        :param v:双精度浮点数
        :return:true或者false
        """
        addr0 = int(addr,base=16)
        mydata=v.to_bytes(8,'little')
        buffer=crt.create_string_buffer(mydata,8)
        re = crt.c_uint32()         
        HANDLE = crt.c_uint32(op(crt.c_uint32(0xffff), crt.c_bool(False), crt.c_uint32(pid)))
        r=wpm(HANDLE, crt.c_void_p(addr0), crt.byref(buffer), crt.c_uint32(8), crt.byref(re))
        if r!=0:
            return True
        else:
            return False
    @classmethod
    def WriteFloat(cls, pid, addr, v):
        """
        写入float
        :param pid:进程id
        :param addr:地址,字符串描述，数值为16进制，包含0x
        :param v:单精度浮点数
        :return:true或者false
        """
        addr0 = int(addr,base=16)
         
        mydata=v.to_bytes(4,'little')
        buffer=crt.create_string_buffer(mydata,4)
        re = crt.c_uint32()         
        HANDLE = crt.c_uint32(op(crt.c_uint32(0xffff), crt.c_bool(False), crt.c_uint32(pid)))
        r=wpm(HANDLE, crt.c_void_p(addr0), crt.byref(buffer), crt.c_uint32(4), crt.byref(re))
        if r!=0:
            return True
        else:
            return False  
    @classmethod
    def WriteInt(cls, pid, addr, mytype, v):
        """
        写入Int
        :param pid:进程id
        :param addr:地址,字符串描述，数值为16进制，包含0x
        :param mytype:0：4字节,1:2字节,2:1字节
        :param v:整形数值
        :return:true或者false
        """
        addr0 = int(addr,base=16)
        if mytype==0:
            length=4
        elif mytype==1:
            length=2
        else:
            length=1
        mydata=v.to_bytes(length,'little')
        buffer=crt.create_string_buffer(mydata,length)
        re = crt.c_uint32()         
        HANDLE = crt.c_uint32(op(crt.c_uint32(0xffff), crt.c_bool(False), crt.c_uint32(pid)))
        r=wpm(HANDLE, crt.c_void_p(addr0), crt.byref(buffer), crt.c_uint32(length), crt.byref(re))
        if r!=0:
            return True
        else:
            return False


