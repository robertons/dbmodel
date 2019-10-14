#-*- coding: utf-8 -*-
from dbmodel.entity import *

class BannerEstado(Entity):

	__primary_key__ = ['id_banner', 'id_estado']

	# FIELDS

	@Int(pk=True, not_null=True, precision = 10, scale=0)
	def id_banner(self): pass

	@Int(pk=True, not_null=True, precision = 10, scale=0)
	def id_estado(self): pass

	# One-to-One

	@Object(name="Banner", key="id", reference="id_banner")
	def banners(self):pass

	@Object(name="Estado", key="id", reference="id_estado")
	def estados(self):pass