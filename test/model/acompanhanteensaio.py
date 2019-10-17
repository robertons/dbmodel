#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhanteEnsaio(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@Int(precision = 10, scale=0)
	def ens_numero(self): pass

	@DateTime()
	def ens_data(self): pass

	@Int(precision = 3, scale=0)
	def ens_publicado(self): pass

	@Int(not_null=True, precision = 10, scale=0)
	def ens_qtd_fotos(self): pass

	@Int(precision = 10, scale=0)
	def ens_qtd_fotos_online(self): pass

	@Int(precision = 3, scale=0)
	def ens_tipo(self): pass

	@String(max=45)
	def ens_video_plataforma(self): pass

	@String(max=255)
	def ens_video_player(self): pass

	@String(max=255)
	def ens_video_link(self): pass

	@String(max=155)
	def ens_video_chave(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_acompanhante(self): pass

	@String(max=45)
	def ens_capa(self): pass

	@String(max=45)
	def ens_destaque(self): pass

	@String(max=45)
	def ens_home(self): pass

	@Int(precision = 10, scale=0)
	def ens_score(self): pass

	@Int(precision = 3, scale=0)
	def ens_aprovado(self): pass

	@Int(precision = 3, scale=0)
	def ens_status(self): pass

	@Int(precision = 3, scale=0)
	def ens_troca_capa(self): pass

	@Int(precision = 3, scale=0)
	def ens_troca_perfil(self): pass

	@Int(precision = 3, scale=0)
	def ens_troca_destaque(self): pass

	# One-to-One

	@Object(name="Acompanhante", key="id", reference="id_acompanhante", table="acompanhantes")
	def acompanhantes(self):pass

	# One-to-many

	@ObjectList(name="AcompanhanteEnsaioEdicao", key="id_ensaio", reference="id", table="acompanhantes_ensaios_edicoes")
	def acompanhantes_ensaios_edicoes(self):pass

	@ObjectList(name="AcompanhanteEnsaioFoto", key="id_ensaio_acompanhante", reference="id", table="acompanhantes_ensaios_fotos")
	def acompanhantes_ensaios_fotos(self):pass