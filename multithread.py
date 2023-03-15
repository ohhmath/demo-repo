import time
import threading
import concurrent.futures
start = time.perf_counter()

def do_something(second):
	print("Sleeping 1 second...")
	time.sleep(second)
	return "done sleeping"

with concurrent.futures.ThreadPoolExecutor() as executor:
	results = [executor.submit(do_something, 1) for _ in range(10)]

	for f in concurrent.futures.as_completed(results):
		print(f.result())

finish = time.perf_counter()

print(f'Finished in {round(finish-start), 2} second(s)')