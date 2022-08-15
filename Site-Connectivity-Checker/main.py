import requests, time

print("\n---> This is a Site Connectivity Checker <---\n")
print("Input your URL in the following format 'http://www.google.com'")
url = "http://google.com"
diff = 1
count = 1
flag = 1

def initialize():
    url = input("Enter a URL to check: ")
    diff = input(f"Ping {url} on an interval of (seconds): ")
    count = input(f"Ping {url} for how many times (number of times): ")
    return url, diff, count

def site_is_online(url, timeout=2):
    """Return True if the target URL is online.

    Raise an exception otherwise.
    """
    error = Exception("unknown error")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            connection.request("HEAD", "/")
            return True
        except Exception as e:
            error = e
        finally:
            connection.close()
    raise error


url, diff, count = initialize()
print("")

while True:

    try:
        if flag % (int(count) + 1) == 0:
            print(f"\n{url} was pinged for {count} times")
            print("")
            url, diff, count = initialize()
            print("")

        response = requests.get(url)
        status_code = response.status_code
        # print("Enter 'Q' to stop")
        if status_code == 200:
            print(f"{url} is LIVE, the site responded with a status code {status_code}")
        if status_code == 301:
            print(f"{url} is UNAVAILABLE, the site Moved Permanently and responded with a status code {status_code}")
        if status_code == 302:
            print(f"{url} is UNAVAILABLE, the site Moved TEMPORARILY and responded with a status code {status_code}")
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
    flag = flag + 1
