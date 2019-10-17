#-*- coding: utf-8 -*-
from dbmodel.entity import *

class Log(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@Int(fk=True, precision = 10, scale=0)
	def id_usuario(self): pass

	@String(max=45)
	def log_operacao(self): pass

	@DateTime()
	def log_data(self): pass

	@String(max=45)
	def log_modulo(self): pass

	@String(max=45)
	def log_tabela(self): pass

	@String(max=4294967295)
	def log_registro(self): pass

	@String(max=45)
	def log_ip(self): pass

	# One-to-One

	@Object(name="Usuario", key="id", reference="id_usuario", table="usuarios")
	def usuarios(self):pass