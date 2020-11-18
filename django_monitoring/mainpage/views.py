from django.shortcuts import render
from django.http import HttpResponse
from . import keyword 
<<<<<<< refs/remotes/origin/master
from .models import StatisticValues, Subscriber
from datetime import datetime
from . import LocationInfo


def index(request):
    #통계 받아오는 API로 가져옴
    result = keyword.keywordFindAPI() 
    print(result)
     #context는 html에 data로 넘겨주는 parameter들을 담는것. 각각의 값을 전달한다
     #예를 들어 context에 result, result2, result3 이렇게 넣어서 전달하면
     #index.html에서 result, result2, result3 변수를 html 태그나 javascript코드 등에서 사용 가능하다.
    '''
    statisticDB = StatisticValues.objects.all() # 테이블 데이타를 전부 가져오기 위한 메소드
    statisticDBValues = list(StatisticValues.objects.all().values())
    context ={
        'result' : result,
        'statisticDBValues' : statisticDBValues,
    }
    print(statisticDBValues)
    '''
    # API 데이터를 DB 테이블 StatisticValues에 저장.
    try :
        #statisticValue = StatisticValues(updateTime = request.POST['updateTime'], TotalCase = request.POST['TotalCase'], 
        #                     TotalDeath = request.POST['TotalDeath'], TotalRecovered = request.POST['TotalRecovered'],
        #                     NowCase = request.POST['NowCase'], TotalChecking = request.POST['TotalChecking'],
        #                     notcaseCount = request.POST['notcaseCount'])
        
        YEAR= datetime.today().year        # 현재 연도 가져오기
        #print(YEAR)
        MONTH= datetime.today().month      # 현재 월 가져오기
        #print(MONTH)
        DAY= datetime.today().day        # 현재 일 가져오기
        #print(DAY)
        TodayDate=str(YEAR)+"."+str(MONTH)+"."+str(DAY)
        print(TodayDate)
        # if statisticDB.objects.get(updateTime=TodayDate).updateTime != TodayDate:
        #if not statisticDB.objects.filter(updateTime=TodayDate).exists(): 
        statisticValue = StatisticValues(updateTime = str(YEAR)+"."+result['updateTime'][23:28], 
                             TotalCase = result['TotalCase'], 
                             TotalDeath = result['TotalDeath'], TotalRecovered = result['TotalRecovered'],
                             NowCase = result['NowCase'], TotalChecking = result['TotalChecking'],
                             TodayCase = result['data0_1'], TodayRecovered =result['TodayRecovered'])
        statisticValue.save()
        
    except :
        statisticValue  = None
    # updateTime # 정보 업데이트 시간 data['updateTime'][23:28] -> 월.일(00.00 구조)

    statisticDB = StatisticValues.objects.all() # 테이블 데이타를 전부 가져오기 위한 메소드
    statisticDBValues = list(StatisticValues.objects.all().values())
    locationset = LocationInfo.get_location(result)
    seoul_gu_results = LocationInfo.scraping_data()
    context ={
        'result' : result,
        'statisticDBValues' : statisticDBValues,
        'locationset' : locationset,
        'seoul_gu_result' : seoul_gu_results,
    }
    print(statisticDBValues)
    print(statisticValue)
=======

def index(request):
    #통계 받아오는 API로 가져옴
    result = keyword.keywordFindAPI() #여기!
   
    """
    print(result)
    =={'resultCode':, 'TotalCase':, 'TotalRecovered':, 'TotalDeath': , 'NowCase': , 
    'city1n': , 'city2n':, 'city3n':, 'city4n':, 'city5n':, 
    'city1p':, 'city2p':, 'city3p': , 'city4p': , 'city5p': , 
    'recoveredPercentage': , 'deathPercentage':, 'checkingCounter': , 'checkingPercentage': , 
    'caseCount': , 'casePercentage':, 'notcaseCount': , 'notcasePercentage':, 'TotalChecking': ,
     'TodayRecovered':, 'TodayDeath':, 'TotalCaseBefore': , 'updateTime': , 'resultMessage':}
    """
     #context는 html에 data로 넘겨주는 parameter들을 담는것. 각각의 값을 전달한다
     #예를 들어 context에 result, result2, result3 이렇게 넣어서 전달하면
     #index.html에서 result, result2, result3 변수를 html 태그나 javascript코드 등에서 사용 가능하다.
    context ={
        'result' : result
    }
>>>>>>> Add Showing TotalCase at stastistics
    return render(request, 'index.html', context)

def mapview(request):
    return render(request, 'map.html')

#구독을 위한 관심지역 설정을 위한 DB view 설정
#전체설정 안하면 뷰오류나서 나중에 DB구현한다음에
'''def index(request) :
    Subscriber = Subscriber.objects.all() # 테이블 데이타를 전부 가져오기 위한 메소드
    context = {'SubscribeData' : SubscribeData}
    try :
        Subscribedatas = SubscribeData(address = request.POST['address'], sub_type = request.POST['sub_type'],
                             large_region = request.POST['large_region'], medium_region = request.POST['medium_region'],
                             small_region = request.POST['small_region'])
        Subscirbedatas.save()
    except :
        Subscribedatas  = None
    return render(request, 'contents-subscribe.html', context) # render는 view에서 템플릿에 전달할 데이타를 Dictionary로 전달한다

<<<<<<< refs/remotes/origin/master
'''
# Create your views here.

<<<<<<< refs/remotes/origin/master
=======
def statisticsView(self,request):
    template_name = 'contents-statistics.html'
    result = keyword.keywordFindAPI() #여기!
    context ={
        'result' : list(result)
    }
    return render(request, template_name, context)
>>>>>>> add list format
=======

# `
# def statisticsView(self,request):
#     template_name = 'contents-statistics.html'
    
#     return render(request, template_name, context)`
>>>>>>> Add Showing TotalCase at stastistics
