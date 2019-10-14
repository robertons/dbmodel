#-*- coding: utf-8 -*-
from dbmodel.entity import *

class FinanceiroServico(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(max=45)
	def fin_srv_nome(self): pass

	@String(max=45)
	def fin_srv_codigo_cnae(self): pass

	@String(max=45)
	def fin_srv_codigo_fiscal(self): pass

	@String(max=155)
	def fin_srv_discriminacao(self): pass

	# One-to-many

	@ObjectList(name="AcompanhanteAnuncio", key="id_servico", reference="id")
	def acompanhantes_anuncios(self):pass

	@ObjectList(name="AcompanhanteAnuncioTipo", key="id_servico", reference="id")
	def acompanhantes_anuncios_tipos(self):pass

	@ObjectList(name="AcompanhanteCaseiraAdicional", key="id_servico", reference="id")
	def acompanhantes_caseiras_adicionais(self):pass

	@ObjectList(name="AcompanhanteCaseiraVip", key="id_servico", reference="id")
	def acompanhantes_caseiras_vips(self):pass

	@ObjectList(name="AcompanhanteCompra", key="id_servico", reference="id")
	def acompanhantes_compras(self):pass

	@ObjectList(name="AcompanhanteDestaque", key="id_servico", reference="id")
	def acompanhantes_destaques(self):pass

	@ObjectList(name="AcompanhanteEnsaioEdicao", key="id_servico", reference="id")
	def acompanhantes_ensaios_edicoes(self):pass

	@ObjectList(name="Financeiro", key="id_servico", reference="id")
	def financeiros(self):pass

	@ObjectList(name="FinanceiroServicoValor", key="id_servico", reference="id")
	def financeiros_servicos_valores(self):pass