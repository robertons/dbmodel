#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhantePublicacao(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_acompanhante(self): pass

	@String(not_null=True, max=155)
	def pub_local(self): pass

	@DateTime()
	def pub_data(self): pass

	@String(max=65535)
	def pub_texto(self): pass

	@String(max=155)
	def pub_image(self): pass

	@Int(precision = 10, scale=0)
	def pub_likes(self): pass

	@String(max=45)
	def pub_ip(self): pass

	@Int(precision = 3, scale=0)
	def pub_publicado(self): pass

	# One-to-One

	@Object(name="Acompanhante", key="id", reference="id_acompanhante", table="acompanhantes")
	def acompanhantes(self):pass