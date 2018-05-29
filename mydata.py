
class RawData:
    def __init__(self):
        self.Singnal = -1
        self.Delta = -1
        self.Theta = -1
        self.LowAlpha = -1
        self.HighAlpha = -1
        self.LowBeta = -1
        self.HighBeta = -1
        self.LowGamma = -1
        self.MiddleGamma = -1
        self.Attention = -1
        self.Meditation = -1
        self.Singnal = -1 ##(0到100之间)
        self.Singnal = -1 ##(0到100之间)
    def getTransData(self,data):
        self.Delta = int(data[8]) << 16 | int(data[9]) << 8 | int(data[10])
        self.Theta = int(data[11]) << 16 | int(data[12]) << 8 | int(data[13])
        self.LowAlpha = int(data[14]) << 16 | int(data[15]) << 8 | int(data[16])
        self.HighAlpha = int(data[17]) << 16 | int(data[18]) << 8 | int(data[19])
        self.LowBeta = int(data[20]) << 16 | int(data[21]) << 8 | int(data[22])
        self.HighBeta = int(data[23]) << 16 | int(data[24]) << 8 | int(data[25])
        self.LowGamma = int(data[26]) << 16 | int(data[27]) << 8 | int(data[28])
        self.MiddleGamma = int(data[29]) << 16 | int(data[30]) << 8 | int(data[31])
        self.Attention = int(data[33])
        self.Meditation = int(data[35])

curDataType=""
curDataByteNum = 0
curData= []
curDataLength = 0

def ReadData(data):
    global curDataType,curDataByteNum,curData,curDataLength
    if (curDataByteNum < 2 and data == 0xAA):
        #log.Printf("find 0xAA", curDataByteNum)
        if curDataByteNum == 0:
            # 开始计数
            curData = bytearray(128)
            curData[1] = 0xAA
            curDataByteNum = 1
            return
    if curDataByteNum == 1:
    # 第二个SYNC
    # log.Printf("valid success", curDataByteNum)
        curData[2] = 0xAA
        curDataByteNum = 2
        return
    if (curDataByteNum < 2 and data != 0xAA ):
        # log.Printf("valid fail", curDataByteNum)
        curDataByteNum = 0
        return
    if curDataByteNum >= 2 :
        # log.Printf("valid ok", curDataByteNum, curDataType)
        curDataByteNum += 1
        #log.Printf("%x", curData[1:curDataByteNum], curDataByteNum)
        curData[curDataByteNum] = data
    if curDataByteNum == 3:
        if data == 0x20 :
            # log.Printf("find big")
            curDataByteNum +=1
            curDataType = "big"
            return
    else:
        # else if (data & 0xFF == 0x04)  {
        curDataType = "small"
        #暂时不读取
        curDataType = ""
        curDataByteNum = 0
        return
    if curDataType == "big" and curDataByteNum > 37 :
        #结束
        #log.Printf("big:%x", curData[1:curDataByteNum])
        bigdata = RawData()
        bigdata.getTransData(curData[1:curDataByteNum])
        print(bigdata)
        #getTransData(curData[1:curDataByteNum])
        curDataByteNum = 0
        curDataType = ""

