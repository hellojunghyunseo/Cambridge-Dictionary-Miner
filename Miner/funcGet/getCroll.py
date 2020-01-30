from bs4 import BeautifulSoup
import requests
import json

def getCroll(origin):
    url = "http://dictionary.cambridge.org/ko/%EC%82%AC%EC%A0%84/%EC%98%81%EC%96%B4-%ED%95%9C%EA%B5%AD%EC%96%B4/"
    page = requests.get(url + origin)
    if page.status_code != 200:
        return setNoneData(origin)

    if len(origin) <= 1: # ` 과 같은 가비지 문자일때
        return setNoneData(origin)

    try:
        areas = getAreas(page)

        wordInfo = list()

        for area in areas:
            word = getWord(area)

            pos = getPos(area)

            mean = getMean(area)

            pron = getProns(area)

            wordInfo.append({
                'origin': origin,
                'word': word,
                'pos': pos,
                'mean': mean,
                'UKpron': pron['UK'],
                'USpron': pron['US']
            })
    except:
        return setNoneData(origin)

    if not wordInfo: #빈 리스트 일시
        return setNoneData(origin)
    #print(wordInfo)
    return wordInfo

def setNoneData(origin):
    wordInfo = {
        'origin': origin,
        'word': '?',
        'pos': '?',
        'mean': '?',
        'UKpron': '?',
        'USpron': '?'
    }
    #print(wordInfo)
    return wordInfo

def getAreas(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    areas = soup.find_all("div", class_="entry-body__el")
    return areas

def getWord(area):
    return area.find("span", class_="dhw").text.strip()

def getPos(area):
    return area.find("span", class_="pos").text.strip()

def getMean(area):
    list = area.find_all("span", class_="trans")
    return makeBundle(list)

def getProns(area):
    list = area.find_all("span", class_="pron-info")
    pron = dict()
    for i in list:
        region = makeBundle(i.find_all("span", class_="region"))
        if region == '':
            continue

        dipa = makeBundle(i.find_all("span", class_="dipa"))
        pron[region.upper()] = dipa

    return pron

def makeBundle(list):
    bundle = ''
    for i in list:
        letter = i.text.strip()
        if bundle == '':
            bundle = letter
        else:
            bundle += "," + letter

    return bundle
