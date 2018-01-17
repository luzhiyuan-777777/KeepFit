def getFirstSightPlan(userqueryinfo,userinfo):
    disname = userqueryinfo['disname']
    if (userinfo):
        gender = userinfo[0].gender
    # 根据用户已有信息获取"初视"治疗方案
    message = {
        'recCode': "successed",
        'openid': ''
    }
    return message