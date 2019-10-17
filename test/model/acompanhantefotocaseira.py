#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhanteFotoCaseira(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(max=100)
	def foto_caseira_arquivo(self): pass

	@String(max=45)
	def foto_caseira_upload_ip(self): pass

	@DateTime()
	def foto_caseira_upload_data(self): pass

	@Int(precision = 10, scale=0)
	def foto_caseira_crop_x(self): pass

	@Int(precision = 10, scale=0)
	def foto_caseira_crop_y(self): pass

	@Int(precision = 10, scale=0)
	def foto_caseira_width(self): pass

	@Int(precision = 10, scale=0)
	def foto_caseira_heigth(self): pass

	@Decimal(precision = 19, scale=6)
	def foto_caseira_scale(self): pass

	@Int(precision = 10, scale=0)
	def foto_caseira_angle(self): pass

	@String(max=65535)
	def foto_caseira_css_box(self): pass

	@String(max=65535)
	def foto_caseira_css_image(self): pass

	@DateTime()
	def foto_caseira_data_moderacao(self): pass

	@Int(precision = 3, scale=0)
	def foto_caseira_moderada(self): pass

	@Int(precision = 3, scale=0)
	def foto_caseira_aprovada(self): pass

	@Int(precision = 3, scale=0)
	def foto_caseira_capa(self): pass

	@Int(precision = 3, scale=0)
	def foto_caseira_publicada(self): pass

	@Int(precision = 3, scale=0)
	def foto_caseira_excluida(self): pass

	@String(max=255)
	def foto_caseira_motivo_recusa(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_acompanhante(self): pass

	@Int(fk=True, precision = 10, scale=0)
	def id_usuario(self): pass

	# One-to-One

	@Object(name="Usuario", key="id", reference="id_usuario", table="usuarios")
	def usuarios(self):pass

	@Object(name="Acompanhante", key="id", reference="id_acompanhante", table="acompanhantes")
	def acompanhantes(self):pass