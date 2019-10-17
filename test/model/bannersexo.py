#-*- coding: utf-8 -*-
from dbmodel.entity import *

class BannerSexo(Entity):

	__primary_key__ = ['id_banner', 'id_sexo']

	# FIELDS

	@Int(pk=True, not_null=True, precision = 10, scale=0)
	def id_banner(self): pass

	@Int(pk=True, not_null=True, precision = 10, scale=0)
	def id_sexo(self): pass

	# One-to-One

	@Object(name="Sexo", key="id", reference="id_sexo", table="sexos")
	def sexos(self):pass

	@Object(name="Banner", key="id", reference="id_banner", table="banners")
	def banners(self):pass