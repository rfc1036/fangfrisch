"""
Copyright © 2020 Ralph Seichter

This file is part of "Fangfrisch".

Fangfrisch is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Fangfrisch is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Fangfrisch. If not, see <https://www.gnu.org/licenses/>.
"""
import logging
import unittest

import fangfrisch.log
from fangfrisch.log import LogHandlerType
# noinspection PyProtectedMember
from fangfrisch.log import _create_handler
from fangfrisch.log import init_logger


class LogTests(unittest.TestCase):
    level = logging.FATAL
    fmt = r'%(message)s'

    def setUp(self) -> None:
        super().setUp()
        fangfrisch.log._handler = None
        fangfrisch.log._logger = None

    def test_init_console_handler(self):
        x = _create_handler(LogHandlerType.CONSOLE, self.level, self.fmt, '')
        self.assertTrue(isinstance(x, logging.Handler))

    def test_init_syslog_handler(self):
        x = _create_handler(LogHandlerType.SYSLOG, self.level, self.fmt, 'localhost')
        self.assertTrue(isinstance(x, logging.Handler))
        x.close()

    def test_init_syslog_handler_port(self):
        x = _create_handler(LogHandlerType.SYSLOG, self.level, self.fmt, '127.0.0.1:514')
        self.assertTrue(isinstance(x, logging.Handler))
        x.close()

    def test_init_logger(self):
        x = init_logger(LogHandlerType.CONSOLE)
        self.assertTrue(isinstance(x, logging.Logger))


if __name__ == '__main__':
    unittest.main()