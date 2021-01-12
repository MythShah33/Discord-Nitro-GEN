import os
from time import sleep
import requests
import random
import string
from colorama import Fore


os.system("cls")

print(f"{Fore.GREEN}[ {Fore.CYAN}\u00A7 {Fore.GREEN}] {Fore.LIGHTYELLOW_EX}Discord Nitro Generator made by {Fore.CYAN}0xb4dc0d3x{Fore.LIGHTYELLOW_EX} | Licensed under {Fore.GREEN}MIT {Fore.LIGHTYELLOW_EX}License")

print(f"{Fore.GREEN}[ {Fore.CYAN}\u00A7 {Fore.GREEN}] {Fore.LIGHTMAGENTA_EX}You can follow me on Github: {Fore.WHITE}https://github.com/0xb4dc0d3x")
amount = int(input(f"\n{Fore.GREEN}[ {Fore.MAGENTA}> {Fore.GREEN}] {Fore.LIGHTGREEN_EX}How much codes will be generated: {Fore.GREEN}"))
print(f"\n{Fore.GREEN}[ {Fore.MAGENTA}? {Fore.GREEN}] {Fore.LIGHTBLACK_EX}Classic Nitro is 16chars and Boost Nitro is 24chars")
nitro = input(f"{Fore.GREEN}[ {Fore.MAGENTA}> {Fore.GREEN}] {Fore.LIGHTBLACK_EX}Boost codes or Classic codes {Fore.GREEN}(boost or classic){Fore.LIGHTBLACK_EX}: {Fore.GREEN}")

if "boost" in nitro or "classic" in nitro:
    pass
else:
    print(f"{Fore.GREEN}[ {Fore.RED}! {Fore.GREEN}] {Fore.LIGHTBLACK_EX}Answer must be {Fore.GREEN}boost {Fore.LIGHTBLACK_EX}or {Fore.GREEN}classic")
    exit()


checker = input(f"{Fore.GREEN}[ {Fore.YELLOW}> {Fore.GREEN}] {Fore.LIGHTBLACK_EX}Enable Checker {Fore.GREEN}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.GREEN}")
########## Proxy exctractor ##########
def scrape():
    scraped = 0
    f = open("proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500&ssl=yes')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        scraped = scraped + 1 
        f.write((p)+"\n")
    f.close()
    print(f"{Fore.GREEN}[ {Fore.YELLOW}? {Fore.GREEN}] {Fore.LIGHTBLACK_EX}Scraped {Fore.GREEN}{scraped} {Fore.LIGHTBLACK_EX}proxies.")

if checker == "yes":
    scrapep = input(f"{Fore.GREEN}[ {Fore.YELLOW}> {Fore.GREEN}] {Fore.LIGHTBLACK_EX}Auto proxy scrape {Fore.GREEN}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.GREEN}")
    print(f"\n{Fore.GREEN}[ {Fore.YELLOW}? {Fore.GREEN}] {Fore.LIGHTBLACK_EX}If no, every check will be on random proxy.")
    mult = input(f"{Fore.GREEN}[ {Fore.YELLOW}> {Fore.GREEN}] {Fore.LIGHTBLACK_EX}Multiple checks for proxy {Fore.GREEN}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.GREEN}")
    if scrapep == "yes":
        scrape()
else:
    print(f"\n{Fore.GREEN}[ {Fore.YELLOW}? {Fore.GREEN}] {Fore.LIGHTBLACK_EX}If true, before code will be {Fore.GREEN}discord.gift/")
    prefix = input(f"{Fore.GREEN}[ {Fore.YELLOW}> {Fore.GREEN}] {Fore.LIGHTBLACK_EX}Prefix before codes {Fore.GREEN}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.GREEN}")
    if "yes" in prefix or "no" in prefix:
        pass
    else:
        print(f"{Fore.GREEN}[ {Fore.RED}! {Fore.GREEN}] {Fore.LIGHTBLACK_EX}Answer must be {Fore.GREEN}yes {Fore.LIGHTBLACK_EX}or {Fore.GREEN}no")
        exit()


print(f"\n{Fore.GREEN}[ {Fore.YELLOW}? {Fore.GREEN}] {Fore.LIGHTBLACK_EX}Generating {Fore.GREEN}{amount}{Fore.LIGHTBLACK_EX} codes!")
if checker != "yes":
    sleep(1)

fulla = amount
f = open("codes.txt", "w+", encoding="UTF-8")
try:
    p = open("proxies.txt", encoding="UTF-8")
except FileNotFoundError:
    p = open("proxies.txt", "w+", encoding="UTF-8")
    print(f"{Fore.GREEN}[{Fore.RED} ! {Fore.GREEN}]{Fore.LIGHTBLACK_EX} No proxies found in {Fore.GREEN}proxies.txt!{Fore.GREEN}")
    raise SystemExit



rproxy = p.read().split('\n')
for i in rproxy:
    if i == "" or i == " ":
        index = rproxy.index(i)
        del rproxy[index]
p.close()

if not rproxy:
    print(f"{Fore.GREEN}[{Fore.RED} ! {Fore.GREEN}]{Fore.LIGHTBLACK_EX} No proxies found in {Fore.GREEN}proxies.txt!{Fore.GREEN}")
    raise SystemExit
########## Generaing codes ##########
if checker != "yes":
    while amount > 0:
        amount = amount - 1
        if "boost" in nitro:
            code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(24)])
        else:
            code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)])
        if prefix == "yes":
            print(f"{Fore.GREEN}[ {Fore.GREEN}+ {Fore.GREEN}] {Fore.LIGHTBLACK_EX}Generated code {Fore.GREEN}{code}")
            f.write(f"discord.gift/{code}\n")
        else:
            print(f"{Fore.GREEN}[ {Fore.GREEN}+ {Fore.GREEN}] {Fore.LIGHTBLACK_EX}Generated code {Fore.GREEN}{code}")
            f.write(f"{code}\n")

else:
    while amount > 0:
        f = open(f"working-codes.txt","a", encoding="UTF-8")
        try:
            if not rproxy[0]:
                print(f"{Fore.GREEN}[ {Fore.RED}! {Fore.GREEN}] {Fore.LIGHTBLACK_EX}All proxies are invalid!{Fore.GREEN}")
                exit()
        except:
            print(f"{Fore.GREEN}[ {Fore.RED}! {Fore.GREEN}] {Fore.LIGHTBLACK_EX}All proxies are invalid!{Fore.GREEN}")
            exit()
        if mult == "yes":
            proxi = rproxy[0]
        else:
            proxi = random.choice(rproxy)
        proxies = {
            "https": proxi
        }
        amount = amount - 1
        if "boost" in nitro:
            code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(24)])
        else:
            code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)])
        try:
            url = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}", proxies=proxies, timeout=3)
            if url.status_code == 200:
                print(f"{Fore.GREEN}[ {Fore.GREEN}+ {Fore.GREEN}] {Fore.LIGHTBLACK_EX}Working Code {Fore.GREEN}{code}{Fore.GREEN}")
                f.write(f"\ndiscord.gift/{code}")
                f.close()
            elif url.status_code == 404:
                fulla = fulla - 1
                print(f"{Fore.GREEN}[ {Fore.RED}- {Fore.GREEN}] {Fore.LIGHTBLACK_EX}Invalid Code {Fore.GREEN}{code}")
            elif url.status_code == 429:
                fulla = fulla - 1
                if mult == "yes":
                    print(f"{Fore.GREEN}[ {Fore.RED}- {Fore.GREEN}] {Fore.LIGHTBLACK_EX}Proxy {Fore.GREEN}{proxi}{Fore.LIGHTBLACK_EX} is ratelimited! | Switching proxy")
                else:
                    print(f"{Fore.GREEN}[ {Fore.RED}- {Fore.GREEN}] {Fore.LIGHTBLACK_EX}Proxy {Fore.GREEN}{proxi}{Fore.LIGHTBLACK_EX} is ratelimited!")
                index = rproxy.index(proxi)
                del rproxy[index]
            else:
                fulla = fulla - 1
                print(f"{Fore.GREEN}[ {Fore.RED}! {Fore.GREEN}] {Fore.LIGHTBLACK_EX}Invalid Error! | Status code {Fore.GREEN}{url.status_code}")
        except:
            index = rproxy.index(proxi)
            del rproxy[index]
            pw = open(f"proxies.txt","w", encoding="UTF-8")
            for i in rproxy:
                pw.write(i + "\n")
            pw.close()
            fulla = fulla - 1
            print(f"{Fore.GREEN}[ {Fore.RED}- {Fore.GREEN}] {Fore.LIGHTBLACK_EX}Failed connecting to proxy {Fore.GREEN}{proxi}{Fore.LIGHTBLACK_EX} | Removing from list!")

f.close()
print(f"{Fore.GREEN}[ {Fore.YELLOW}? {Fore.GREEN}] {Fore.LIGHTBLACK_EX}Successfully generated {Fore.GREEN}{fulla} {Fore.LIGHTBLACK_EX}codes!{Fore.GREEN}")

input()
