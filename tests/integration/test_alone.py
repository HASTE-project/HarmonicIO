import os
import subprocess
import sys

import pytest

from tests.utils import run_module, TIMEOUT


# We test that the worker and master run (and don't terminate within a timeout), and that things happen successfully by looking at the log output (and


def test_worker():
    '''
    Assert that the worker starts successfully
    '''
    # if sys.version_info < (3, 6):
    #     return

    with pytest.raises(subprocess.TimeoutExpired) as ex_info:
        # Start the worker by itself, check that it initializes:
        result = run_module('harmonicIO.worker', timeout_seconds=TIMEOUT)

        print(result)
        # Should not have terminated within the timeout (sanity check)
        assert False

    stdout_lines = ex_info.value.stdout.split('\n')
    print(stdout_lines)
    print(ex_info.value.stderr)

    for expected in ['[OUT: Load setting successful.]',
                     '[OUT: Docker master initialization complete.]',  # note the typo!
                     ]:
        assert expected in stdout_lines


def test_master():
    '''
    Assert that the master starts successfully
    '''

    with pytest.raises(subprocess.TimeoutExpired) as ex_info:
        # Start the worker by itself, check that it initializes:
        result = run_module('harmonicIO.master', timeout_seconds=TIMEOUT)

        print(result)
        # Should not have terminated within the timeout (sanity check)
        assert False

    stdout_lines = ex_info.value.stdout.split('\n')
    print(stdout_lines)
    print(ex_info.value.stderr)

    for exp in ['[OUT: Load setting successful.]',
                '[OUT: Enable Messaging System on port: 8090]',
                '[OUT: REST Ready.....]']:
        assert exp in stdout_lines
