#-*- coding: utf-8 -*-
from dbmodel.entity import *

class StatAcompanhanteDia(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@Int(fk=True, precision = 10, scale=0)
	def id_mes(self): pass

	@Int(precision = 10, scale=0)
	def stat_dia(self): pass

	@Int(not_null=True, precision = 10, scale=0)
	def stat_acessos_unicos(self): pass

	@Int(not_null=True, precision = 10, scale=0)
	def stat_acessos_totais(self): pass

	@Int(precision = 10, scale=0)
	def stat_ano(self): pass

	@Int(precision = 10, scale=0)
	def stat_mes(self): pass

	@Int(precision = 10, scale=0)
	def id_acompanhante(self): pass

	# One-to-One

	@Object(name="StatAcompanhanteMe", key="id", reference="id_mes")
	def stat_acompanhante_mes(self):pass

	# One-to-many

	@ObjectList(name="StatAcompanhanteDiaTrafego", key="id_dia", reference="id")
	def stat_acompanhante_dia_trafego(self):pass