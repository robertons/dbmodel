#-*- coding: utf-8 -*-
from dbmodel.entity import *

class Cidade(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_estado(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_regiao(self): pass

	@Int(fk=True, precision = 10, scale=0)
	def id_municipio(self): pass

	@String(not_null=True, max=255)
	def cid_nome(self): pass

	@String(max=255)
	def cid_nome_completo(self): pass

	@Int(not_null=True, precision = 3, scale=0)
	def cid_distrito(self): pass

	@Int(precision = 3, scale=0)
	def cid_principal_regiao(self): pass

	@String(max=255)
	def cid_url(self): pass

	@Decimal(precision = 19, scale=2)
	def cid_desconto(self): pass

	@Int(not_null=True, precision = 10, scale=0)
	def cid_range_start(self): pass

	@Int(not_null=True, precision = 10, scale=0)
	def cid_range_end(self): pass

	@DateTime()
	def cid_data_modificacao(self): pass

	# One-to-One

	@Object(name="Regiao", key="id", reference="id_regiao")
	def regioes(self):pass

	@Object(name="Cidade", key="id", reference="id_municipio")
	def cidades(self):pass

	@Object(name="Estado", key="id", reference="id_estado")
	def estados(self):pass

	# One-to-many

	@ObjectList(name="Acompanhante", key="id_cidade", reference="id")
	def acompanhantes(self):pass

	@ObjectList(name="AcompanhanteBairro", key="id_cidade", reference="id")
	def acompanhantes_bairros(self):pass

	@ObjectList(name="AcompanhanteCidade", key="id_cidade", reference="id")
	def acompanhantes_cidades(self):pass

	@ObjectList(name="AcompanhanteNotificacao", key="id_cidade", reference="id")
	def acompanhantes_notificacoes(self):pass

	@ObjectList(name="AcompanhantePublicacao", key="id_cidade", reference="id")
	def acompanhantes_publicacoes(self):pass

	@ObjectList(name="Bairro", key="id_cidade", reference="id")
	def bairros(self):pass

	@ObjectList(name="Cep", key="id_cidade", reference="id")
	def ceps(self):pass

	@ObjectList(name="Cidade", key="id_municipio", reference="id")
	def cidades(self):pass