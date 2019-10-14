#-*- coding: utf-8 -*-
from dbmodel.entity import *

class Faq(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(max=45)
	def faq_pergunta(self): pass

	@String(max=65535)
	def faq_resposta(self): pass

	@Int(precision = 3, scale=0)
	def faq_publicado(self): pass