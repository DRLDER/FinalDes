from django.shortcuts import render


def test(request):
    content = {}
    content['test1'] = "简颢科技"
    return render(request, 'MainPage.html', content)


def showInfo(request):
    name = request.POST.get("username")
    passwd = request.POST.get("password")
    content = {}
    content['username'] = name
    content['password'] = passwd
    return render(request, 'ShowYourInfo.html',content)
