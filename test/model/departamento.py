#-*- coding: utf-8 -*-
from dbmodel.entity import *

class Departamento(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(not_null=True, max=45)
	def dep_nome(self): pass

	@String(max=65535)
	def dep_desc(self): pass

	@String(not_null=True, max=45)
	def dep_controller(self): pass

	@String(max=45)
	def dep_icone(self): pass

	# One-to-many

	@ObjectList(name="Modulo", key="id_departamento", reference="id")
	def modulos(self):pass

	@ObjectList(name="PerfilDepartamento", key="id_departamento", reference="id")
	def perfis_departamentos(self):pass

	@ObjectList(name="UsuarioDepartamento", key="id_departamento", reference="id")
	def usuarios_departamentos(self):pass