#-*- coding: utf-8 -*-
from dbmodel.entity import *

class Indicacao(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(max=155)
	def ind_remetente(self): pass

	@String(max=155)
	def ind_remetente_email(self): pass

	@String(max=155)
	def ind_destinatario(self): pass

	@String(max=155)
	def ind_destinatario_email(self): pass