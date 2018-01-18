from baseApp.models import Symptom
def getFirstSightPlan(userqueryinfo,userinfo):
    disname = userqueryinfo['disname']
    if (userinfo):
        gender = userinfo[0].gender
        data = Symptom.objects.filter(Symptom__contains=disname)
        for item in data:
            print(item.Symptom +" -- 经络 :"+item.MeridianName )
    # 根据用户已有信息获取"初视"治疗方案,将涉及到的经络的病症返给用户，使其选出最为接近的一条经络，再返回该经络的易读穴位即可
    message = {
        'recCode': "successed",
        'openid': ''
    }
    return message