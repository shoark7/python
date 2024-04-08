import threading
import queue
import time
import random


MAX_QUEUE_SIZE = 5
NUM_PRODUCERS = 1
NUM_CONSUMERS = 3

shared_queue = queue.Queue()
lock = threading.Lock()


def producer():
    while True:
        item = random.randint(1, 100)
        with lock:
            if shared_queue.qsize() < MAX_QUEUE_SIZE:
                shared_queue.put(item)
                print(f"Produced item: {item}, Queue size: {shared_queue.qsize()}")
        time.sleep(random.uniform(0.5, 1.5))


def consumer(no: int):
    while True:
        with lock:
            if not shared_queue.empty():
                item = shared_queue.get()
                print(f"No.{no} Consumed item: {item}, Queue size: {shared_queue.qsize()}")
        time.sleep(random.uniform(0.5, 1.5))


producer_threads = []
for _ in range(NUM_PRODUCERS):
    t = threading.Thread(target=producer)
    producer_threads.append(t)
    t.start()


consumer_threads = []
for i in range(NUM_CONSUMERS):
    t = threading.Thread(target=consumer, args=(i,))
    consumer_threads.append(t)
    t.start()


for t in producer_threads:
    t.join()


for t in consumer_threads:
    t.join()
