#-*- coding: utf-8 -*-
from dbmodel.entity import *

class Bairro(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_estado(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_cidade(self): pass

	@String(max=150)
	def bai_nome(self): pass

	@String(max=150)
	def bai_url(self): pass

	@DateTime()
	def bai_data_atualizacao(self): pass

	# One-to-One

	@Object(name="Estado", key="id", reference="id_estado", table="estados")
	def estados(self):pass

	@Object(name="Cidade", key="id", reference="id_cidade", table="cidades")
	def cidades(self):pass

	# One-to-many

	@ObjectList(name="Acompanhante", key="id_bairro", reference="id", table="acompanhantes")
	def acompanhantes(self):pass