#-*- coding: utf-8 -*-
from dbmodel.entity import *

class Texto(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(max=45)
	def text_pagina(self): pass

	@String(max=65535)
	def text_texto_base(self): pass

	@String(max=65535)
	def text_estados(self): pass

	@String(max=65535)
	def text_sexos(self): pass