import os
import subprocess
import sys

import pytest

from tests.utils import run_module


# We test that the worker and master run (and don't terminate within a timeout), and that things happen successfully by looking at the log output (and


def test_worker():
    '''
    Assert that the worker starts successfully
    '''

    if os.environ['TRAVIS'] == 'true':
        # This test doesn't work on Travis at all.
        # TODO: fix
        return

    with pytest.raises(subprocess.TimeoutExpired) as ex_info:
        # Start the worker by itself, check that it initializes:
        result = run_module('harmonicIO.worker', timeout_seconds=10)

        print(result)
        # Should not have terminated within the timeout (sanity check)
        assert False

    stdout_lines = ex_info.value.stdout.split('\n')
    print(stdout_lines)

    for expected in ['[OUT: Load setting successful.]',
                     '[OUT: Docker master initialization complete.]',  # note the typo!
                     ]:
        assert expected in stdout_lines


def test_master():
    '''
    Assert that the master starts successfully
    '''

    if os.environ['TRAVIS'] == 'true':
        # This test doesn't work on Travis at all.
        # TODO: fix
        return

    with pytest.raises(subprocess.TimeoutExpired) as ex_info:
        # Start the worker by itself, check that it initializes:
        result = run_module('harmonicIO.master', timeout_seconds=10)

        print(result)
        # Should not have terminated within the timeout (sanity check)
        assert False

    stdout_lines = ex_info.value.stdout.split('\n')
    print(stdout_lines)

    for exp in ['[OUT: Load setting successful.]',
                '[OUT: Enable Messaging System on port: 8090]',
                '[OUT: REST Ready.....]']:
        assert exp in stdout_lines
