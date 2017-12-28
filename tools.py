from baseApp.models import LoginDatas

def getUserPassword(username,password):
    data = LoginDatas.objects.filter(Username=username,Password=password)
    if not data :
        return "0"
    return "1"
