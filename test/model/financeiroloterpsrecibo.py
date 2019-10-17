#-*- coding: utf-8 -*-
from dbmodel.entity import *

class FinanceiroLoteRpsRecibo(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_financeiro_lote_rps(self): pass

	@String(max=55)
	def rps_id_declaracao_srv(self): pass

	@String(max=55)
	def rps_id(self): pass

	@Int(precision = 10, scale=0)
	def rps_numero(self): pass

	@String(max=45)
	def rps_serie(self): pass

	@Int(precision = 3, scale=0)
	def rps_tipo(self): pass

	@DateTime()
	def rps_competencia(self): pass

	@Int(precision = 3, scale=0)
	def rps_simples_nacional(self): pass

	@Int(precision = 3, scale=0)
	def rps_incentivofiscal(self): pass

	@Int(precision = 19, scale=0)
	def rps_cnpj_prestador(self): pass

	@String(max=45)
	def rps_inscricao_municipal_prestador(self): pass

	@Int(precision = 19, scale=0)
	def rps_tomador_cpf(self): pass

	@String(max=100)
	def rps_tomador_razaosocial(self): pass

	@Int(precision = 19, scale=0)
	def rps_tomador_telefone(self): pass

	@String(max=45)
	def rps_tomador_email(self): pass

	@String(max=125)
	def rps_tomador_endereco(self): pass

	@String(max=10)
	def rps_tomador_endereco_num(self): pass

	@String(max=60)
	def rps_tomador_endereco_bairro(self): pass

	@String(max=8)
	def rps_tomador_cep(self): pass

	@String(max=60)
	def rps_tomador_complemento(self): pass

	@String(max=2)
	def rps_tomador_uf(self): pass

	@String(max=30)
	def rps_tomador_cod_municipio(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_financeiro(self): pass

	@Int(precision = 10, scale=0)
	def rps_servico_iss_retido(self): pass

	@String(max=5)
	def rps_servico_item(self): pass

	@String(max=45)
	def rps_servico_codigo_cnae(self): pass

	@String(max=255)
	def rps_servico_discriminacao(self): pass

	@Int(precision = 10, scale=0)
	def rps_servico_codigo_municipio(self): pass

	@Decimal(precision = 19, scale=2)
	def rps_servico_valor(self): pass

	@Decimal(precision = 19, scale=2)
	def rps_servico_aliquota(self): pass

	@Int(precision = 3, scale=0)
	def rps_servico_exigibilidade_iss(self): pass

	@Int(precision = 10, scale=0)
	def rps_servico_municipio_incidencia(self): pass

	@String(max=45)
	def rps_servico_nf_status(self): pass

	@String(max=255)
	def rps_servico_nf_observacao(self): pass

	# One-to-One

	@Object(name="Financeiro", key="id", reference="id_financeiro", table="financeiros")
	def financeiros(self):pass

	@Object(name="FinanceiroLoteRps", key="id", reference="id_financeiro_lote_rps", table="financeiros_lotes_rps")
	def financeiros_lotes_rps(self):pass