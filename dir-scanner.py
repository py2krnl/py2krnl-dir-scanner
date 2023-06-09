import requests
import os
import threading

target_domain = str(input("Target domain > "))
wordlist_path = str(input("Wordlist Path > "))
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
                    url = f"https://{domain}/{data}"
                    t = threading.Thread(target=send_request, args=(url, header))
                    t.start()
                    threads.append(t)

                for t in threads:
                    t.join()
    except Exception as e:
        exit(e)

def send_request(url: str, header: dict):
    try:
        response = requests.get(url=url, headers=header , timeout=2.0)
        if response.ok:
            print(response.url)
    except Exception as e:
        exit(e)

if __name__ == "__main__":
    check(domain=target_domain, wordlist=wordlist_path, header=headers)
