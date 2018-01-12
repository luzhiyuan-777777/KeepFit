
from baseApp.models import LoginDatas,WxUserInfo
import json
def getUserPassword(username,password):
    data = LoginDatas.objects.filter(Username=username,Password=password)
    if not data :
        return "0"
    return "1"

def isUserInDb(username):
    data = LoginDatas.objects.filter(Username=username)
    if not data :
        return "0"
    return "1"
def string2json(data):
    return json.loads(data)

def wxUser2Db(userInfoJson,userOpenId):
    nickName = userInfoJson['nickName']
    gender = userInfoJson['gender']
    language = userInfoJson['language']
    city = userInfoJson['city']
    province = userInfoJson['province']
    avatarUrl = userInfoJson['avatarUrl']
    data = WxUserInfo(useropenid=userOpenId,nickname=nickName,gender=gender,language=language,city=city,province=province,avatarUrl=avatarUrl,validflag="1")
    data.save()

def getWxUserInfo(useropenid):
    data = WxUserInfo.objects.filter(useropenid=useropenid)
    if data:
        return data
    else:
        return ""
