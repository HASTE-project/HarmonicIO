import sys

import pytest
import os

os.environ['PYTHONUNBUFFERED'] = '1'

# It seems there are issues with pytest plugins which break the tests.
# It works if running from PyCharm (using the runner).
# Or using this script (but not directly from the terminal).

exit_code = pytest.main([], [])
sys.exit(exit_code)