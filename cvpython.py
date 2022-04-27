#import some shit
import io
import sys
from tkinter import N
import requests
import json

#for redirecting result to output
old_stdout = sys.stdout
new_stdout = io.StringIO()
sys.stdout = new_stdout

#define api url
response_API = requests.get('https://covid19.ddc.moph.go.th/api/Cases/today-cases-by-provinces')

#get data from response_api and convert to json
data = json.loads(response_API.text)

#get surat thani data from json mess
def getdata():
    global txndate
    global newcase
    global totalcase
    global newdeath
    global totaldeath
    global updatetime
    txndate = data[59]['txn_date']
    newcase = data[59]['new_case']
    totalcase = data[59]['total_case']
    newdeath = data[59]['new_death']
    totaldeath = data[59]['total_death']
    updatetime = data[59]['update_date']

#display data from getdata
def printdata():
    print('วันที่แถลง',txndate,'คน')
    print('จำนวนผู้ติดเชื้อรายใหม่',newcase,'คน')
    print('จำนวนผู้ติดเชื้อสะสม',totalcase,'คน')
    print('จำนวนผู้ป่วยเสียชีวิตรายใหม่',newdeath,'คน')
    print('จำนวนผู้ป่วยเสียชีวิตสะสม',totaldeath,'คน')
    print('อัพเดทเมื่อ',updatetime)


#define function called run
def run():
    if response_API.status_code == 200:
        print('---------------------------')
        print('Server Status - 200 OK')
        print('---------------------------')
        getdata()
        printdata()
    elif response_API.status_code == 404:
        print('Server Status - 404 Not Found')
    elif response_API.status_code == 500:
        print('Server Status - 500 Internal Server Error')
    elif response_API.status_code == 502:
        print('Server Status - 502 Bad Gateway')
    elif response_API.status_code == 403:
        print('Server Status - 403 Forbidden')
    elif response_API.status_code == 418:
        print('Server Status - 418 I\'m a teapot')
    else:
        print('Server is not running')


run()
output = new_stdout.getvalue()
sys.stdout = old_stdout
print(output)

