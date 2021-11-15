import logging
from unittest import TestCase, TestSuite, TextTestRunner
from Configuration import channels as Channel
from Configuration import global_parameters as cfg
from managers import redisManager as Mgr
from services.RedisServices import RedisPubSubService

TEST_MESSAGE = "Hello! I am message"


class TestRedisPubSubService(TestCase):
    def test_read_message(self):
        redis_subscriber = RedisPubSubService(Channel.Type.storageStatus)
        fetch_msg = redis_subscriber.subscriber.get_message(timeout=60)
        if fetch_msg['data'] == 1:
            fetch_msg = redis_subscriber.subscriber.get_message(timeout=60)
        self.assertEqual(TEST_MESSAGE, fetch_msg['data'])

    def test_publish_message(self):
        redis_publisher = RedisPubSubService(Channel.Type.storageCheck)
        deilvered_to = redis_publisher.publish_message(TEST_MESSAGE)
        self.assertIs(deilvered_to, None)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    test_suite = TestSuite()
    Mgr.RedisManager()
    test_suite.addTest(TestRedisPubSubService('test_read_message'))
    test_suite.addTest(TestRedisPubSubService('test_publish_message'))
    TextTestRunner(verbosity=2).run(test_suite)
