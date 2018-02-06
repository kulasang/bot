# -*- coding: utf-8 -*- kulasang

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

cl = LINETCR.LINE()
cl.login(token="EpZRKmh6jdQUubSsVhr6.0P3FlAwpvyaZKXTQhGnEXG.SceZ3eQDqdNigJh1jStNhPDsQ3/sp6UZyKOb3jg2aL0=")
cl.loginResult()

ki = kk = kc = cl 

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage10 ="""
╔═════════════════
║ ─┅═✥ คำสั่งบอท ✥═┅─
╠═════════════════
╠❂➣ ดูรูป @
╠❂➣ ดูปก @
╠❂➣ ดู Mid @
╠❂➣ ดูโปรไฟล์ @
╠❂➣ ดูชื่อคนอื่น @
╠❂➣ ข้อมูลคนอื่น @
╠❂➣ ข้อมูลติดต่อ @
╠❂➣ สถานะคนอื่น @
╠❂➣ ลิงค์รูปคนอื่น @
╠❂➣ ลิงค์ปกคนอื่น @
╠❂➣ ข้อมูลกลุ่ม
╠❂➣ ปิดลิงค์กลุ่ม
╠❂➣ แท็กทั้งหมด
╠❂➣ เช็คบอททำงาน
╠❂➣ ส่งของขวัญ
╠❂➣ ยกเลิกเชิญ
╠❂➣ หยุด
╠═════════════════
╠❂➣ บอทตั้งจุดอ่าน
╠❂➣ บอทดูคนอ่าน
╚═════════════════
 Heart CookieRun Tⓗ
 ツ จอมขมังเวทย์ ™
"""
KAC=[cl,ki,kk,kc]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid]
admin=["ud29ddf2da58f558033931b6a1e035ec6"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':True,
    'message':"ขอบคุณที่เพิ่มฉันเป็นเพื่อน\nHeart CookieRun Tⓗ\nกฏกติกาของกลุ่ม\nhttps://sites.google.com/view/cookierun/home\n\nหากคุณต้องการเข้าร่วมกลุ่มส่งใจคุกกี้รัน\nติดต่อแอดมินกลุ่ม\nhttp://line.me/ti/p/~ed-kulasang",
    "lang":"JP",
    "comment":"Heart CookieRun Tⓗ",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":True,
    "atjointicket":False,
    }

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

setTime = {}
setTime = wait2['setTime']

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d ชม. %02d นาที %02d วินาที' % (hours, mins, secs)    

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False
	
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error		

#-------------------------------------------------------------------------------------

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
            cl.acceptGroupInvitation(op.param1)
            cl.sendText(op.param1, "ขณะนี้มีการเชิญสมาชิกเข้ากลุ่ม")
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []

        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
												
#----------------------------------------------------------------------ส่งข้อมูลเข้ากลุ่ม
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                           cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"❂ ชื่อที่แสดง :\n" + msg.contentMetadata["displayName"] + "\n\n❂ MID :\n" + msg.contentMetadata["mid"] + "\n\n❂ สถานะข้อความ :\n" + contact.statusMessage + "\n\n❂ ลิงค์รูปส่วนตัว :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n❂ ลิงค์รูปปก :\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"❂ ชื่อที่แสดง :\n" + contact.displayName + "\n\n❂ MID :\n" + msg.contentMetadata["mid"] + "\n\n❂ สถานะข้อความ :\n" + contact.statusMessage + "\n\n❂ ลิงค์รูปส่วนตัว :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n❂ ลิงค์รูปปก :\n" + str(cu))
												
#--------------------------------------------------------------------------------------------------------------												
            elif msg.text in ["บอท","บอด","Bot","bot"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage10)
                else:
                    cl.sendText(msg.to,helpt)
											
            elif msg.text in ["ปิดลิงค์กลุ่ม","Link off"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดลิงค์กลุ่มสำเร็จค่ะ")
                    else:
                        cl.sendText(msg.to,"ปิดแล้ว")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ไม่สามารถใช้นอกกลุ่มได้")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
				
            elif msg.text.lower() == 'ข้อมูลกลุ่ม':
                    group = cl.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md = "═════ ข้อมูลกลุ่ม ═════\n❂ ชื่อกลุ่ม :\n" + group.name + "\n\n❂ ไอดีกลุ่ม :\n" + group.id + "\n\n❂ ผู้สร้างกลุ่ม :\n" + gCreator + "\n\n❂ รูปกลุ่ม :\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nลิงค์กลุ่ม: เปิด"
                    else: md += "\n\nลิงค์กลุ่ม: ปิด"
                    if group.invitee is None: md += "\nสมาชิกทั้งหมด: " + str(len(group.members)) + " คน" + "\nไม่รับคำเชิญ: 0 คน"
                    else: md += "\nสมาชิกทั้งหมด : " + str(len(group.members)) + " คน" + "\nไม่รับคำเชิญ: " + str(len(group.invitee)) + " คน"
                    cl.sendText(msg.to,md)

								
            elif msg.text in ["สมน้ำหน้า","5555","55555"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["อิอิ","ชอบใจ"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["เศร้า"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["ชี้หน้า"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["โมโห","โกรธ"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["กรุณา","เมตตา"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in [";ว๊าย","ว้าย","ตกใจ"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["ฮ่าๆ","555","หัวเราะ"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["อืม","อืมม"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["ยินดีต้อนรับ","Welcome","Wc","wc"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
																		
#-----------------------------------------------runtime-------------------------------										
										
            elif msg.text.lower() == 'เช็คบอททำงาน':
                eltime = time.time() - mulai
                van = "═ บอททำงานมาแล้ว ═\n"+waktu(eltime)
                cl.sendText(msg.to,van)				
						
            elif msg.text.lower() == 'บอทตั้งจุดอ่าน':
                if msg.toType == 2:
                    cl.sendText(msg.to, "ตั้งจุดอ่าน/ลบจุดอ่าน" + datetime.now().strftime('\n%Y/%m/%d - %H:%M:%S'))
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d - %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print wait2
                        
            elif msg.text.lower() == 'บอทดูคนอ่าน':
                if msg.toType == 2:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "❂ ที่เห็นครั้งล่าสุด:%s\n\n\n❂ ที่เห็นครั้งสุดท้าย:\n%s\n\n═══════════════\nเปิดดูคนอ่าน:\n[%s]\n═══════════════\nBy: Heart CookieRun Tⓗ" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        print "ReadPoint Set..."
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d - %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print wait
                        cl.sendText(msg.to, "ตั้งจุดอ่านโดยอัตโนมัติ:" + datetime.now().strftime('\n%Y-%m-%d - %H:%M:%S'))
                    else:
                        cl.sendText(msg.to, "ไม่ได้ตั้งจุดคนอ่านค่ะ")			
								
            elif "แท็กทั้งหมด" == msg.text.lower():
                 group = cl.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                 if jml > 200  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "จำนวน: " + str(jml) +  " คน"
                 cnt.to = msg.to
                 cl.sendMessage(cnt)			
									
            elif "ดูโปรไฟล์" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"❂ ชื่อที่แสดง :\n" + contact.displayName + "\n❂ สถานะข้อความ :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"❂ รูปส่วนตัว : " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"❂ รูปปก : " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass	
									
            elif "ข้อมูลคนอื่น" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"❂ ชื่อที่แสดง :\n" + contact.displayName + "\n\n❂ Mid :\n" + contact.mid + "\n\❂ nสถานะข้อความ :\n" + contact.statusMessage + "\n\n❂ ลิงค์รูปส่วนตัว :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n❂ ลิงค์รูปปก :\n" + str(cu))
                except:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))
										
            elif "สถานะคนอื่น" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "=== ❂ สถานะข้อความ ❂ ===\n" + contact.statusMessage)
                except:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
										
            elif "ดูชื่อคนอื่น" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "=== ❂ ชื่อที่แสดง ❂ ===\n" + contact.displayName)
                except:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)			
										
            elif "ข้อมูลติดต่อ" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)  										

            elif msg.text in ["หยุด"]:
	            cl.sendText(msg.to,"Stop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nStop!\nThank You :)")
							
            elif "ลิงค์ปกคนอื่น @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("ลิงค์ปกคนอื่น @","")    
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"ไม่พบที่อยู่ติดต่อ")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)          
                            path = str(cu)
                            cl.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
								
            elif "ลิงค์รูปคนอื่น @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("ลิงค์รูปคนอื่น @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"ไม่พบที่อยู่ติดต่อ")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"					
								
            elif ("ดู Mid " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)		
									
            elif msg.text in ["ส่งของขวัญ","ของขวัญ"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)									
								
#-----------------------------------------------ล้างกลุ่ม--------------------------------													
#            elif "Cleanse" in msg.text:
#                if msg.toType == 2:
#                    print "ok"
#                    _name = msg.text.replace("Cleanse","")
#                    gs = ki.getGroup(msg.to)
#                    gs = kk.getGroup(msg.to)
#                    gs = kc.getGroup(msg.to)
#                    ki.sendText(msg.to,"Just some casual cleansing ô")
#                    kk.sendText(msg.to,"Group cleansed.")
#                    kc.sendText(msg.to,"Fuck You All")
#                    targets = []
#                    for g in gs.members:
#                        if _name in g.displayName:
#                            targets.append(g.mid)
#                    if targets == []:
#                        ki.sendText(msg.to,"Not found.")
#                        kk.sendText(msg.to,"Not found.")
#                        kc.sendText(msg.to,"Not found.")
#                    else:
#                        for target in targets:
#                            try:
#                                klist=[ki,kk,kc]
#                                kicker=random.choice(klist)
#                                kicker.kickoutFromGroup(msg.to,[target])
#                                print (msg.to,[g.mid])
#                            except:
#                                ki.sendText(msg.to,"Group cleanse")
#                                kk.sendText(msg.to,"Group cleanse")
#                                kc.sendText(msg.to,"Group cleanse")
#-----------------------------------------------ล้างกลุ่ม--------------------------------
#            elif "Nk " in msg.text:
#                  if msg.from_ in admin:
#                       nk0 = msg.text.replace("Nk ","")
#                       nk1 = nk0.lstrip()
#                       nk2 = nk1.replace("@","")
#                       nk3 = nk2.rstrip()
#                       _name = nk3
#                       gs = cl.getGroup(msg.to)
#                       targets = []
#                       for s in gs.members:
#                           if _name in s.displayName:
#                              targets.append(s.mid)
#                       if targets == []:
#                           sendMessage(msg.to,"user does not exist")
#                           pass
#                       else:
#                           for target in targets:
#                                try:
#                                    klist=[cl,ki,kk,kc]
#                                    kicker=random.choice(klist)
#                                    kicker.kickoutFromGroup(msg.to,[target])
#                                    print (msg.to,[g.mid])
#                                except:
#                                    ki.sendText(msg.to,"Succes Cv")
#                                    kk.sendText(msg.to,"Fuck You")
#------------------------------------------------------------------
            elif msg.text in ["เมา"]:
                ki.sendText(msg.to,"บางคนว่า ไปดื่มสุรามา")
#------------------------------------------------------------------

            elif msg.text in ["55"]:
                ki.sendText(msg.to,"สวัสดีเพื่อน 􀜁􀅔Har Har􏿿")
#------------------------------------------------------------------

            elif msg.text in ["5555"]:
                ki.sendText(msg.to,"เอิ๊กกก!! 􀜁􀅔Har Har􏿿")
#------------------------------------------------------------------
            elif msg.text in ["สุดยอด","ยอดเยี่ยม","ดีเลิศ"]:
                ki.sendText(msg.to,"สุดยอด 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"ยอดเยี่ยม 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"ดีเลิศ 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#------------------------------------------------------------------	
            elif "ดูปก @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("ดูปก @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"ไม่พบข้อมูลติดต่อ")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"			
#------------------------------------------------------------------
            elif "ดูรูป @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("ดูรูป @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"ไม่พบข้อมูลติดต่อ")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"			
#------------------------------------------------------------------

            elif msg.text in ["ยกเลิกเชิญ","ยกเลิกค้างเชิญ"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"ยกเลิกค้างเชิญสำเร็จค่ะ")
#---------------------ทักคนเข้าออก
#        if op.type == 17:
#          if op.param2 in Bots:
#            return
#          ginfo = cl.getGroup(op.param1)
#          random.choice(KAC).sendText(op.param1, "สวัสดีค่ะ "+ cl.getContact(op.param2).displayName +"\nยินดีต้อนรับเข้าสู่กลุ่ม " + str(ginfo.name))
#          random.choice(KAC).sendText(op.param1, "กรุณาอ่านกฏของกลุ่ม\nและการปิดแจ้งเตือนกลุ่มได้ที่โน้ตค่ะ")
#          random.choice(KAC).sendText(op.param1, "ขอบคุณค่ะ !!!😘")
#          print "MEMBER HAS JOIN THE GROUP"
#        if op.type == 15:
#          if op.param2 in Bots:
#             return
#          random.choice(KAC).sendText(op.param1, "ออกกลุ่มกันอีกแล้ว\nโชคดีนะคะ บ๊ะบาย 😊")
#          print "MEMBER HAS LEFT THE GROUP"
#					
#---------------------ทักคนเข้าออกแบบมีดึงรูป
        if op.type == 17:
          if op.param2 in Bots:
            return
          ginfo = cl.getGroup(op.param1)
          contact = cl.getContact(op.param2)
          image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
          cl.sendImageWithURL(op.param1,image)					
          random.choice(KAC).sendText(op.param1, "สวัสดีค่ะ "+ cl.getContact(op.param2).displayName +"\nยินดีต้อนรับเข้าสู่กลุ่ม " + str(ginfo.name))
          random.choice(KAC).sendText(op.param1, "กรุณาอ่านกฏของกลุ่ม\nและการปิดแจ้งเตือนกลุ่มได้ที่โน้ตค่ะ")
          random.choice(KAC).sendText(op.param1, "ขอบคุณค่ะ !!!^_^")
          print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
          if op.param2 in Bots:
             return
          random.choice(KAC).sendText(op.param1, "โชคดีนะคะ บะบาย ^_^")
          print "MEMBER HAS LEFT THE GROUP"	
																				
#------------------------------------------------------------------
        if op.type == 55:
            print "[NOTIFIED_READ_MESSAGE]"
            try:
                if op.param1 in wait2['readPoint']:
                    Nama = cl.getContact(op.param2).displayName
                    if Nama in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n|| " + Nama
                        wait2['ROM'][op.param1][op.param2] = "|| " + Nama
                        wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                else:
                    cl.sendText
            except:
                pass   


        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)

			