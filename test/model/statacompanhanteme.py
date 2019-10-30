#-*- coding: utf-8 -*-
from dbmodel.entity import *

class StatAcompanhanteMe(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_acompanhante(self): pass

	@Int(not_null=True, precision = 10, scale=0)
	def stat_ano(self): pass

	@Int(not_null=True, precision = 10, scale=0)
	def stat_mes(self): pass

	@Int(precision = 10, scale=0)
	def stat_mes_acessos_unicos(self): pass

	@Int(precision = 10, scale=0)
	def stat_mes_acessos_totais(self): pass

	# One-to-One

	@Object(name="Acompanhante", key="id", reference="id_acompanhante", table="acompanhantes")
	def acompanhantes(self):pass

	# One-to-many

	@ObjectList(name="StatAcompanhanteDia", key="id_mes", reference="id", table="stat_acompanhante_dia")
	def stat_acompanhante_dia(self):pass