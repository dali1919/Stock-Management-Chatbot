import logging
from unittest import TestCase, TextTestRunner, TestSuite
from managers import redisManager

class TestRedisManager(TestCase):
    def test_get_instance(self):
        redisManager.RedisManager()
        redis =redisManager.RedisManager.get_instance()
        self.assertEqual(redis, redisManager.RedisManager.get_instance())

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    test_suite = TestSuite()
    test_suite.addTest(TestRedisManager('test_get_instance'))
    TextTestRunner(verbosity=2).run(test_suite)
    