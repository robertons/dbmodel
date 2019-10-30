#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhanteEnsaioFoto(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@Int(precision = 10, scale=0)
	def foto_numero(self): pass

	@Int(precision = 3, scale=0)
	def foto_capa(self): pass

	@Int(precision = 3, scale=0)
	def foto_perfil(self): pass

	@Int(precision = 3, scale=0)
	def foto_destaque(self): pass

	@Int(precision = 3, scale=0)
	def foto_publicada(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_ensaio_acompanhante(self): pass

	@String(max=155)
	def foto_file_name(self): pass

	@String(max=45)
	def foto_file_type(self): pass

	@String(max=255)
	def foto_watermark_position(self): pass

	@String(max=255)
	def foto_capa_crop(self): pass

	@String(max=255)
	def foto_destaque_crop(self): pass

	@String(max=255)
	def foto_perfil_crop(self): pass

	@Int(precision = 3, scale=0)
	def foto_horizontal(self): pass

	@Int(precision = 3, scale=0)
	def foto_nua(self): pass

	# One-to-One

	@Object(name="AcompanhanteEnsaio", key="id", reference="id_ensaio_acompanhante", table="acompanhantes_ensaios")
	def acompanhantes_ensaios(self):pass