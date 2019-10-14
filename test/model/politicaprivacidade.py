#-*- coding: utf-8 -*-
from dbmodel.entity import *

class PoliticaPrivacidade(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(max=45)
	def pol_titulo(self): pass

	@String(max=65535)
	def pol_texto(self): pass

	@Int(precision = 10, scale=0)
	def pol_ordem(self): pass