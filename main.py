import xml.etree.ElementTree as ET
import urllib.request
import Func
import datetime,time
import gmail
from Func import indent
from urllib.parse import quote


key="key=9a3bdfabc4837b2691c9b0f17c7d2575"
t=datetime.date.today()

# Today=str(t).replace("-","")
yesterday = datetime.date.today() + datetime.timedelta(days=-1)
Yesterday=str(yesterday).replace("-","")


# year="2016"
# mon="06"
# date="13"


# Func.AddAlarm()
Func.SendAlarm()
print("어제날짜: "+Yesterday)    #오늘껀 통계가 안나와서 출력이 안됨
# Dt="&targetDt="+year+mon+date




while(1):
    Dt = "&targetDt=" + Yesterday
    day=""
    print("""
    (입력가능 명령어)
    극장사이트
    일일
    주간
    영화목록
    영화사목록
    알람설정
    알람보내기
    """)
    Operation=input("오퍼레이션 선택:")

    if Operation=="극장사이트":
        Func.ConnectCinema()
        continue


    if(Operation == "일일"): #일일은 전날까지만
        day=input("조회날짜 입력(yyyymmdd)")
        if(len(day)==8 ):
            Dt="&targetDt=" + day
        Oper = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?"     #일일
        url = urllib.request.urlopen(Oper + key + Dt )

    elif (Operation == "알람설정"):
        Func.AddAlarm()
        continue
    elif (Operation == "알람보내기"):
        Func.SendAlarm()
        continue


    elif(Operation == "주간"): #주간은 입력한 날짜에 해당하는 주의 주말(금~일요일까지 집계한 내용을 보여줌)
        day = input("조회날짜 입력(yyyymmdd)")
        if (len(day) == 8):
            Dt = "&targetDt=" + day
        Oper = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.xml?"    #주간
        url = urllib.request.urlopen(Oper + key + Dt +"&weekGb=0")
    elif(Operation == "영화목록"):
        criteria=""
        criteria=str(input("검색 조건 입력(영화명,감독명,제작연도,개봉연도,코드명):"))
        Word=str(input("검색어 입력 "))
        Oper = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.xml?"  # 목록
        if (len(Word)):
            if criteria=="영화명":
                url = urllib.request.urlopen(Oper + key + "&movieNm=" + quote("%s" % Word))
            elif criteria == "감독명":
                url = urllib.request.urlopen(Oper + key + "&directorNm=" + quote("%s" % Word))
            elif criteria == "제작연도":
                url = urllib.request.urlopen(Oper + key + "&openStartDt=" + quote("%s" % Word))
            elif criteria == "개봉연도":
                url = urllib.request.urlopen(Oper + key + "&prdtStartYear=" + quote("%s" % Word))
            elif criteria == "코드명":
                url = urllib.request.urlopen(Oper + key + "&movieTypeCd=" + quote("%s" % Word))
            else:
                continue
        else:
            #미설정시
            url = urllib.request.urlopen(Oper + key + "&itemPerPage=1000")
    elif(Operation == "영화사목록"):
        Oper = "http://kobis.or.kr/kobisopenapi/webservice/rest/company/searchCompanyList.xml?"  # 목록
        url = urllib.request.urlopen(Oper + key)



    tree = ET.parse(url)
    note=tree.getroot()


#정리해서 보여줌
    indent(note)

#xml 문서 그대로 보여줌
#ET.dump(note)

    if Operation=="일일":
        Func.daily(note)
    elif Operation=="주간":
        Func.weekly(note)
    elif Operation=="영화목록":
        Func.MovieList(note)
    elif Operation=="영화사목록":
        Func.CompanyList(note)

    answer=input("메일을 보내시겠습니까? Y/N ")
    if answer=="Y"or answer== "y":
        m=gmail.Mail()
        m.login()
        m.write()
        m.add(Func.tag_list,Func.value_list)
        m.send()

    answer = input("xml 파일 저장을 원하시겠습니까? Y/N " )
    if answer == "Y" or answer == "y":
        fileNm=input("저장할 파일명")
        ET.ElementTree(note).write("%s.xml"%fileNm)

