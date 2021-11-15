"""
Item class to include all fields as expected in the storage_chek json.

"""

class ItemModel:
    def __init__(self, item="" ):
       
        self.__item_dic = {"item": item}   

    def set_item(self, item):
        self.__item_dic["item"] = item

    def get_item_dict(self):
        return self.__item_dic


class ItemBuilder:

    def __init__(self):
        self.item = ""
        

    def withitem(self, item):
        self.item = item
        return self


    def build(self):
        return ItemModel(item=self.item)

