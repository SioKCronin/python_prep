#!/usr/bin/env python3

from datetime import datetime, timedelta
from random import random

from queue import QUEUE_CLASSES


def run_tests(queue_implementation):
    """
    A few simple assertions to ensure the queue actually works.

    Add your own!
    """
    queue = queue_implementation()
    assert queue.is_empty()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    queue.enqueue(3)
    queue.enqueue(4)
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.dequeue() == 4
    assert queue.is_empty()


def run_simulation(queue_implementation, p_enqueue=0.5, p_dequeue=0.5, duration=5):
    """
    Run a simulation where a producer periodically adds to a queue, and
    a consumer periodically pulls from it.
    """
    start = last_msg = datetime.now()
    delta = timedelta(seconds=duration)
    msg_freq = timedelta(seconds=0.2)
    num_enqueues = 0
    num_dequeues = 0
    max_queue_size = 0
    queue = queue_implementation()
    msg = "New message!"
    
    while True:
        now = datetime.now()
        elapsed = now - start

        if elapsed > delta:
            break

        if now - last_msg > msg_freq:
            print('\r\033[K{:20} {:.0f}\t\t{:.0f}\t\t{}'.format(
                q.__name__[:20],
                num_enqueues / elapsed.total_seconds(),
                num_dequeues / elapsed.total_seconds(),
                max_queue_size
            ), end='')
            last_msg = now

        if random() < p_enqueue:
            queue.enqueue((now, msg))
            num_enqueues += 1
            max_queue_size = max(max_queue_size, queue.size())

        if random() < p_dequeue:
            if not queue.is_empty():
                queue.dequeue()
                num_dequeues += 1

    print()


if __name__ == '__main__':
    for q in QUEUE_CLASSES:
        print("Running {}".format(q))
        run_tests(q)

    print('All implementations passing simple correctness test, benchmarking..')

    prob_pairs = [(.5, .5), (.6, .4), (.49, .51)]

    for p_enq, p_deq in prob_pairs:
        print('\n\033[1mBenchmarking for P(enqueue)={}, P(dequeue)={}\033[0m\n'.format(p_enq, p_deq))
        print('                     enqueues/sec\tdequeues/sec\tmax queue size')
        print('                     ---\t\t---\t\t---')
        for q in QUEUE_CLASSES:
            run_simulation(q, p_enq, p_deq)

