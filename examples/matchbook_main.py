from matchbook import APIClient
from matchbook.enums import Side
from matchbook.enums import Boolean
import time
import xlwings as xw
from pprint import pprint
import sys
from datetime import datetime, timedelta
from twilio.rest import Client

client = Client("AC838779119d6a0fb49d121f539854fb98","ba59e17b80f0caebe226ba7928b13b34")

def substring_after(s, delim):
    ostr = s.partition(delim)[2]
    #    print("in funct = " + ostr)
    if not ostr:
        ostr = s
    return ostr.lstrip()


def check_exists(self):
    xlapp = ''
    for j in xw.apps.keys():
        for i in xw.apps[j].books:
            if i.name == spreadsheet:
                xlapp = j
    return xlapp

def get_excel_runners():
    wb = xw.apps(oapp).books(spreadsheet)
    #    wb = xw.apps[xlapp].books[spreadsheet]
    sht = wb.sheets['Sheet1']
    rng = sht.range('a5', 'Q50').value
    race = sht.range('a1').value
    racestart = sht.range('ac2').value
    i = 0
    j = 0
    runner_list = []

    for i in range(len(rng)):
        #    print(rng[i][1])
        if (rng[i][16] == 'BACKSP' or rng[i][16] == 'BACK-SP' or rng[i][16] == 'BACK') and racestart > -1:
            #        print(rng[i][0],rng[i][16],rng[i][6])
            runner_list.append([rng[i][0], 'buy', rng[i][7]])
            j = j + 1
        elif (rng[i][16] == 'LAYSP' or rng[i][16] == 'LAY-SP' or rng[i][16] == 'LAY') and racestart > -1:
            runner_list.append([rng[i][0], 'sell', rng[i][5]])
            j = j + 1

    return runner_list, race

def Put_Matchbook_Runners(oRunners):
    wb = xw.apps(oapp).books(spreadsheet)
    sht = wb.sheets['Matchbook']
    sht.range('A1').value = next_race
    for i in range(len(oRunners)):
        sht.range('A5').value = oRunners


#spreadsheet = 'Matchbook test.xlsm'
spreadsheet = 'BA Template - Horses Win and place 23.10.20.xlsm'
oapp = check_exists(spreadsheet)
if oapp == '':
    pprint('Spreadsheet not open - Aborting')
    sys.exit()
else:
    pprint('Spreadsheet exists. Appkey = ' + str(oapp))

starttime=time.time()
refreshtime = time.time()
keep_going = True
runner_list = []
horse_events = []
mb = APIClient()
#mb = APIClient(configuration['auth']['login'],configuration['auth']['login'])
mb.login()
print(str(mb.login))
start_balance = mb.account.get_account()
print("Start Balance = " + str(start_balance['balance']))
horses_id = 24735152712200
country_events = []
upcoming_events = []
betsPlaced = ''
next_market_id =''
next_event_id = ''
next_race_start = datetime.utcnow() - timedelta(seconds=10)
old_market_id = ''
old_race = ''
next_race = ''
oldBFrace = ''
race = ''
pattern = '%d.%m.%Y %H:%M:%S'

while keep_going:
    timenow = time.time()
    now = datetime.now()
# refresh connection to matchbook every hour minutes
    if timenow-starttime>3600:
         try:
             mb.keep_alive()
             starttime = time.time()
         except:
             pass

    if horse_events==[] and now.strftime("%H") >= "10" and now.strftime("%H") <= "20":
        horse_events = mb.market_data.get_events(sport_ids=horses_id, include_event_participants=Boolean.F,
                                                 before=(int(starttime + 3600 * 12)), after=int(time.time() - 10))
#        horse_events = [i for i in horse_events if i['meta-tags'][4]['name'] == 'UK Ireland' and i['status'] == 'open'\
#                        and i['markets'][0]['name'] == 'WIN']
        horse_events = [i for i in horse_events if i['status'] == 'open'\
                        and i['markets'][0]['name'] == 'WIN']
        print("horse_events refreshed..." + str(datetime.now().time()))
        start_balance = mb.account.get_account()
        print("Start Balance = " + str(start_balance['balance']))
#        pprint(horse_events)
#    print(next_race_start)
#    print(datetime.datetime.now().isoformat())
    try:
        old_race = next_race
        dtnow = datetime.utcnow().isoformat()
        horse_events = [i for i in horse_events if i['start'] > datetime.utcnow().isoformat()]
        if next_race_start < datetime.utcnow() or len(horse_events)==1:
            for i in horse_events:
 #              if i['meta-tags'][4]['name'] == 'UK Ireland' and i['status'] == 'open' \
 #                      and i['markets'][0]['name']=='WIN' and i['start'] > datetime.utcnow().isoformat():
 #               if i['start'] > datetime.utcnow().isoformat():
                next_race = [i['id'], i['start'], i['name']]
 #           next_race = [horse_events[0]['id'], horse_events[0]['start'], horse_events[0]['name']]
                upcoming_events = []
                if old_race != next_race:
                    for horses in horse_events:
                        upcoming_events.append([horses['id'], horses['start'], horses['name']])

                    balance = mb.account.get_account()
                    cur_balance = "Balance = " + str(round(balance['balance'],2)) + "  - Daily P&L = " + str(balance['balance']-start_balance['balance'])
                    print("Balance = " + str(balance['balance']) + "  - Daily P&L = " + str(balance['balance']-start_balance['balance']))

                    next_event_id = i['id']
                    next_market_id = i['markets'][0]['id']
                    old_race = next_race
    #                    Put_Matchbook_Runners([])
                    next_race_start = datetime.fromisoformat(i['start'].rstrip('Z'))
                    print("Next Matchbook race is - " + str(next_race) + " starts at " + str(next_race_start))
                    print("next_event_id= " + str(next_event_id) + ", next_market_id= " + str(next_market_id))
    #                    horse_events.remove(i)
    #                       client.messages.create(to="+447946620083", from_="+18082016144", body=cur_balance)
                break
#                    upcoming_events.remove(i)

#            if len(upcoming_events) > 0:
#            print(pprint(upcoming_events), str(dtnow))
#            pprint(dtnow)
#            upcoming_events = []
    except:
        pass

    if len(upcoming_events)>0:
        try:
            oldBFrace = race
            runner_list, race = get_excel_runners()
            if oldBFrace!=race:
                print("Next Betfair race is - " + str(race))
                oldBFrace = race

        except:
            pass
#print(str(runner_list))

    if len(runner_list) > 0:
#        try:
            oTime = int(time.time())
            if next_market_id != old_market_id:
    #            print(str(next_market_id) + " - " + str(country_events[0][2]))
                old_market_id = next_market_id
            oContracts = []
            print("mb.market_data.get_runners(" + str(next_event_id) + ", " + str(next_market_id) + ")" )
            oContracts = mb.market_data.get_runners(next_event_id, next_market_id)
    #        pprint(oContracts)
            oRunners = []
            for k in oContracts['runners']:
                #print(k['name'].lstrip('0123456789.- ') + "  " + str(k['id']) + "   " + str(k['prices'][0]['decimal-odds']))
                if k['withdrawn'] != True:
                    mylist = [k['name'].lstrip('0123456789.- '), str(k['id'])]
                    # for j in k['prices']:
                    #     mylist.append(j['odds'])
                    oRunners.append(mylist)
#        except:
#            pass

        #       print(oRunners)
#        Put_Matchbook_Runners(oRunners)

    for k in range(len(runner_list)):
        for y in oRunners:
            if substring_after((str(runner_list[k][0]).lower()).replace("'", ""), ".") == str(
                    str(y[0]).lower()).replace("'", ""):
                oexists = 1
#                print("This exists in both: " + y[0] + ' ' + y[1] + ", BackOrLay = " + str(
#                    runner_list[k][1]) + ", Price = " + str(runner_list[k][2]))
                runner_id = y[1]
                if runner_list[k][1] == 'buy':
                    BackOrLay = Side.Back
                    # to place £10 bet...
                    amount = 5
                    price = runner_list[k][2]
                else:
                    BackOrLay = Side.Lay
                    amount = (5/(runner_list[k][2] -1))
                    price = runner_list[k][2]

                try:
                    if betsPlaced != next_market_id:
                        order_submit = mb.betting.send_orders(runner_id, price, BackOrLay, amount)
#                        print(str(order_submit))
                        print(str(order_submit[0]['market-name']) + ' - ' + str(
                            order_submit[0]['event-name']) + ' - ' + str(order_submit[0]['runner-name']) + ' - '
                              + str(order_submit[0]['side']) + ' - ' + str(order_submit[0]['odds']))
                        betsPlaced = 'True'

                except:
                    pass

    if betsPlaced == 'True':
        betsPlaced = next_market_id

        time.sleep(1)

    else:
        if len(upcoming_events) > 0:
            time.sleep(1)
        else:
            time.sleep(3600)


#    Put_Matchbook_Runners(oRunners)

    #print(next_event_detail['markets'][0]['name'])
    #print(str(map(str,(event_ids['0']))))

