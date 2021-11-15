"""
Redis pub-sub service. This client implements and provides redis publisher-subscriber services

"""
import sys
import logging
import time
import traceback
import typing 
import json
from Configuration import channels as Channel
from Configuration import global_parameters as cfg
from managers import redisManager as Mgr


class RedisPubSubService:
    def __init__(self, channel_type):
        """
        Constructor to initialise RedisService. Depending on the :param channel_type as defined by
        {@see configuration/channels.py}, the relevant object subscribing to the given channel is created.
        :param channel_type:
        :raises Exception if wrong channel type provided or error in subscription.
        """
        self.exec_message = None
        try:
            self.subscriber = Mgr.RedisManager.get_instance().pubsub()
            self.channel_type = channel_type
            if channel_type == Channel.Type.storageCheck:
                self.subscriber.subscribe(cfg.REDIS_LOCAL_STORAGE_CHECK_CHANNEL)
                self.channel = cfg.REDIS_LOCAL_STORAGE_CHECK_CHANNEL
            elif channel_type == Channel.Type.storageStatus:
                self.subscriber.subscribe(cfg.REDIS_LOCAL_STORAGE_STATUS_CHANNEL)
                self.channel = cfg.REDIS_LOCAL_STORAGE_STATUS_CHANNEL
            else:
                self.exec_message = 'No such redis channel configured.'

        except Exception as e:
            logging.error("Error in subscribing to the source channel.")
            logging.error(str(e))
            logging.error(traceback.format_exc())
        if self.exec_message:
            raise Exception(self.exec_message)

    def read_message(self):
        """
        Method to read a message from a Redis channel.
        :return: Message read.
        """
        
        message = "no message"
        self.subscriber.get_message()
        message_json = self.subscriber.get_message()['data']
        if message_json:
           message = json.dumps(message_json)
        return message
        

    def publish_message(self, message):
        """
        Method to publish a message to the Redis channel.
        :param message: Message to be published.
        """
        manager = Mgr.RedisManager.get_instance()
        manager.publish("storageCheck", message)

    def __del__(self):
        print("RedisPubSubService destroyed")
