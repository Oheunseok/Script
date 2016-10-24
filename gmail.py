global tag_list,field_list,value_list
import xml.etree.ElementTree as ET
import smtplib
from  Func import *

from email.mime.text import MIMEText

class Mail:
    def __init__(self):
        self.loginID, self.loginPW="shin1sub2","2fjsrjtehhag"
        self.senderAddr,self.recipientAddr="secretfice@naver.com","ssuby11@naver.com"
        self.text=""
    def login(self):
        pass
        self.loginID, self.loginPW = input("구글ID"), input("PW")
    def write(self):
        self.recipientAddr = input("받는 사람")
        text = "본문 샬라샬라"
        text = ""
        push = True
        print("메일내용을 적으세요('send'를 누르면 발송)")
        while (push):
            s = input()
            if (s == "send"):
                push = False
                break
            self.text += s + '\n'
    def add(self,tag,value):

        size = len(tag)
        print(value)

        i=0
        for i in range(len(value)):
            if (i % size == 0):
                self.text += "--------------------------------\n"
                self.text += tag[i % size] + " --> " + value[i] + '\n'
                self.text += "--------------------------------\n"
            else:
                self.text += tag[i % size] + " --> " + value[i] + '\n'
            i += 1

        print(self.text)
    def send(self):
        msg = MIMEText(self.text, _charset="utf8")
        msg['Subject'] = input("제목입력")  # 제목
        msg['From'] = self.senderAddr  # 발신자
        msg['to'] = self.recipientAddr  # 수신자

        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.login(self.loginID, self.loginPW)
        s.sendmail(self.senderAddr, self.recipientAddr, msg.as_string())

        s.quit()

    def revMail(self,time,recipient):
        self.loginID, self.loginPW = "shin1sub2", "2fjsrjtehhag"
        self.recipientAddr=recipient



        msg = MIMEText("설정하신 알람시간(%s)이 경과했습니다. 늦지 않게 주의하세요"%time, _charset="utf8")
        msg['Subject'] = "지정한 알람시간이 됬습니다"  # 제목
        msg['From'] = self.senderAddr  # 발신자
        msg['to'] = self.recipientAddr  # 수신자

        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.login(self.loginID, self.loginPW)
        s.sendmail(self.senderAddr, self.recipientAddr, msg.as_string())

        s.quit()

# m=Mail()
# m.login()
# m.write()
# m.send()






