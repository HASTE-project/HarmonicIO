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
    print('executable: ' + sys.executable)
    print('base prefix: ' + sys.base_prefix)
    # print('executable: ' + sys.real_prefix )

    result = subprocess.run([sys.executable,
                             '-m',
                             module_name],
                            # Note, compatible with 3.5.x here:
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            universal_newlines=True,

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
