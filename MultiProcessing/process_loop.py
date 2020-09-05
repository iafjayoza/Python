import multiprocessing
import time
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return f"Done sleeping for {seconds} seconds ..."

# processes = []
#
# for _ in range(10):
#     t = multiprocessing.Process(target=do_something,args=[1.5])
#     t.start()
#     processes.append(t)
#
# for process in processes:
#     process.join()

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = [executor.submit(do_something,sec) for sec in secs]
    for i in concurrent.futures.as_completed(results):
        print(i.result())


end = time.perf_counter()

print(f"Finished in {round(end-start,2)} seconds")