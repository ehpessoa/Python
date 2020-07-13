from concurrent import futures

import requests

with futures.ThreadPoolExecutor(max_workers=1000) as executor:
    futures = [
        executor.submit(
            lambda: requests.get("https://github.com/ehpessoa/"))
        for _ in range(10)
    ]

results = [
    f.result().status_code
    for f in futures
]

print("Results: %s" % results)
