import datetime
import json
import random

from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from DJ_App.models import user_date, memInfoList, COMECOList, COMECIList, ProductionList, InfoList, \
    administratorNameList


# 主页处理
def index(request):
    res = render(request, 'MainPage.html')
    UPTip = request.COOKIES.get('UPerror')
    if UPTip == "":
        res.set_cookie('UPerror', -1)
        return res
    else:
        return res


# 系统页面处理
def showInfo(request):
    resBack = render(request, 'MainPage.html')
    UPTip = request.COOKIES.get('UPerror')
    UserName = request.session.get('userName')
    content = {}
    content['username'] = UserName
    if UPTip == "":
        resBack.set_cookie('UPerror', -1)
        return resBack
    elif UPTip == '0':
        res = render(request, 'ShowYourInfo.html', content)
        return res
    else:
        resBack.set_cookie('UPerror', -1)
        return resBack


# 主页登录表单处理
def testNameandPass(request):
    name = request.POST.get("username")
    passwd = request.POST.get("password")
    content = {'username': name, 'password': passwd}

    if request.COOKIES.get('UPerror') == '0':
        resJump = render(request, 'ShowYourInfo.html', content)
        return resJump

    if name == "" or passwd == "":
        res = redirect('../')
        res.set_cookie('UPerror', -1)
        return res
    try:
        if user_date.objects.get(username=name):
            print("right username!")
    except user_date.DoesNotExist:
        print("name is error!")
        res = redirect('../')
        res.set_cookie('UPerror', 1)
        return res
    else:
        try:
            if user_date.objects.get(username=name, password=passwd):
                print("right name and pass!")
        except user_date.DoesNotExist:
            print("error pass!")
            res = redirect('../')
            res.set_cookie('UPerror', 2)
            return res
        else:
            res = redirect('../info/')
            res.set_cookie('UPerror', 0)
            request.session['userName'] = content['username']
            return res


# 人员信息表单处理
@csrf_exempt
def textMemInfo(request):
    newdata = {
        'username': request.POST.get('username'),
        'nation': request.POST.get('nation'),
        'NP': request.POST.get('NP'),
        'birthplace': request.POST.get('birthplace'),
        'sex': request.POST.get('sex'),
        'birthday': request.POST.get('birthday'),
        'health': request.POST.get('health'),
        'tel': request.POST.get('tel'),
        'email': request.POST.get('email'),
        'education': request.POST.get('education'),
        'expText': request.POST.get('expText'),
        'writername': request.session.get('userName'),
        'writedate': str(datetime.datetime.now())
    }
    print(newdata['sex'])
    try:
        getDateObj = memInfoList.objects.get(writername=newdata['writername'])
        # getDateObjList= memInfoList.objects.filter(nation='蒙古族')
    except memInfoList.DoesNotExist:
        print('没有查询到相关数据！')
        newdata['Message'] = "您的信息已创建！"
        newDatalist = memInfoList(username=newdata['username'], nation=newdata['nation'],
                                  NP=newdata['NP'],
                                  birthplace=newdata['birthplace'], sex=newdata['sex'],
                                  birthday=newdata['birthday'],
                                  health=newdata['health'], tel=newdata['tel'],
                                  email=newdata['email'],
                                  education=newdata['education'], expText=newdata['expText'],
                                  writername=newdata['writername'], writedate=newdata['writedate'])
        newDatalist.save()
        #下面是对数据库更新的else部分
    else:
        print('查询到相关数据！')
        newdata['Message'] = "您的信息已更新！"
        getDateObj.username = newdata['username']
        getDateObj.nation = newdata['nation']
        getDateObj.NP = newdata['NP']
        getDateObj.birthplace = newdata['birthplace']
        getDateObj.sex = newdata['sex']
        getDateObj.birthday = newdata['birthday']
        getDateObj.health = newdata['health']
        getDateObj.tel = newdata['tel']
        getDateObj.email = newdata['email']
        getDateObj.education = newdata['education']
        getDateObj.expText = newdata['expText']
        getDateObj.writername = newdata['writername']
        getDateObj.writedate = newdata['writedate']
        getDateObj.save()
    return HttpResponse(json.dumps(newdata))
    # 这里我们要做一个数据库的检测，是否相同用户名填写的数据，我们要做一个及时更新。


# 获取自研项目、外方合作、人员工资、税务支出、宣传支出、员工开销等字样的索引值
def getSpecialString(string):
    newStrArr = ['自研项目', '外方合作', '人员工资', '税务支出', '宣传支出', '员工开销']
    getIndex = -1
    for k in range(0, len(newStrArr)):
        if string.find(newStrArr[k]) != -1:
            getIndex = k
            break

    if getIndex == 0:
        getIndexStr = '自研项目'
    elif getIndex == 1:
        getIndexStr = '外方合作'
    elif getIndex == 2:
        getIndexStr = '人员工资'
    elif getIndex == 3:
        getIndexStr = '税务支出'
    elif getIndex == 4:
        getIndexStr = '宣传支出'
    elif getIndex == 5:
        getIndexStr = '员工开销'
    else:
        getIndexStr = '其它'
    return getIndexStr


# 获取自研项目、外方合作等字样的索引值
def getSpecialString2(string):
    newStrArr = ['自研项目', '外方合作']
    getIndex = -1
    for k in range(0, len(newStrArr)):
        if string.find(newStrArr[k]) != -1:
            getIndex = k
            break

    if getIndex == 0:
        getIndexStr = '自研项目'
    elif getIndex == 1:
        getIndexStr = '外方合作'
    else:
        getIndexStr = '其它'
    return getIndexStr


# 公司财务支出表单发布/更新
@csrf_exempt
def ECOOFormUpdate(request):
    newdata = {
        'projectNM': request.POST.get('projectNM'),
        'projectCost': request.POST.get('projectCost'),
        'writername': request.session.get('userName'),
        'writedate': str(datetime.datetime.now()),
    }
    IsExistClass = getSpecialString(newdata['projectNM'])
    if IsExistClass == '其它':
        print('这是一个其它类型，未找到索引！')
        newdata['projectClass'] = IsExistClass

    else:
        print('这是一个''+IsExistClass+''！')
        newdata['projectClass'] = IsExistClass

    try:
        getDateObj = COMECOList.objects.get(ProjectNM=newdata['projectNM'])
    except COMECOList.DoesNotExist:
        print('这是一个新的支出项目')
        newdata['Message'] = '这是一个新的支出项目！'
        newDatalist = COMECOList(ProjectNM=newdata['projectNM'], ProjectCost=float(newdata['projectCost']),
                                 writername=newdata['writername'], writedate=newdata['writedate'],
                                 ProjectClass=newdata['projectClass'])
        newDatalist.save()
        return HttpResponse(json.dumps(newdata))
    #修改数据库部分，其中包含原数据库信息不便展示
    else:
        print('这是一个已经产生的支出项目')
        newdata['Message'] = '这是一个已经产生的支出项目，我们已实现更新！'
        getDateObj.ProjectCost = float(newdata['projectCost'])
        getDateObj.ProjectClass = newdata['projectClass']
        getDateObj.writername = newdata['writername']
        getDateObj.writedate = newdata['writedate']
        getDateObj.save()
        return HttpResponse(json.dumps(newdata))


# 公司财务收入表单发布/更新
@csrf_exempt
def ECOIFormUpdate(request):
    newdata = {
        'ProjectNM': request.POST.get('ProjectNM'),
        'ProjectGot': request.POST.get('ProjectGot'),
        'writername': request.session.get('userName'),
        'writedate': str(datetime.datetime.now()),
    }
    IsExistClass = getSpecialString2(newdata['ProjectNM'])
    if IsExistClass == '其它':
        print('这是一个其它类型，未找到索引！')
        newdata['projectClass'] = IsExistClass

    else:
        print('这是一个''+IsExistClass+''！')
        newdata['projectClass'] = IsExistClass

    try:
        getDateObj = COMECIList.objects.get(ProjectNM=newdata['ProjectNM'])
    except COMECIList.DoesNotExist:
        print('这是一个新的收入项目')
        newdata['Message'] = '这是一个新的收入项目！'
        newDatalist = COMECIList(ProjectNM=newdata['ProjectNM'], ProjectGot=float(newdata['ProjectGot']),
                                 writername=newdata['writername'], writedate=newdata['writedate'],
                                 ProjectClass=newdata['projectClass'])
        newDatalist.save()
        return HttpResponse(json.dumps(newdata))
    else:
        print('这是一个已经产生的收入项目')
        newdata['Message'] = '这是一个已经产生的收入项目，我们已实现更新！'
        getDateObj.ProjectGot = float(newdata['ProjectGot'])
        getDateObj.ProjectClass = newdata['projectClass']
        getDateObj.writername = newdata['writername']
        getDateObj.writedate = newdata['writedate']
        getDateObj.save()
        return HttpResponse(json.dumps(newdata))


# 公司财务的动态更新
@csrf_exempt
def ECOIOListUpdate(request):
    newdata = {}
    # 这里我们获取支出的相关项目
    # 获取自研项目0、外方合作1、人员工资2、税务支出3、宣传支出4、员工开销5、其它-1
    getECOO_0 = COMECOList.objects.filter(ProjectClass='自研项目')
    getECOO_1 = COMECOList.objects.filter(ProjectClass='外方合作')
    getECOO_2 = COMECOList.objects.filter(ProjectClass='人员工资')
    getECOO_3 = COMECOList.objects.filter(ProjectClass='税务支出')
    getECOO_4 = COMECOList.objects.filter(ProjectClass='宣传支出')
    getECOO_5 = COMECOList.objects.filter(ProjectClass='员工开销')
    getECOO_sub1 = COMECOList.objects.filter(ProjectClass='其它')
    ###########################################################
    # 这里我们获取收入的相关项目
    # 获取自研项目0、外方合作1、其它-1
    getECOI_0 = COMECIList.objects.filter(ProjectClass='自研项目')
    getECOI_1 = COMECIList.objects.filter(ProjectClass='外方合作')
    getECOI_sub1 = COMECIList.objects.filter(ProjectClass='其它')

    ############################################################
    # 这里是支出计量
    # 获取到6类项目的支出情况（自研项目0、外方合作1、人员工资2、税务支出3、宣传支出4、员工开销5、其它-1）

    ECOOsum0 = 0
    for x in range(0, len(getECOO_0)):
        ECOOsum0 += getECOO_0[x].ProjectCost

    ECOOsum1 = 0
    for x1 in range(0, len(getECOO_1)):
        ECOOsum1 += getECOO_1[x1].ProjectCost

    ECOOsum2 = 0
    for x2 in range(0, len(getECOO_2)):
        ECOOsum2 += getECOO_2[x2].ProjectCost

    ECOOsum3 = 0
    for x3 in range(0, len(getECOO_3)):
        ECOOsum3 += getECOO_3[x3].ProjectCost

    ECOOsum4 = 0
    for x4 in range(0, len(getECOO_4)):
        ECOOsum4 += getECOO_4[x4].ProjectCost

    ECOOsum5 = 0
    for x5 in range(0, len(getECOO_5)):
        ECOOsum5 += getECOO_5[x5].ProjectCost

    ECOOsumsub1 = 0
    for x6 in range(0, len(getECOO_sub1)):
        ECOOsumsub1 += getECOO_sub1[x6].ProjectCost

    ECOOsum = ECOOsum0 + ECOOsum1 + ECOOsum2 + ECOOsum3 + ECOOsum4 + ECOOsum5 + ECOOsumsub1

    # 这里是收入计量

    ECOIsum0 = 0
    for y in range(0, len(getECOI_0)):
        ECOIsum0 += getECOI_0[y].ProjectGot

    ECOIsum1 = 0
    for y1 in range(0, len(getECOI_1)):
        ECOIsum1 += getECOI_1[y1].ProjectGot

    ECOIsumsub1 = 0
    for y2 in range(0, len(getECOI_sub1)):
        ECOIsumsub1 += getECOI_sub1[y2].ProjectGot

    ECOIsum = ECOIsum0 + ECOIsum1 + ECOIsumsub1

    # 获取收入支出总值
    newdata['ECOOsum'] = ECOOsum
    newdata['ECOIsum'] = ECOIsum
    # 获取支出每类总值
    newdata['ECOOsum0'] = ECOOsum0
    newdata['ECOOsum1'] = ECOOsum1
    newdata['ECOOsum2'] = ECOOsum2
    newdata['ECOOsum3'] = ECOOsum3
    newdata['ECOOsum4'] = ECOOsum4
    newdata['ECOOsum5'] = ECOOsum5
    newdata['ECOOsumsub1'] = ECOOsumsub1
    # 获取收入每类总值
    newdata['ECOIsum0'] = ECOIsum0
    newdata['ECOIsum1'] = ECOIsum1
    newdata['ECOIsumsub1'] = ECOIsumsub1
    # 取值完成
    ################################
    # print('总支出：' + str(ECOOsum) + '总收入：' + str(
    #     ECOIsum) + '支出小类分别：' + str(ECOOsum0) + ',' + str(ECOOsum1) + ',' + str(ECOOsum2) + ',' + str(
    #     ECOOsum3) + ',' + str(ECOOsum4) + ',' + str(
    #     ECOOsum5) + ',' + str(ECOOsumsub1) + ',' + '收入小类分别：' + str(ECOIsum0) + ',' + str(ECOIsum1) + ',' + str(
    #     ECOIsumsub1))
    return HttpResponse(json.dumps(newdata))


# model_to_dict只能实行一个QuerySet的转换，

@csrf_exempt
def PDInfoUpdate(request):
    PDAllObj = ProductionList.objects.all()

    newdataList = []

    for k in range(0, len(PDAllObj)):
        dataUnit = []
        dataUnit.append(PDAllObj[k].ProductionNM)
        dataUnit.append(PDAllObj[k].ProductionUnitPrice)
        dataUnit.append(PDAllObj[k].ProductionSoldNum)
        dataUnit.append(PDAllObj[k].ProductionPrice)
        dataUnit.append(PDAllObj[k].ProductionSoldDate)
        # print(dataUnit)
        newdataList.append(dataUnit)

    # 添加safe=False,获取JsonRep
    # print(newdataList)
    # 获取日期索引的方法
    def takeDate(elem):
        return elem[4]

    # 获取总价
    def takeTotalPriceData(elem):
        return elem[3]

    # 消除非本月数据，清洗数据，并根据总售价排序数据
    def cleanOtherMouthData(DataList):
        thisYearDate = datetime.datetime.now().year
        getDataLength = len(DataList)
        getnewdataList = []
        for i in range(0, getDataLength):
            if str(thisYearDate) in DataList[i][4]:
                getnewdataList.append(DataList[i])

        # print('获取到的本年数据：' + str(getnewdataList))
        getnewdataList.sort(key=takeTotalPriceData, reverse=True)
        # print('获取到的根据价格排序的数据：' + str(getnewdataList))
        return getnewdataList

    newdataList = cleanOtherMouthData(newdataList)

    # 获取总价前十的数据的方法
    def getTop10Data(DataList):
        getnewdataList = []
        for i in range(0, 10):
            getnewdataList.append(DataList[i])

        return getnewdataList

    # 获取到总价前十数据，将其从小到大排序
    newdataList = getTop10Data(newdataList)
    newdataList.sort(key=takeTotalPriceData)

    # print('这是实际获取到的根据价格排序的数据：' + str(newdataList))

    return HttpResponse(json.dumps(newdataList))


@csrf_exempt
def PDFormUpdate(request):
    newdata = {
        'PDName': request.POST.get('PDName'),
        'UnitPrice': request.POST.get('UnitPrice'),
        'SoldNum': request.POST.get('SoldNum'),
        'TotalPrice': request.POST.get('TotalPrice'),
        'SoldDate': request.POST.get('SoldDate')
    }
    try:
        PDGetObj = ProductionList.objects.get(ProductionNM=newdata['PDName'], ProductionSoldDate=newdata['SoldDate'])
    except ProductionList.DoesNotExist:
        print('这是一个新的产品信息。')
        newdata['Message'] = '这是一个新的产品信息,已创建新项目！'
        PDCreateObj = ProductionList(ProductionNM=newdata['PDName'], ProductionUnitPrice=newdata['UnitPrice'],
                                     ProductionSoldNum=newdata['SoldNum'],
                                     ProductionPrice=newdata['TotalPrice'],
                                     ProductionSoldDate=newdata['SoldDate'])
        PDCreateObj.save()

    else:
        print('这是一个已经存在的产品信息。')
        newdata['Message'] = '这是一个已经存在的产品信息,已更新项目！'
        PDGetObj.ProductionNM = newdata['PDName']
        PDGetObj.ProductionUnitPrice = newdata['UnitPrice']
        PDGetObj.ProductionSoldNum = newdata['SoldNum']
        PDGetObj.ProductionPrice = newdata['TotalPrice']
        PDGetObj.ProductionSoldDate = newdata['SoldDate']
        PDGetObj.save()

    return HttpResponse(json.dumps(newdata))


# 此方法用于管理员发送通知所使用的AJAX，关联‘@func1’
@csrf_exempt
def InfoUpdate(request):
    newdata = {}
    newdata['TextContent'] = request.POST.get('TextContent')
    newdata['writername'] = request.POST.get('writername')
    newdata['writedate'] = request.POST.get('writedate')
    # print(newdata)
    try:
        getInfoData = InfoList.objects.get(TextContent=newdata['TextContent'], writername=newdata['writername'],
                                           writedate=newdata['writedate'])
    except InfoList.DoesNotExist:
        # 获取本人是否发送过同样的消息
        getInfoData = InfoList.objects.filter(TextContent=newdata['TextContent'], writername=newdata['writername'])
        if len(getInfoData) == 0:
            getInfoData = InfoList.objects.filter(TextContent=newdata['TextContent'])
            if len(getInfoData) == 0:
                # print("我们没有查询到同样信息。")
                newdata['Message'] = "我们没有查询到通知过这条信息,所以我们同步发送了这条消息。"
                createInfoData = InfoList(TextContent=newdata['TextContent'], writername=newdata['writername'],
                                          writedate=newdata['writedate'])
                createInfoData.save()
            else:
                # print("我们查询到在有人发送过同样信息")
                newdata['NewDataConfirmTag'] = 1
                # print(str(getInfoData[0]))
                if len(getInfoData) > 1:
                    newdata['Message'] = "我们查询到有人(例如:" + getInfoData[len(getInfoData) - 1].writername + \
                                         ")发送过同样信息,但是不一定是最近发的，所以建议您确认并更新本次操作，我们会将您的数据更新同步发送出去。您确认本次操作吗？"
                elif len(getInfoData) == 1:
                    newdata['Message'] = "我们查询到有人(例如:" + str(getInfoData[0].writername) + \
                                         ")发送过同样信息,但是不一定是最近发的，所以建议您确认并更新本次操作，我们会将您的数据更新同步发送出去。您确认本次操作吗？"

                # 此处传回，并在接受到用户操作后跳转至新方法

        elif len(getInfoData) > 1:
            getSameDate = getInfoData[len(getInfoData) - 1].writedate
            newgetInfoData = getInfoData[len(getInfoData) - 1]
            newgetInfoData.writedate = newdata['writedate']
            newgetInfoData.save()
            # print("我们查询到您在[" + getSameDate + "]发送过同样信息,所以我们更新了您的发布时间并同步发送了这条消息。")
            newdata['Message'] = "我们查询到您在[" + getSameDate + "]发送过同样信息,所以我们更新了您的发布时间并同步发送了这条消息。"
        elif len(getInfoData) == 1:
            # print(getInfoData[0].writedate)
            getSameDate = getInfoData[0].writedate
            getInfoData[0].writedate = newdata['writedate']
            getInfoData[0].save()
            # print("我们查询到您在[" + getSameDate + "]发送过同样信息,所以我们更新了您的发布时间并同步发送了这条消息。")
            newdata['Message'] = "我们查询到您在[" + getSameDate + "]发送过同样信息,所以我们更新了您的发布时间并同步发送了这条消息。"

    else:
        # print("我们查询到在同一时间您发送的信息，数据库不更新！")
        newdata['Message'] = "我们查询到您在同一时间发送过此信息。"

    return HttpResponse(json.dumps(newdata))


# 此方法用作当用户确认后才执行的二次Ajax操作,属于‘@func1’
@csrf_exempt
def SureInfoDataUpdate(request):
    newdata = {}
    newdata['TextContent'] = request.POST.get('TextContent')
    newdata['writername'] = request.POST.get('writername')
    newdata['writedate'] = request.POST.get('writedate')
    createInfoData = InfoList(TextContent=newdata['TextContent'], writername=newdata['writername'],
                              writedate=newdata['writedate'])
    createInfoData.save()
    newdata['Message'] = '已同步更新！'
    return HttpResponse(json.dumps(newdata))


@csrf_exempt
def showmenewInfo(request):
    newdata = []
    getOBj = InfoList.objects.all()

    def getFormatTodayDate():
        year = str(datetime.datetime.now().year)
        mouth = '0' + str(datetime.datetime.now().month) if datetime.datetime.now().month < 10 else \
            str(datetime.datetime.now().month)
        day = '0' + str(datetime.datetime.now().day) if datetime.datetime.now().day < 10 else \
            str(datetime.datetime.now().day)
        return year + '-' + mouth + '-' + day

    def getFormatYesterdayDate():
        year = str(datetime.datetime.now().year)
        mouth = '0' + str(datetime.datetime.now().month) if datetime.datetime.now().month < 10 else \
            str(datetime.datetime.now().month)
        day = '0' + str(datetime.datetime.now().day - 1) if datetime.datetime.now().day - 1 < 10 else \
            str(datetime.datetime.now().day - 1)
        return year + '-' + mouth + '-' + day

    yesterdayDate = getFormatYesterdayDate()
    todayDate = getFormatTodayDate()
    print(yesterdayDate + '   ' + todayDate)
    for i in range(0, len(getOBj)):
        data = []
        print(getOBj[i].writedate)
        if yesterdayDate in getOBj[i].writedate or todayDate in getOBj[i].writedate:
            data.append(getOBj[i].TextContent)
            data.append(getOBj[i].writername)
            data.append(getOBj[i].writedate)
            newdata.append(data)

    def gettime(elem):
        return elem[2]

    newdata.sort(key=gettime)
    # newdata['Message'] = '我们显示了最新的20条不同管理员的消息，其它消息'
    print(newdata)
    return HttpResponse(json.dumps(newdata))


# 获取人员权限
@csrf_exempt
def getAuthority(request):
    newdata = {}
    newdata['username'] = request.POST.get('username')
    try:
        getOBJ = administratorNameList.objects.get(adminname=newdata['username'])
    except administratorNameList.DoesNotExist:
        newdata['adminFlag'] = -1
        newdata['Message'] = '您是普通用户，不可以发送消息通知！'
    else:
        if getOBJ.adminPVLevel == 1:
            newdata['adminFlag'] = 1
            newdata['Message'] = '尊敬的超管，您可以使用任何功能！'
        elif getOBJ.adminPVLevel == 2:
            newdata['adminFlag'] = 2
            newdata['Message'] = '您是管理员，可以发送消息！'
        else:
            newdata['adminFlag'] = 0
            newdata['Message'] = '您的行为是非法的！'

    return HttpResponse(json.dumps(newdata))


# 获取收入项目，预测用
@csrf_exempt
def getFutureInfo(request):
    newdata = []
    getECOIall = COMECIList.objects.all()
    for i in range(0, len(getECOIall)):
        datanode = []
        # 生成随机数因子
        datanode.append(random.random())
        datanode.append(getECOIall[i].ProjectGot)
        newdata.append(datanode)

    return HttpResponse(json.dumps(newdata))
