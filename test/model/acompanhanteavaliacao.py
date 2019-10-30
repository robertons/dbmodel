#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhanteAvaliacao(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_acompanhante(self): pass

	@DateTime()
	def ava_data(self): pass

	@String(max=45)
	def ava_usuario(self): pass

	@Int(precision = 10, scale=0)
	def ava_likes(self): pass

	@String(max=65535)
	def ava_comentario(self): pass

	@Int(precision = 3, scale=0)
	def ava_aprovado(self): pass

	# One-to-One

	@Object(name="Acompanhante", key="id", reference="id_acompanhante", table="acompanhantes")
	def acompanhantes(self):pass