#-*- coding: utf-8 -*-
from dbmodel.entity import *

class Regiao(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_estado(self): pass

	@String(max=100)
	def reg_nome(self): pass

	@String(max=65535)
	def reg_texto(self): pass

	@Int(precision = 3, scale=0)
	def reg_ativo(self): pass

	@Int(precision = 10, scale=0)
	def reg_prioridade(self): pass

	@String(max=65535)
	def reg_template_texto(self): pass

	@String(max=100)
	def reg_url(self): pass

	# One-to-One

	@Object(name="Estado", key="id", reference="id_estado", table="estados")
	def estados(self):pass

	# One-to-many

	@ObjectList(name="Acompanhante", key="id_regiao", reference="id", table="acompanhantes")
	def acompanhantes(self):pass

	@ObjectList(name="Cep", key="id_regiao", reference="id", table="ceps")
	def ceps(self):pass

	@ObjectList(name="Cidade", key="id_regiao", reference="id", table="cidades")
	def cidades(self):pass