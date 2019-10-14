#-*- coding: utf-8 -*-

__private_methods__ = ["toJSON"]

from enum import Enum

from dbmodel.entity.datatype  import *


class EntityStatus(Enum):
    created = 1
    filled = 2
    modified = 3

class Entity(object):

    def __init__(self, status=1, **kw):
        try:
            self.__status__ = EntityStatus(status)
            for item in self.__dir__():
                if not item.startswith("__") and item not in __private_methods__:
                    self.__dict__["__%s"%item] = self.__getattribute__(item)
                    if self.__dict__["__%s"%item].name and not self.__dict__["__%s"%item].type:
                        self.__dict__["__%s"%item].type = getattr(__import__('model.{0}'.format(self.__dict__["__%s"%item].name.lower()), fromlist=[self.__dict__["__%s"%item].name]), self.__dict__["__%s"%item].name)
                    self.__dict__[item] = None if self.__dict__["__%s"%item].__class__.__name__ != "ObjectList" else ListType(self.__dict__["__%s"%item].type)
                    if item in kw:
                        self.__setattr__(item, kw[item])
                        del kw[item]
            if len(kw) > 0:
                self.__setrelattr__(**kw)
        except Exception as e:
            raise e

    def __setrelattr__(self, **kw):
        relation_kw = {item.split(".")[0]: {value[0].split(".")[1]:value[1] for value in kw.items() if item.split(".")[0] in value[0]} for item in sorted(kw) if "." in item}
        for _table, _data in relation_kw.items():
            if self.__dict__["__%s"%_table].__class__.__name__ == "Object" or isinstance(_data, list):
                self.__setattr__(_table, _data)
            if self.__dict__["__%s"%_table].__class__.__name__ == "ObjectList" and isinstance(_data, dict):
                self.__setattr__(_table, [_data])

    def __setattr__(self, item, value):
        try:
            if not item.startswith("__"):
                if hasattr(self, "__%s"%item):
                    self.__status__ = EntityStatus(3)
                    field = self.__getattribute__("__%s"%item)
                    if field.type and field.__class__.__name__ is "ObjectList" and isinstance(value, list):
                        for item_list in value:
                            if isinstance(item_list, dict):
                                self.__dict__[item].append(field.type(**item_list))
                            if isinstance(item_list, field.type):
                                self.__dict__[item].append(item_list)
                    else:
                        if field.type and isinstance(value, dict):
                            field.value = field.type(**value)
                        else:
                            field.value = value
                        self.__dict__[item] = field.value
                else:
                    raise Exception("%s field does not exist"%item)
            else:
                super().__setattr__(item, value)
        except Exception as e:
            raise e

    def toJSON(self, encode=False):
        try:
            return {k: CustomEncoder(v, self.__getattribute__("__%s"%k), encode) if encode else v if not hasattr(v, "toJSON") else v.toJSON() for k, v in self.__dict__.items() if not k.startswith("__") and v is not None }
        except Exception as e:
            raise e

def CustomEncoder(item, datatype, encode=False):
	try:
		if hasattr(item, "toJSON"):
			return item.toJSON(encode)
		if isinstance(item, decimal.Decimal):
			return float(item)
		if isinstance(item, datetime.datetime):
			return item.strftime("%d/%m/%Y %H:%M:%S")
		if isinstance(item, bytes):
			return item.decode('utf-8')
		return item
	except Exception as e:
		raise e
