'''
This class is a manager for Redis Connections. It is a Singleton class to ensure
that not many objects are created for interfacing with Redis. Only one manager object would exist.

'''
import redis
import traceback
from Configuration import global_parameters as  globals


class RedisManager:

    __redis_connector = None

    @staticmethod
    def get_instance():
        if RedisManager.__redis_connector is None:
            RedisManager()
        return RedisManager.__redis_connector


    def __init__(self):
        """ Virtually private constructor. """
        if RedisManager.__redis_connector is not None:
            raise Exception("RedisManager is singleton!")
        else:
            try:
                RedisManager.__redis_connector = self
                RedisManager.__redis_connector = redis.StrictRedis(host=globals.REDIS_LOCAL_HOSTNAME,
                                                                   port=globals.REDIS_LOCAL_HOST_PORT,
                                                                   decode_responses=True)
         
                print("REDIS CONNECTED SUCCESSFULLY!!!!")
            except Exception as e:
                print("Error in connecting to the Redis server.")
                print(str(e))
                print(traceback.format_exc())
                RedisManager.__redis_connector = None
                
                