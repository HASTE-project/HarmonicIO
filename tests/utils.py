import asyncio
import os
import runpy
import sys
import time
from multiprocessing import Queue, Process
import subprocess

TIMEOUT = 5

def run_module(module_name, timeout_seconds=10):
    '''
    Run a python3 module in a sub-process, and block until completion/timeout.
    '''
    print('cwd: ' + os.getcwd())

    result = subprocess.run(['python',
                             '-m',
                             module_name],
                            # capture_output=True,
                            # text=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,

                            timeout=timeout_seconds,
                            cwd='test_root')
    return result


async def run_module_async(module_name, timeout_seconds=TIMEOUT):
    '''
    Run a python3 module in a sub-process, asynchronously.
    '''
    result_queue = Queue()
    p = Process(target=_run_module_async_inner, args=('process-' + module_name, module_name, result_queue))
    p.start()
    await asyncio.sleep(timeout_seconds)

    # Wait an extra second..
    p.join(timeout=0)

    return result_queue


def _run_module_async_inner(name, module_name, stdout_queue):
    try:
        results = run_module(module_name)
        stdout_queue.put(results)
    except subprocess.TimeoutExpired as ex:
        stdout_queue.put(ex)
