#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhanteAnuncioTipo(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_servico(self): pass

	@String(not_null=True, max=100)
	def anun_tipo_nome(self): pass

	@String(not_null=True, max=100)
	def anun_tipo_nomeclatura(self): pass

	@Decimal(not_null=True, precision = 19, scale=2)
	def anun_tipo_valor(self): pass

	@Decimal(not_null=True, precision = 19, scale=3)
	def anun_tipo_desconto_exclusividade(self): pass

	@Decimal(not_null=True, precision = 19, scale=2)
	def anun_tipo_valor_foto_adicional(self): pass

	@Decimal(not_null=True, precision = 19, scale=2)
	def anun_tipo_valor_publicacao(self): pass

	@Int(not_null=True, precision = 10, scale=0)
	def anun_tipo_dias_validade(self): pass

	# One-to-One

	@Object(name="FinanceiroServico", key="id", reference="id_servico", table="financeiros_servicos")
	def financeiros_servicos(self):pass

	# One-to-many

	@ObjectList(name="AcompanhanteAnuncio", key="id_tipo_anuncio", reference="id", table="acompanhantes_anuncios")
	def acompanhantes_anuncios(self):pass