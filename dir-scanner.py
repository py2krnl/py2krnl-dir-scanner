#!/usr/bin/env python
import argparse
import requests
import os
import threading
from colorama import Fore
import sys


version = 0.01

headers = {
    "User-Agent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Sec-Ch-Ua": "AppleWebKit/605.1.15",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "iPhone",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document"
}




def check(domain: str, wordlist: str, header: dict):
    try:
        if os.path.exists(wordlist):
            with open(wordlist, "r") as wordlist_file:
                _data = wordlist_file.readlines()
                threads = []
                for data in _data:
                    data = data.rstrip()
                    url = f"{args.protocol}://{domain}/{data}"
                    t = threading.Thread(target=send_request, args=(url, header))
                    t.start()
                    threads.append(t)

                for t in threads:
                    t.join()
    except Exception as e:
        exit(e)

def send_request(url: str, header: dict):
    try:
        response = requests.get(url=url, headers=header , timeout=5.0 , allow_redirects=False)
        if response.status_code >= 200 and response.status_code <= 299:
            print(f"[{Fore.GREEN}+{Fore.RESET}]  {response.url:<37} \t{Fore.GREEN}({Fore.RESET}STATUS:{response.status_code}|SIZE:{len(response.content)}{Fore.GREEN}){Fore.RESET}")
        elif response.status_code >= 300 and response.status_code <= 399:
            print(f"[{Fore.YELLOW}*{Fore.RESET}]  {response.url:<37} \t{Fore.YELLOW}({Fore.RESET}STATUS:{response.status_code}|SIZE:{len(response.content)}{Fore.YELLOW}){Fore.RESET}")
        else:
            pass
    except Exception as e:
        exit(e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Directory Scanning Tool", usage=f"python {sys.argv[0]} --protocol http --target-domain example.com --wordlist-path wordlist.txt")
    parser.add_argument("-p","--protocol", type=str, help="Protocol (http or https)")
    parser.add_argument("-t","--target-domain", type=str, help="Target domain")
    parser.add_argument("-w","--wordlist-path", type=str, help="Wordlist path")


    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)


    args = parser.parse_args()

    os.system("clear")
    print(f"\n* * * Target is: {args.target_domain} * * *\n")
    print("")

    check(domain=args.target_domain, wordlist=args.wordlist_path, header=headers)