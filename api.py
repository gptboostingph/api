

from top1phsmm.api import top1phsmm
from top1phsmm.api import Autmate
from mahdix import *
darkblue = "\033[34m"
red = "\033[1;31m"
hotpink = "\033[38;5;197m"
from threading import Thread
from concurrent.futures import ThreadPoolExecutor as thd
import requests
connect=top1phsmm(api_key='pnyh7jers8ujf4u6wo8k5914lyh7mfjx845dxkazh6ydgqn2t63uktxe2d4w0m4c')
connect_automate=Autmate()
def submite(token,post_url,order_id):
    url='https://graph.facebook.com/v13.0/me/feed'
    datas={
        'link':post_url,
        'published':'0',
        'privacy':'{"value":"SELF"}',
        'access_token':token}
    try:
        res=requests.post(url,data=datas,headers={
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate',
            'connection': 'keep-alive',
            'content-length': '0',
            'host': 'graph.facebook.com'
        }).json()
        if res['id']:
            opder_delev_list.append(order_id)
            count_of_2 = opder_delev_list.count(order_id)
            # sys.stdout.write(f'\033[1;37m[\033[38;5;81m{count_of_2}\033[1;37m]\033[1;32m Done Successfully Shared\033[1;31m ───────> \033[1;34m{order_id} \033[1;31m')
            # sys.stdout.flush()  # Ensure the output is immediately written
            # sys.stdout.write('\r') 
            # Move the cursor to the beginning of the line
            # print(f'\033[38;5;189m────────────────────────────────────────────────────────────')
            print(f'\033[1;31m[\033[1;31m{order_id}\033[1;31m]\033[1;34m Currently Sharing\033[1;35m [{count_of_2}] \033[1;31m\n', end='\r')
    except Exception as e:
        try:
            for thdes in thdess:
                thdes.join()
                thdess.remove(thdes)
        except:pass
        # print(f'Error: {rc(mycolor)} {res['error']['message']}' ,end= '\r')
        pass






my_cookes = list(open( 'input_file.txt', 'r',encoding='utf-8').read().splitlines()) # use by saved cookes|token
print(f'zack chevron: total account {darkblue}{len(my_cookes)}')
service_id=[]
opder_delev_list=[]
wrong_url=[]
thdess=[]


def mains():
    get_orders=connect.get_orders()
    for lins in get_orders:
        service_id =lins['service_id']
        quantity =lins['quantity']
        order_link=lins['link']
        order_id =lins['id']
        status= lins['status']
        if service_id in [1204] and quantity > 0  and 'facebook.com' in order_link and 'pending' in status  :
            if order_id not in opder_delev_list:
                opder_delev_list.append(order_id)
                connect.update_order_status(order_id, status='In Progress')  # Update the status to "In Progress"
                if '/share/' in order_link:
                    retx=requests.get(order_link,headers=connect_automate.headers_web,allow_redirects=True)
                    order_link=retx.url
                print(f'{RED}Order ID: {LI_CYAN}{order_id}')
                print(f'{hotpink}Quantity: {darkblue}{quantity}')
                print(f'{WHITE}Link: {LI_BLACK}{order_link}')
                print(f'{red}SPAM SHARING ON THE GO')
                while  opder_delev_list.count(order_id)<= quantity :
                    # with thd(max_workers=600) as main executor:
                        for cokis in my_cookes:
                            token = cokis.split('|')[1]
                            count_of_2 = opder_delev_list.count(order_id)
                            if count_of_2+700 >= quantity:
                                print(f"{BG_RED}The Oder Is Complited : {darkblue} {order_id}")
                                connect.set_orders_completed(order_id)
                                break
                            elif  count_of_2 < quantity:
                                try:
                                    thdes=Thread(target= submite,args=(token,order_link,order_id,))
                                    thdess.append(thdes)
                                    thdes.start()                                    
                                except:pass
                                # with thd(max_workers=600) as main executor:
                                # sub.submit(submite,token,order_link,order_id)


        if service_id in [1229] and quantity > 0 and '/video_id/' in order_link and 'facebook.com' in order_link and 'pending' in status  :
         if order_id not in opder_delev_list:
                opder_delev_list.append(order_id)
                if '/videos/' in order_link:
                    retx=requests.get(order_link,headers=connect_automate.headers_web,allow_redirects=True)
                    order_link=retx.url
                print(mahdilinx())
                print(f'{BG_RED}Order ID: {BLUE}{order_id}')
                print(f'{LI_WHITE}Quantity: {LI_GREEN}{quantity}')
                print(f'{LI_WHITE}Link: {LI_GREEN}{order_link}')
                print(linex())
                while  opder_delev_list.count(order_id)<= quantity :
                    # with thd(max_workers=600) as main executor:
                        for cokis in my_cookes:
                            token = cokis.split('|')[1]
                            count_of_2 = opder_delev_list.count(order_id)
                            if count_of_2+700 >= quantity:
                                connect.update_oder_status(order_id)
                                print(f"{LI_GREEN}The Oder Is Complited : {LI_WHITE} {order_id}")
                                print(mahdilinx())
                                break
                            elif  count_of_2 < quantity:
                                try:
                                    thdes=Thread(target= submite,args=(token,order_link,order_id,))
                                    thdess.append(thdes)
                                    thdes.start()
                                except:pass
                                # with thd(max_workers=600) as main executor:
                            #       sub.submit(submite,token,order_link,order_id)
                            

        if service_id in [1199] and quantity > 0  and 'facebook.com' in order_link and 'pending' in status  :
            if order_id not in opder_delev_list:
                opder_delev_list.append(order_id)
                if '/share/' in order_link:
                    retx=requests.get(order_link,headers=connect_automate.headers_web,allow_redirects=True)
                    order_link=retx.url
                print(mahdilinx())
                print(f'{LI_WHITE}Order ID: {LI_GREEN}{order_id}')
                print(f'{LI_WHITE}Quantity: {LI_GREEN}{quantity}')
                print(f'{LI_WHITE}Link: {LI_GREEN}{order_link}')
                print(linex())
                while  opder_delev_list.count(order_id)<= quantity :
                    # with thd(max_workers=400) as main executor:
                        for cokis in my_cookes:
                            token = cokis.split('|')[1]
                            count_of_2 = opder_delev_list.count(order_id)
                            if count_of_2+700 >= quantity:
                                connect.update_oder_status(order_id)
                                print(f"{LI_GREEN}The Oder Is Complited : {LI_WHITE} {order_id}")
                                print(mahdilinx())
                                break
                            elif  count_of_2 < quantity:
                                try:
                                    
                                     
                                    thdes=Thread(target= submite,args=(token,order_link,order_id,))
                                    thdess.append(thdes)
                                    thdes.start()
                                except:pass
                                # with thd(max_workers=400) as main executor:
                            #       sub.submit(submite,token,order_link,order_id)

        if service_id in [1229] and quantity > 0 and '/video_id/' in order_link and 'facebook.com' in order_link and 'pending' in status  :
         if order_id not in opder_delev_list:
                opder_delev_list.append(order_id)
                if '/videos/' in order_link:
                    retx=requests.get(order_link,headers=connect_automate.headers_web,allow_redirects=True)
                    order_link=retx.url
                print(mahdilinx())
                print(f'{LI_WHITE}Order ID: {LI_GREEN}{order_id}')
                print(f'{LI_WHITE}Quantity: {LI_GREEN}{quantity}')
                print(f'{LI_WHITE}Link: {LI_GREEN}{order_link}')
                print(linex())
                while  opder_delev_list.count(order_id)<= quantity :
                    # with thd(max_workers=600) as main executor:
                        for cokis in my_cookes:
                            token = cokis.split('|')[1]
                            count_of_2 = opder_delev_list.count(order_id)
                            if count_of_2+700 >= quantity:
                                connect.update_oder_status(order_id)
                                print(f"{LI_GREEN}The Oder Is Complited : {LI_WHITE} {order_id}")
                                print(mahdilinx())
                                break
                            elif  count_of_2 < quantity:
                                try:
                                    thdes=Thread(target= submite,args=(token,order_link,order_id,))
                                    thdess.append(thdes)
                                    thdes.start()
                                    # slps(.2)
                                except:pass
                                # with thd(max_workers=600) as main executor:
                            #       sub.submit(submite,token,order_link,order_id)
                            
                                # slps(.0)

while True:
    threa = Thread(target=mains).start()
    slps(10)
