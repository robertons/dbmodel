#-*- coding: utf-8 -*-
from dbmodel.entity import *

class Cep(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_estado(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_regiao(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_cidade(self): pass

	@String(not_null=True, max=11)
	def cep_postal(self): pass

	@String(max=50)
	def cep_tipo(self): pass

	@String(max=100)
	def cep_nome_logradouro(self): pass

	@String(max=100)
	def cep_logradouro(self): pass

	@String(max=100)
	def cep_bairro(self): pass

	@String(not_null=True, max=255)
	def cep_cid_nome(self): pass

	@String(max=45)
	def cep_est_prefixo(self): pass

	@String(not_null=True, max=255)
	def cep_est_nome(self): pass

	@String(not_null=True, max=2)
	def cep_est_sigla(self): pass

	@String(max=100)
	def cep_complemento(self): pass

	@String(max=100)
	def cep_grandes_usuarios(self): pass

	@String(max=100)
	def cep_latitude(self): pass

	@Decimal(not_null=True, precision = 19, scale=13)
	def cep_latitude_decimal(self): pass

	@String(max=100)
	def cep_longitude(self): pass

	@Decimal(not_null=True, precision = 19, scale=13)
	def cep_longitude_decimal(self): pass

	@String(max=20)
	def cep_codigo_ibge_cidade(self): pass

	@String(max=20)
	def cep_area_cidade(self): pass

	@String(max=2)
	def cep_codigo_ddd_cidade(self): pass

	@String(max=20)
	def cep_ativo(self): pass

	@Int(precision = 3, scale=0)
	def cep_cid_distrito(self): pass

	@String(max=65535)
	def cep_est_texto(self): pass

	@String(max=65535)
	def cep_est_principais_cidades(self): pass

	@String(max=255)
	def cep_cid_nome_completo(self): pass

	@Int(precision = 3, scale=0)
	def cep_cid_principal_regiao(self): pass

	@String(max=45)
	def cep_cid_url(self): pass

	@Decimal(precision = 19, scale=2)
	def cep_cid_desconto(self): pass

	@Int(fk=True, precision = 10, scale=0)
	def id_municipio(self): pass

	@String(max=100)
	def cep_reg_nome(self): pass

	@String(max=65535)
	def cep_reg_texto(self): pass

	@Int(precision = 3, scale=0)
	def cep_reg_ativo(self): pass

	@Int(precision = 10, scale=0)
	def cep_reg_prioridade(self): pass

	@String(max=65535)
	def cep_reg_template_texto(self): pass

	@Int(precision = 10, scale=0)
	def id_bairro(self): pass

	# One-to-One

	@Object(name="Regiao", key="id", reference="id_regiao")
	def regioes(self):pass

	@Object(name="Cidade", key="id", reference="id_cidade")
	def cidades(self):pass

	@Object(name="Estado", key="id", reference="id_estado")
	def estados(self):pass

	# One-to-many

	@ObjectList(name="Acompanhante", key="id_cep", reference="id")
	def acompanhantes(self):pass