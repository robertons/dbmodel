#-*- coding: utf-8 -*-
from dbmodel.entity import *

class TextoVariavel(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(max=45)
	def var_name(self): pass

	@String(max=45)
	def var_example(self): pass

	@String(max=45)
	def var_table(self): pass

	@String(max=45)
	def var_tipo(self): pass

	@String(max=155)
	def var_link(self): pass

	@String(max=155)
	def var_key(self): pass