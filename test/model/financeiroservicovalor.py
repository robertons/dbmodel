#-*- coding: utf-8 -*-
from dbmodel.entity import *

class FinanceiroServicoValor(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(not_null=True, max=45)
	def fin_srv_nome(self): pass

	@String(not_null=True, max=255)
	def fin_srv_descricao(self): pass

	@Int(not_null=True, precision = 10, scale=0)
	def fin_srv_codigo(self): pass

	@Decimal(not_null=True, precision = 19, scale=2)
	def fin_srv_valor(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_servico(self): pass

	# One-to-One

	@Object(name="FinanceiroServico", key="id", reference="id_servico", table="financeiros_servicos")
	def financeiros_servicos(self):pass