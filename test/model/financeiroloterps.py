#-*- coding: utf-8 -*-
from dbmodel.entity import *

class FinanceiroLoteRps(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(max=100)
	def lote_id(self): pass

	@String(max=45)
	def lote_versao(self): pass

	@Int(precision = 10, scale=0)
	def lote_numero(self): pass

	@Int(precision = 19, scale=0)
	def lote_cnpj(self): pass

	@String(max=45)
	def lote_inscricaomunicipal(self): pass

	@Int(precision = 10, scale=0)
	def lote_qtd_rps(self): pass

	@String(max=155)
	def lote_arquivo_xml(self): pass

	@String(max=155)
	def lote_arquivoxls(self): pass

	@DateTime()
	def lote_data(self): pass

	@Decimal(precision = 19, scale=2)
	def lote_total(self): pass

	# One-to-many

	@ObjectList(name="FinanceiroLoteRpsRecibo", key="id_financeiro_lote_rps", reference="id")
	def financeiros_lotes_rps_recibos(self):pass