from baseApp.models import Symptom,Point

def getFirstSightPlan(userqueryinfo,userinfo):
    disname = userqueryinfo['disname']
    list = []
    if (userinfo):
        gender = userinfo[0].gender
        data = Symptom.objects.filter(Symptom__contains=disname)
        if data :
            index = 1
            for item in data:
                dictionary = {}
                if(item.Symptom.find("|") != -1):
                    dictionary["symptom"] = item.Symptom.split('|') #list
                else:
                    dictionary["symptom"] = item.Symptom
                dictionary["meridian"] = item.Meridian
                dictionary["id"] = index
                index += 1
                list.append(dictionary)
        else:
            return list
    # 根据用户已有信息获取"初视"治疗方案,将涉及到的经络的病症返给用户，使其选出最为接近的一条经络，再返回该经络的易读穴位即可
    return list

def getFirstPlan(meridian):
    list = []
    dict = {}
    if meridian:
        data = Point.objects.filter(Meridian=meridian)
        if data :
            for item in data:
                dictionary = {}
                dictionary["Point"] = item.Point
                dictionary["PointName"] = item.PointName
                dictionary["PointStep"] = item.PointStep
                dictionary["PointPosition"] = item.PointPosition
                list.append(dictionary)
        return list
    else:
        return dict