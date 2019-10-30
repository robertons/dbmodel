#-*- coding: utf-8 -*-
from dbmodel.entity import *

class StatAcompanhanteDiaTrafego(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_dia(self): pass

	@String(max=150)
	def trafego_origem(self): pass

	@String(max=100)
	def trafego_local_clique(self): pass

	@String(max=50)
	def trafego_ip(self): pass

	@Int(precision = 10, scale=0)
	def stat_ano(self): pass

	@Int(precision = 10, scale=0)
	def stat_mes(self): pass

	@Int(precision = 10, scale=0)
	def stat_dia(self): pass

	# One-to-One

	@Object(name="StatAcompanhanteDia", key="id", reference="id_dia", table="stat_acompanhante_dia")
	def stat_acompanhante_dia(self):pass