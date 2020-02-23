from concurrent import futures

import requests

with futures.ThreadPoolExecutor(max_workers=6) as executor:
    futures = [
        executor.submit(
            lambda: print("testing"))
        for _ in range(12)
    ]
