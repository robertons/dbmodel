#-*- coding: utf-8 -*-
from dbmodel.entity import *

class Estado(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(max=255)
	def est_nome(self): pass

	@String(max=2)
	def est_sigla(self): pass

	@String(max=45)
	def est_prefixo(self): pass

	@String(max=65535)
	def est_texto(self): pass

	@Int(precision = 10, scale=0)
	def est_prioridade(self): pass

	@String(max=65535)
	def est_principais_cidades(self): pass

	@String(max=100)
	def est_cep_range_1(self): pass

	@String(max=100)
	def est_cep_range_2(self): pass

	@DateTime()
	def est_data_modificacao(self): pass

	@String(max=150)
	def est_geolocalizacao(self): pass

	# One-to-many

	@ObjectList(name="Acompanhante", key="id_estado", reference="id")
	def acompanhantes(self):pass

	@ObjectList(name="AcompanhanteNotificacao", key="id_estado", reference="id")
	def acompanhantes_notificacoes(self):pass

	@ObjectList(name="Bairro", key="id_estado", reference="id")
	def bairros(self):pass

	@ObjectList(name="BannerEstado", key="id_estado", reference="id")
	def banners_estados(self):pass

	@ObjectList(name="Bela", key="id_estado", reference="id")
	def belas(self):pass

	@ObjectList(name="Cep", key="id_estado", reference="id")
	def ceps(self):pass

	@ObjectList(name="Cidade", key="id_estado", reference="id")
	def cidades(self):pass

	@ObjectList(name="Regiao", key="id_estado", reference="id")
	def regioes(self):pass