#-*- coding: utf-8 -*-
from dbmodel.entity import *

class UsuarioDepartamento(Entity):

	__primary_key__ = ['id_usuario', 'id_departamento']

	# FIELDS

	@Int(pk=True, not_null=True, precision = 10, scale=0)
	def id_usuario(self): pass

	@Int(pk=True, not_null=True, precision = 10, scale=0)
	def id_departamento(self): pass

	# One-to-One

	@Object(name="Usuario", key="id", reference="id_usuario")
	def usuarios(self):pass

	@Object(name="Departamento", key="id", reference="id_departamento")
	def departamentos(self):pass