
import xlwings as xw
import os
import json
import matchbook
from matchbook import APIClient
from matchbook.enums import Side
from matchbook.enums import Boolean
import time
import xlwings as xw
import json
import json
import logging
from logging.config import fileConfig
from pprint import pprint
import sys
from time import sleep
import datetime
from datetime import datetime, timedelta

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
    #    oapp = xw.apps.active
    #    okey = xw.apps.keys()
    #    wb = xw.apps[oapp].books.open(r'F:/Users/Oliver.Home64bit/Documents/BA/2020/270320 - D.xlsm')
    wb = xw.apps(oapp).books(spreadsheet)
    #    wb = xw.apps[xlapp].books[spreadsheet]
    sht = wb.sheets['Sheet1']
    rng = sht.range('a5', 'Q50').value
    race = sht.range('a1').value
    racestart = sht.range('ac2').value
    #    print(race)
    # print(rng[0][1])
    i = 0
    j = 0
    runner_list = []

    for i in range(len(rng)):
        #    print(rng[i][1])
        if (rng[i][16] == 'BACKSP' or rng[i][16] == 'BACK-SP' or rng[i][16] == 'BACK') and racestart > -1:
            #        print(rng[i][0],rng[i][16],rng[i][6])
            runner_list.append([rng[i][0], 'buy', rng[i][5]])
            j = j + 1
        elif (rng[i][16] == 'LAYSP' or rng[i][16] == 'LAY-SP' or rng[i][16] == 'LAY') and racestart > -1:
            runner_list.append([rng[i][0], 'sell', rng[i][7]]) # To lay at current back price, enter 5, or to take current ask price enter 7
            j = j + 1

    #        runner_list.append({'name': rng[i][0], 'BackOrLay': rng[i][16], 'price': rng[i][5]})
    #        runner_list.update({'horses': {'name': rng[i][0], 'BackOrLay': rng[i][16], 'price': rng[i][5]}})
    # runner_list.append['name': rng[i][0],'BackOrLay': rng[i][16],'price': rng[i][5]]
    # a = np.array(runner_list)
    # print(runner_list)
    # if 'BACK' in rng
    # if len(runner_list) > 0:

    return runner_list, race

def Put_Matchbook_Runners(oRunners):
    wb = xw.apps(oapp).books(spreadsheet)
    sht = wb.sheets['Matchbook']
    for i in range(len(oRunners)):
        sht.range('A5').value = oRunners


#######__start__########
spreadsheet = 'BA Template - Dogs.xlsm'
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

mb = APIClient()
#mb = APIClient(configuration['auth']['login'],configuration['auth']['login'])
mb.login()
print(str(mb.login))


#balance = mb.account.get_account()
#sports = mb.reference_data.get_sports()
#print(json.dumps(balance, indent=4))
#horses_id = 24735152712200
greyhounds_id = 241798357140019
horse_events = mb.market_data.get_events(sport_ids=greyhounds_id, include_event_participants=Boolean.F,
                                         before=(int(starttime + 3600*24)), after=(int(starttime - 3600)))
#pprint(horse_events)
start_balance = mb.account.get_account()
start_balance = start_balance['balance']
new_balance = 0
print("Start Balance = " + str(start_balance))
country_events = []
for i in horse_events:
 #   if i['meta-tags'][4]['name'] == 'UK Ireland' and i['status'] == 'open':
        country_events.append([i['id'], i['start'], i['name']])

pprint(country_events)
next_event_id = country_events[0][0]
print(str(country_events[0][1] + ' Next race is - ' + country_events[0][2]))

betsPlaced = ''
old_market_id = ''
#horses_id = [s['id'] for s in sports if s['name']=='Horse Racing'][0]
#print(str(horses_id))


while keep_going:
    timenow = time.time()
    try:
        mb.keep_alive()
    except:
        pass
# refresh connection to Smarkets every 20 minutes
    now = datetime.now()
    if now.strftime("%H") >= "10" and new_balance!=start_balance:
        new_balance = mb.account.get_account()
        new_balance = new_balance['balance']
        print("Balance " + str(now) + " = " + str(new_balance))
        start_balance = new_balance

#    print(str(timenow-starttime))
    if timenow-starttime>1200 and now.strftime("%H") >= "10" and now.strftime("%H") <= "22":
        try:
            mb.keep_alive()
            starttime = time.time()
            cur_balance = mb.account.get_account()
            cur_balance = cur_balance['balance']
            if start_balance !=cur_balance:
                PandL = round(cur_balance-start_balance,2)
                print(f'                    Current balance = {cur_balance}; P&L Today = {PandL}')

        except:
            pass

    try:
        runner_list, race = get_excel_runners()
    except:
        pass

#print(str(runner_list))

    if len(runner_list) > 0:
        oTime = int(time.time())
        horse_events = mb.market_data.get_events(sport_ids=greyhounds_id, include_event_participants=Boolean.F,
                                                 before=(int(starttime + (3600))), after=(int(starttime - 3600)))
        #print(json.dumps(horse_events, indent=4))
        if len(horse_events) > 0:
            country_events = []
            for i in horse_events:
    #             if i['meta-tags'][4]['name'] == 'UK Ireland' and i['status'] == 'open':
                  country_events.append([i['id'], i['start'], i['name']])
            #event_ids = ','.join(str(d['id']) for d in horse_events)
    #        print(str(country_events))
            #event_ids = [val['id'] for val in horse_events]

            try:
                 next_event_id = country_events[0][0]
        #        print(next_event_id)
            except:
                pass

            next_event_detail = mb.market_data.get_events(event_id=next_event_id, include_event_participants='false')

            #next_market_id = [s['markets']['id'] for s in next_event_detail if s['markets']['name']=='WIN'][0]
            #print(json.dumps(next_event_detail, indent=4))
            for i in next_event_detail['markets']:
                if i['name'] == 'WIN':
                    next_market_id = i['id']

            if next_market_id != old_market_id:
                print(str(next_market_id) + " - " + str(country_events[0][2]))
                old_market_id = next_market_id

                oContracts = mb.market_data.get_runners(next_event_id, next_market_id)
    #        runner_id = oContracts['runners'][0]['id']
            #order_submit = mb.betting.send_orders(runner_id,5,Side.Back, 2)
            #print(str(order_submit))
            #print(json.dumps(oContracts, indent=4))

            #print(str(runner_id))

            oRunners = []
            for k in oContracts['runners']:
                #print(k['name'].lstrip('0123456789.- ') + "  " + str(k['id']) + "   " + str(k['prices'][0]['decimal-odds']))
                if k['withdrawn'] != True:
                    oRunners.append([k['name'].lstrip('0123456789.- '),str(k['id'])])


 #       print(oRunners)

    for k in range(len(runner_list)):
        for y in oRunners:
    #        print(runner_list[k][0] + ' ' + y[0])
    #        print(substring_after((str(runner_list[k][0]).lower()).replace("'", ""), ".") + '  ' + str(
    #                str(y[0]).lower()).replace("'", ""))
            if substring_after((str(runner_list[k][0]).lower()).replace("'", ""), ".") == str(
                    str(y[0]).lower()).replace("'", ""):
                oexists = 1
#                print("This exists in both: " + y[0] + ' ' + y[1] + ", BackOrLay = " + str(
#                    runner_list[k][1]) + ", Price = " + str(runner_list[k][2]))
                runner_id = y[1]
                if runner_list[k][1] == 'buy':
                    BackOrLay = Side.Back
                    # to place £10 bet...
                    amount = 4
                    price = runner_list[k][2]
                #                quantity = int((amount * 100000000) / price)
                else:
                    BackOrLay = Side.Lay
                    amount = (5/(runner_list[k][2] -1))
                    price = runner_list[k][2]
                #                quantity = int((amount * 100000000) / price)
                # price = str(runner_list[k][2])
                #                        price = 10
                #                        stake = 20000000

                try:
                    if betsPlaced != next_market_id:
                        order_submit = mb.betting.send_orders(runner_id, price, BackOrLay, amount)
#                        print(str(order_submit))
                        print(str(order_submit[0]['market-name']) + ' - ' + str(
                            order_submit[0]['event-name']) + ' - ' + str(order_submit[0]['runner-name']) + ' - '
                              + str(order_submit[0]['side']) + ' - ' + str(order_submit[0]['odds']))
                        betsPlaced = 'True'
                    # client.place_order(
                    #     str(next_market_id),  # market id
                    #     str(contract_id),  # contract id
                    #     price,
                    #     quantity,
                    #     #                           50,  # percentage price * 10**4, here: 0.5% / 200 decimal / 19900 american
                    #     #                            500000,  # quantity: total stake * 10**4, here: 50 GBP. Your buy order locks 0.25 GBP, as
                    #     #      0.25 GBP * 200 = 50 GBP
                    #     BackOrLay,  # order side: buy or sell
                    # )
                except:
                    pass

    if betsPlaced == 'True':
        betsPlaced = next_market_id

        time.sleep(2)

    else:
        time.sleep(2)


#    Put_Matchbook_Runners(oRunners)

    #print(next_event_detail['markets'][0]['name'])
    #print(str(map(str,(event_ids['0']))))

