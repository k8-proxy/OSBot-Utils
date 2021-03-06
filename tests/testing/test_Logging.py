from unittest import TestCase
from unittest.mock import patch

from osbot_utils import testing
from osbot_utils.testing.Logging import Logging

#todo see https://opensource.com/article/17/9/python-logging for more capabilities to add to this class

class test_Logging(TestCase):

    def setUp(self):
        self.logging = Logging()

    # def test_is_pycharm_running(self):
    #     assert self.logging.is_pycharm_running()

    #todo: find way to mock/capture the output sent ot sys.stdout (since @patch('builtins.print') is not working)
    def test_enable_pycharm_logging(self):
        self.logging.enable_pycharm_logging()
        self.logging.info('aaaa')
        self.logging.warning('aaaa')
        self.logging.debug('aaaa')
        self.logging.error('aaaa')
        self.logging.critical('aaaa')

        # simulate case when is_pycharm_running returns True (for example when running tests in CI pipeline)
        self.logging.is_pycharm_running = lambda : True

        self.logging.enable_pycharm_logging()
        self.logging.info('aaaa')



    def test_log_to_string(self):
        stream_handler = self.logging.log_to_string_io()
        string_io      = stream_handler.stream

        self.logging.info   ('aaaa')
        self.logging.warning('warning')
        self.logging.debug  ('debug')
        self.logging.error  ('error')
        self.logging.critical('critical')
        assert string_io.getvalue() == """INFO - aaaa
WARNING - warning
DEBUG - debug
ERROR - error
CRITICAL - critical
"""

    def test_logger(self):
        # test default
        assert self.logging.logger().name == 'root'

        # test with specific name
        log_name = 'an log name'
        logging_with_name = Logging(log_name)
        assert logging_with_name.target == log_name
        assert logging_with_name.logger().name == log_name

        # test passing a class as target
        assert Logging(Logging).logger().name == Logging.__name__

        # test passing a module as target
        assert Logging(testing).logger().name == testing.__name__
