import asyncio

from tests.utils import run_module_async, TIMEOUT

import sys
import os

# We test that the worker and master run (and don't terminate within a timeout), and that things happen successfully by looking at the log output (and


async def _inner_test_master_and_worker():
    results = await asyncio.gather(
        run_module_async('harmonicIO.master', TIMEOUT),
        run_module_async('harmonicIO.worker', TIMEOUT)
    )

    return results


def test_master_and_worker():
    '''
    Start the master and  the worker, and assert that a report is sent to the master, and received by it successfully.
    '''

    results = asyncio.run(_inner_test_master_and_worker())
    print(results)

    master_timeout_expired_ex = results[0].get()
    worker_timeout_expired_ex = results[1].get()

    master_stdout_lines = master_timeout_expired_ex.stdout.split('\n')
    master_stderr_lines = master_timeout_expired_ex.stderr.split('\n')

    worker_stdout_lines = worker_timeout_expired_ex.stdout.split('\n')
    worker_stderr_lines = worker_timeout_expired_ex.stderr.split('\n')

    print(master_stdout_lines)
    print(master_stderr_lines)
    # ['[OUT: Running Harmonic Master]',
    #  '[OUT: Load setting successful.]',
    #  '[OUT: Node name: PE Master]',
    #  '[OUT: Node address: 127.0.0.1]',
    #  '[OUT: Node port: 8080]',
    #  '[OUT: Enable Messaging System on port: 8090]',
    #  '[OUT: REST Ready.....]',
    #  '[DEB: Update worker status (PE Worker)]',
    #  '[DEB: Update worker status (PE Worker)]',
    #  '']
    # ['127.0.0.1 - - [28/Jan/2019 14:11:24] "PUT /status?token=None HTTP/1.1" 200 4',
    #  '127.0.0.1 - - [28/Jan/2019 14:11:29] "PUT /status?token=None HTTP/1.1" 200 4',
    #  '']

    assert '[DEB: Update worker status (PE Worker)]' in master_stdout_lines

    print(worker_stdout_lines)
    print(worker_stderr_lines)
    # ['[OUT: Running Harmonic Worker]',
    #  '[OUT: Load setting successful.]',
    #  '[OUT: Node name: PE Worker]',
    #  '[OUT: Node internal address: 127.0.0.1]',
    #  '[OUT: Node port: 8081]',
    #  '[OUT: Port range: 9000 to 9010 (10 ports available)]',
    #  '[OUT: Docker master initialization complete.]',
    #  '[DEB: Reports status to master node complete.]',
    #  '[OUT: REST Ready.....]',
    #  '[DEB: Reports status to master node complete.]',
    #  '']
    # ['']
    assert '[DEB: Reports status to master node complete.]' in worker_stdout_lines
