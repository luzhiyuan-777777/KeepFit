from baseApp.models import LoginDatas

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