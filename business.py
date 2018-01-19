from baseApp.models import Symptom

def getFirstSightPlan(userqueryinfo,userinfo):
    disname = userqueryinfo['disname']
    list = []
    if (userinfo):
        gender = userinfo[0].gender
        data = Symptom.objects.filter(Symptom__contains=disname)
        if data :
            for item in data:
                dictionary = {}
                if(item.Symptom.find("|") != -1):
                    dictionary["symptom"] = item.Symptom.split('|') #list
                else:
                    dictionary["symptom"] = item.Symptom
                dictionary["meridian"] = item.Meridian
                list.append(dictionary)
        else:
            return list
    # 根据用户已有信息获取"初视"治疗方案,将涉及到的经络的病症返给用户，使其选出最为接近的一条经络，再返回该经络的易读穴位即可
    return list