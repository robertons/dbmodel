#-*- coding: utf-8 -*-
from dbmodel.entity import *

class Perfil(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(not_null=True, max=45)
	def per_nome(self): pass

	@Int(not_null=True, precision = 3, scale=0)
	def per_get(self): pass

	@Int(not_null=True, precision = 3, scale=0)
	def per_post(self): pass

	@Int(not_null=True, precision = 3, scale=0)
	def per_put(self): pass

	@Int(not_null=True, precision = 3, scale=0)
	def per_delete(self): pass

	# One-to-many

	@ObjectList(name="PerfilDepartamento", key="id_perfil", reference="id", table="perfis_departamentos")
	def perfis_departamentos(self):pass

	@ObjectList(name="Usuario", key="id_perfil", reference="id", table="usuarios")
	def usuarios(self):pass