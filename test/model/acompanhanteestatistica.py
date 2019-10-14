#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhanteEstatistica(Entity):

	__primary_key__ = ['stat_ano', 'stat_mes', 'id_acompanhante']

	# FIELDS

	@Int(pk=True, not_null=True, precision = 10, scale=0)
	def stat_ano(self): pass

	@Int(pk=True, not_null=True, precision = 10, scale=0)
	def stat_mes(self): pass

	@Int(pk=True, not_null=True, precision = 10, scale=0)
	def id_acompanhante(self): pass

	@Int(not_null=True, precision = 10, scale=0)
	def stat_acessos_unicos(self): pass

	@Int(not_null=True, precision = 10, scale=0)
	def stat_acessos_totais(self): pass

	# One-to-One

	@Object(name="Acompanhante", key="id", reference="id_acompanhante")
	def acompanhantes(self):pass