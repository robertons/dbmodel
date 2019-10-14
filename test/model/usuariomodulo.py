#-*- coding: utf-8 -*-
from dbmodel.entity import *

class UsuarioModulo(Entity):

	__primary_key__ = ['id_usuario', 'id_modulo']

	# FIELDS

	@Int(pk=True, not_null=True, precision = 10, scale=0)
	def id_usuario(self): pass

	@Int(pk=True, not_null=True, precision = 10, scale=0)
	def id_modulo(self): pass

	# One-to-One

	@Object(name="Modulo", key="id", reference="id_modulo")
	def modulos(self):pass

	@Object(name="Usuario", key="id", reference="id_usuario")
	def usuarios(self):pass