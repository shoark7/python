import urllib.request

from concurrent.futures import ThreadPoolExecutor, as_completed


def make_requests(i: int) -> str: 
   response = urllib.request.urlopen('http://127.0.0.1:8080')
   html = response.read()
   return str(i).encode()

with ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(make_requests, i) for i in range(4)}
    for future in as_completed(future_to_url):
        data = future.result()
        print(f"{data=}")