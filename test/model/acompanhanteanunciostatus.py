#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhanteAnuncioStatus(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(not_null=True, max=45)
	def anun_status(self): pass

	# One-to-many

	@ObjectList(name="AcompanhanteAnuncio", key="id_anuncio_status", reference="id", table="acompanhantes_anuncios")
	def acompanhantes_anuncios(self):pass