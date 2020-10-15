# MIT License
#
# Copyright (c) 2020 Evgeny Medvedev, evge.medvedev@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import logging
import threading
import time


class RateLimitingProxy:
    def __init__(self, delegate, max_per_second=5):
        self._lock = threading.Lock()
        self._delegate = delegate
        self._min_interval = 1.0 / max_per_second
        self._last_time_called = time.perf_counter()
        self._wait_buffer = 0.001

    def __getattr__(self, name):
        self._lock.acquire()
        try:
            elapsed = time.perf_counter() - self._last_time_called
            left_to_wait = self._min_interval - elapsed + self._wait_buffer
            if left_to_wait > 0:
                logging.debug(f'Waiting {left_to_wait} seconds because of rate limiting')
                time.sleep(left_to_wait)

            return getattr(self._delegate, name)
        finally:
            self._last_time_called = time.perf_counter()
            self._lock.release()
