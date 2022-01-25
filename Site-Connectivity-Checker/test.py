import requests, time
import socket

connectivity = False
temp = 0

ipaddress = socket.gethostbyname(socket.gethostname())
if ipaddress == "127.0.0.1":
    print("No internet, Site Connectivity Checker unavailable")
    check = input("\nThe system is facing internet connectivity issues\nDo you wish to continue ? (Y/N)")
    if check == "Y" or check == 'y':
        connectivity = True
else:
    print("Internet Connected, Site Connectivity Checker live")
    connectivity = True

if connectivity:

    print("\n---> This is a Site Connectivity Checker <---\n")
    print("Input your URL in the following format 'http://www.google.com'")


    def initialize():
        url = input("Enter a URL to check: ")
        if url == "":
            url = "http://www.google.com"
        diff = input(f"Ping {url} on an interval of (seconds): ")
        if diff == "":
            diff = 1
        count = input(f"Ping {url} for how many times (number of times): ")
        if count == "":
            count = 1
            count = int(count)
        return url, diff, count


    url, diff, count = initialize()
    print("")
    # response = requests.get(url)

    while True:

        try:

            response = requests.get(url)
            status_code = response.status_code
            if status_code == 200:
                print(f"{url} is LIVE, the site responded with a status code {status_code}")
            if status_code == 301:
                print(
                    f"{url} is UNAVAILABLE, the site Moved Permanently and responded with a status code {status_code}")
            if status_code == 302:
                print(
                    f"{url} is UNAVAILABLE, the site Moved TEMPORARILY and responded with a status code {status_code}")
            if status_code == 404:
                print(f"{url} is UNAVAILABLE, the site was NOT FOUND and responded with a status code {status_code}")
            if status_code == 500:
                print(
                    f"{url} is UNAVAILABLE, the site is having an INTERNAL SERVER ERROR and responded with a status code {status_code}")
            if status_code == 503:
                print(
                    f"{url} is UNAVAILABLE, the site's SERVICE is UNAVAILABLE and responded with a status code {status_code}")


        except Exception as e:
            print(e)
            url = input("\nEnter another URL to check: ")
            diff = input(f"Ping {url} on an interval of (seconds): ")
            count = input(f"Ping {url} for how many times (number of times): ")
        time.sleep(int(diff))
        temp = temp + 1
        if temp == int(count):
            temp = 0
            print(f"\n{url} was pinged for {count} times\n")
            url, diff, count = initialize()
            print("")
