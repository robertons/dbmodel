#-*- coding: utf-8 -*-
from dbmodel.entity import *

class Modulo(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_departamento(self): pass

	@String(not_null=True, max=45)
	def mod_nome(self): pass

	@String(max=65535)
	def mod_table(self): pass

	@String(not_null=True, max=45)
	def mod_controller(self): pass

	@String(max=45)
	def mod_icone(self): pass

	# One-to-One

	@Object(name="Departamento", key="id", reference="id_departamento")
	def departamentos(self):pass

	# One-to-many

	@ObjectList(name="UsuarioModulo", key="id_modulo", reference="id")
	def usuarios_modulos(self):pass