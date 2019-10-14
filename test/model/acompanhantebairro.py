#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhanteBairro(Entity):

	__primary_key__ = ['id_acompanhante', 'id_bairro', 'id_cidade']

	# FIELDS

	@Int(pk=True, not_null=True, precision = 10, scale=0)
	def id_acompanhante(self): pass

	@Int(pk=True, not_null=True, precision = 10, scale=0)
	def id_bairro(self): pass

	@Int(pk=True, not_null=True, precision = 10, scale=0)
	def id_cidade(self): pass

	# One-to-One

	@Object(name="Acompanhante", key="id", reference="id_acompanhante")
	def acompanhantes(self):pass

	@Object(name="Bairro", key="id", reference="id_bairro")
	def bairros(self):pass

	@Object(name="Cidade", key="id", reference="id_cidade")
	def cidades(self):pass