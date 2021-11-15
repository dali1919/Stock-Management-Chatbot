"""
The action server 

"""
import logging
from typing import Any, Text, Dict, List
import json
import time
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from Configuration import channels as channel 
from Configuration import global_parameters as global_parameters
from itemModel import itemClass as itemClass
from managers import JsonManager as JsonManager
from managers import redisManager as redisManager
from services import RedisServices as RedisServices

class ActionLidCheck(Action):
    """
    Action to connect to redis and get the lid amount
        
    """

    def name(self) -> Text:
       return "action_lid_check"

    def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         item = "lid"
         try: 
            logging.debug("subscribing to storage_status.")
            Redis_connection_status = RedisServices.RedisPubSubService(channel.Type.storageStatus)
            logging.info("subscribtion to storage_status successful.")
            logging.debug("subscribing to storage_check.")
            Redis_connection_check = RedisServices.RedisPubSubService(channel.Type.storageCheck)
            logging.info("subscribtion to storage_check successful.")

            logging.debug("Setting up item builder.")
            item_builder = itemClass.ItemBuilder()

            logging.info("item builder ready.")
            item_builder.withitem(item)
            logging.info("item builder instantiated with true values.")
            logging.debug("Building item")

            item_model = item_builder.build()
            logging.info("item built with id: {}".format(id(item_model)))

            
            logging.debug("Serializing order for REDIS publish.")
            item_dict = item_model.get_item_dict()
            item_serialized = JsonManager.JsonManager.serialize_dict(item_dict)
            logging.info("item serialized for REDIS publish.")
            logging.info(item_serialized)

            logging.debug("Publishing to REDIS.")
            Redis_connection_check.publish_message(item_serialized)
            logging.info("Message sent successfully")
            time.sleep(15)
            logging.debug("Reading from REDIS.")
            msg = Redis_connection_status.read_message()
            temp = re.findall(r'\d+',msg)
            res = list(map(int, temp))
            logging.debug("destroying the Redis_connection")
            Redis_connection_check.__del__()
            Redis_connection_status.__del__()
         except Exception as e:
            logging.error("Could handel the request. \n {}".
                          format(traceback.print_stack())) 
         
         dispatcher.utter_message(text="The lid amount is: "+ str(res[0]))
         dispatcher.utter_message(text="The lid amount is: 10")
         return []
        



class ActionSeedBagCheck(Action):
    """
    Action to connect to redis and get the seedBag amount
        
    """

    def name(self) -> Text:
        return "action_seedBag_check"

    def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         item="seedBag"
         try: 
            logging.debug("subscribing to storage_status.")
            Redis_connection_status = RedisServices.RedisPubSubService(channel.Type.storageStatus)
            logging.info("subscribtion to storage_status successful.")
            logging.debug("subscribing to storage_check.")
            Redis_connection_check = RedisServices.RedisPubSubService(channel.Type.storageCheck)
            logging.info("subscribtion to storage_check successful.")


            logging.debug("Setting up item builder.")
            item_builder = itemClass.ItemBuilder()

            logging.info("item builder ready.")
            item_builder.withitem(item)
            logging.info("item builder instantiated with true values.")
            logging.debug("Building item")

            item_model = item_builder.build()
            logging.info("item built with id: {}".format(id(item_model)))

            
            logging.debug("Serializing order for REDIS publish.")
            item_dict = item_model.get_item_dict()
            item_serialized = JsonManager.JsonManager.serialize_dict(item_dict)
            logging.info("item serialized for REDIS publish.")

            logging.debug("Publishing to REDIS.")
            Redis_connection_check.publish_message(item_serialized)
            logging.info("Message sent successfully")

            
            
            logging.debug("Reading from REDIS.")
            Redis_connection_status.su
            msg = Redis_connection_status.read_message()
            temp = re.findall(r'\d+',msg)
            res = list(map(int, temp))
            logging.debug("destroying the Redis_connection")
            Redis_connection_check.__del__()
            Redis_connection_status.__del__()
         except Exception as e:
            logging.error("Could handel the request. \n {}".
                          format(traceback.print_stack()))
         
         dispatcher.utter_message(text="The lid amount is: "+ str(res[0]))
         dispatcher.utter_message(text="The lid amount is: 10")
         return []

class ActionPalletCheck(Action):
    """
    Action to connect to redis and get the pallet amount
         
    """

    def name(self) -> Text:
        return "action_pallet_check"

    def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         item="pallet"
         try: 
            logging.debug("subscribing to storage_status.")
            Redis_connection_status = RedisServices.RedisPubSubService(channel.Type.storageStatus)
            logging.info("subscribtion to storage_status successful.")
            logging.debug("subscribing to storage_check.")
            Redis_connection_check = RedisServices.RedisPubSubService(channel.Type.storageCheck)
            logging.info("subscribtion to storage_check successful.")

            logging.debug("Setting up item builder.")
            item_builder = itemClass.ItemBuilder()

            logging.info("item builder ready.")
            item_builder.withitem(item)
            logging.info("item builder instantiated with true values.")
            logging.debug("Building item")

            item_model = item_builder.build()
            logging.info("item built with id: {}".format(id(item_model)))

            
            logging.debug("Serializing order for REDIS publish.")
            item_dict = item_model.get_item_dict()
            item_serialized = JsonManager.JsonManager.serialize_dict(item_dict)
            logging.info("item serialized for REDIS publish.")

            logging.debug("Publishing to REDIS.")
            Redis_connection_check.publish_message(item_serialized)
            logging.info("Message sent successfully")

            
            
            logging.debug("Reading from REDIS.")
            msg = Redis_connection_status.read_message()
            temp = re.findall(r'\d+',msg)
            res = list(map(int, temp))
            logging.debug("destroying the Redis_connection")
            Redis_connection_check.__del__()
            Redis_connection_status.__del__()
         except Exception as e:
            logging.error("Could handel the request. \n {}".
                          format(traceback.print_stack()))
         
         dispatcher.utter_message(text="The pallet amount is: "+ str(res[0]))
         dispatcher.utter_message(text="The pallet amount is: 10 ")
         return []



class ActionPaperCupCheck(Action):
    """
    Action to connect to redis and get the paperCup amount
        
    """

    def name(self) -> Text:
        return "action_paperCup_check"

    def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         item="paperCup"
         try: 
            logging.debug("subscribing to storage_status.")
            Redis_connection_status = RedisServices.RedisPubSubService(channel.Type.storageStatus)
            logging.info("subscribtion to storage_status successful.")
            logging.debug("subscribing to storage_check.")
            Redis_connection_check = RedisServices.RedisPubSubService(channel.Type.storageCheck)
            logging.info("subscribtion to storage_check successful.")

            logging.debug("Setting up item builder.")
            item_builder = itemClass.ItemBuilder()

            logging.info("item builder ready.")
            item_builder.withitem(item)
            logging.info("item builder instantiated with true values.")
            logging.debug("Building item")

            item_model = item_builder.build()
            logging.info("item built with id: {}".format(id(item_model)))

            
            logging.debug("Serializing order for REDIS publish.")
            item_dict = item_model.get_item_dict()
            item_serialized = JsonManager.JsonManager.serialize_dict(item_dict)
            logging.info("item serialized for REDIS publish.")

            logging.debug("Publishing to REDIS.")
            Redis_connection_check.publish_message(item_serialized)
            logging.info("Message sent successfully")

            
            logging.debug("Reading from REDIS.")
            msg = Redis_connection_status.read_message()
            temp = re.findall(r'\d+',msg)
            res = list(map(int, temp))
            logging.debug("destroying the Redis_connection")
            Redis_connection_check.__del__()
            Redis_connection_status.__del__()
         except Exception as e:
            logging.error("Could handel the request. \n {}".
                          format(traceback.print_stack()))
         
         dispatcher.utter_message(text="The lid amount is: "+ str(res[0]))
         dispatcher.utter_message(text="The paperCup amount is: 10 ")
         return []


class ActionPlasticCupCheck(Action):
    """
    Action to connect to redis and get the paperCup amount
        
    """

    def name(self) -> Text:
        return "action_plasticCup_check"

    def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         item="plasticCup"
         try: 
            logging.debug("subscribing to storage_status.")
            Redis_connection_status = RedisServices.RedisPubSubService(channel.Type.storageStatus)
            logging.info("subscribtion to storage_status successful.")
            logging.debug("subscribing to storage_check.")
            Redis_connection_check = RedisServices.RedisPubSubService(channel.Type.storageCheck)
            logging.info("subscribtion to storage_check successful")

            logging.debug("Setting up item builder.")
            item_builder = itemClass.ItemBuilder()

            logging.info("item builder ready.")
            item_builder.withitem(item)
            logging.info("item builder instantiated with true values.")
            logging.debug("Building item")

            item_model = item_builder.build()
            logging.info("item built with id: {}".format(id(item_model)))

            
            logging.debug("Serializing order for REDIS publish.")
            item_dict = item_model.get_item_dict()
            item_serialized = JsonManager.JsonManager.serialize_dict(item_dict)
            logging.info("item serialized for REDIS publish.")

            logging.debug("Publishing to REDIS.")
            Redis_connection_check.publish_message(item_serialized)
            logging.info("Message sent successfully")

            
            
            logging.debug("Reading from REDIS.")
            msg = Redis_connection_status.read_message()
            temp = re.findall(r'\d+',msg)
            res = list(map(int, temp))
            logging.debug("destroying the Redis_connection")
            Redis_connection_check.__del__()
            Redis_connection_status.__del__()
         except Exception as e:
            logging.error("Could handel the request. \n {}".
                          format(traceback.print_stack()))
         
         dispatcher.utter_message(text="The lid amount is: "+ str(res[0]))
         dispatcher.utter_message(text="The plasticCup amount is: 10")
         return []

class ActionPlasticCupUpdate(Action):
    """
    Action to connect to redis and get the paperCup amount
        
    """

    def name(self) -> Text:
        return "action_plasticCup_update"

    def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
     
         
         dispatcher.utter_message(text="The plasticCup is updated successfully!!!" )
         return []
class ActionPaperCupUpdate(Action):
    """
    Action to connect to redis and get the paperCup amount
        
    """

    def name(self) -> Text:
        return "action_paperCup_update"

    def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
         
         dispatcher.utter_message(text="The plasticCup is updated seccuessfully!!!"+ data )
         return []
class ActionLidUpdate(Action):
    """
    Action to connect to redis and get the paperCup amount
        
    """

    def name(self) -> Text:
        return "action_lid_update"

    def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
         
         dispatcher.utter_message(text="The lid is updated seccuessfully!!!")
         return []
         
         
class ActionSeedBagUpdate(Action):
    """
    Action to connect to redis and get the paperCup amount
        
    """

    def name(self) -> Text:
        return "action_seedBag_update"

    def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
         
         dispatcher.utter_message(text="The seedBag is updated seccuessfully!!!")
         return []
class ActionPalletUpdate(Action):
    """
    Action to connect to redis and get the paperCup amount
        
    """

    def name(self) -> Text:
        return "action_pallet_update"

    def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
         
         dispatcher.utter_message(text="The pallet is updated seccuessfully!!!")
         return []
         




