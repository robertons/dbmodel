#-*- coding: utf-8 -*-
from dbmodel.entity import *

class Banner(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(max=45)
	def ban_titulo(self): pass

	@String(max=65535)
	def ban_codigo_fonte(self): pass

	@DateTime()
	def ban_vencimento(self): pass

	@Int(precision = 3, scale=0)
	def ban_ativo(self): pass

	@Int(precision = 3, scale=0)
	def ban_fixo(self): pass

	@String(max=65535)
	def ban_paginas(self): pass

	@String(max=45)
	def ban_prioridade(self): pass

	@Int(precision = 10, scale=0)
	def ban_cliques(self): pass

	@Int(precision = 10, scale=0)
	def ban_impressoes(self): pass

	@String(max=45)
	def ban_local(self): pass

	# One-to-many

	@ObjectList(name="BannerEstado", key="id_banner", reference="id", table="banners_estados")
	def banners_estados(self):pass

	@ObjectList(name="BannerSexo", key="id_banner", reference="id", table="banners_sexos")
	def banners_sexos(self):pass