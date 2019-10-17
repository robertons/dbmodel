#-*- coding: utf-8 -*-
from dbmodel.entity import *

class PerfilDepartamento(Entity):

	__primary_key__ = ['id_perfil', 'id_departamento']

	# FIELDS

	@Int(pk=True, not_null=True, precision = 10, scale=0)
	def id_perfil(self): pass

	@Int(pk=True, not_null=True, precision = 10, scale=0)
	def id_departamento(self): pass

	# One-to-One

	@Object(name="Departamento", key="id", reference="id_departamento", table="departamentos")
	def departamentos(self):pass

	@Object(name="Perfil", key="id", reference="id_perfil", table="perfis")
	def perfis(self):pass