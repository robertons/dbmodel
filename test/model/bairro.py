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

	@Object(name="Cidade", key="id", reference="id_cidade")
	def cidades(self):pass

	@Object(name="Estado", key="id", reference="id_estado")
	def estados(self):pass

	# One-to-many

	@ObjectList(name="Acompanhante", key="id_bairro", reference="id")
	def acompanhantes(self):pass

	@ObjectList(name="AcompanhanteBairro", key="id_bairro", reference="id")
	def acompanhantes_bairros(self):pass