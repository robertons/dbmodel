#-*- coding: utf-8 -*-
from dbmodel.entity import *

class Sexo(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(max=45)
	def sexo_nome(self): pass

	@String(max=45)
	def sexo_menu(self): pass

	@String(max=45)
	def sexo_menu_singular(self): pass

	@String(max=45)
	def sexo_titulo_singular(self): pass

	@String(max=45)
	def sexo_titulo_plural(self): pass

	@String(max=45)
	def sexo_titulo_alternativo_singular(self): pass

	@String(max=45)
	def sexo_titulo_alternativo_plural(self): pass

	@String(max=45)
	def sexo_url(self): pass

	@String(max=45)
	def sexo_url_singular(self): pass

	@Int(precision = 3, scale=0)
	def sexo_disponivel(self): pass

	@String(max=45)
	def sexo_url_alternativo_singular(self): pass

	@String(max=45)
	def sexo_url_alternativo_plural(self): pass

	# One-to-many

	@ObjectList(name="Acompanhante", key="id_sexo", reference="id", table="acompanhantes")
	def acompanhantes(self):pass

	@ObjectList(name="BannerSexo", key="id_sexo", reference="id", table="banners_sexos")
	def banners_sexos(self):pass

	@ObjectList(name="Bela", key="id_sexo", reference="id", table="belas")
	def belas(self):pass