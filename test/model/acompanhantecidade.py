#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhanteCidade(Entity):

	__primary_key__ = ['id_acompanhante', 'id_cidade']

	# FIELDS

	@Int(pk=True, not_null=True, precision = 10, scale=0)
	def id_acompanhante(self): pass

	@Int(pk=True, not_null=True, precision = 10, scale=0)
	def id_cidade(self): pass

	# One-to-One

	@Object(name="Acompanhante", key="id", reference="id_acompanhante", table="acompanhantes")
	def acompanhantes(self):pass

	@Object(name="Cidade", key="id", reference="id_cidade", table="cidades")
	def cidades(self):pass