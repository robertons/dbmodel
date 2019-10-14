#-*- coding: utf-8 -*-
from dbmodel.entity import *

class Newsletter(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(max=45)
	def news_nome(self): pass

	@String(max=155)
	def news_email(self): pass