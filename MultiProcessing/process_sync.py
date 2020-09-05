import multiprocessing

def withdraw(balance,lock):
    for _ in range(10000):
        lock.acquire()
        balance.value -= 1
        lock.release()

def depoosit(balance,lock):
    for _ in range(10000):
        lock.acquire()
        balance.value += 1
        lock.release()

def perform_transactions():
    # initial balance (in shared memory)
    balance = multiprocessing.Value('i', 100)

    # creating a lock object
    lock = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=withdraw,args=(balance,lock))
    p2 = multiprocessing.Process(target=depoosit,args=(balance,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f'final balance = {balance.value}')

for _ in range(10):
    perform_transactions()