#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhanteLog(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(max=45)
	def log_campo(self): pass

	@String(max=65535)
	def log_valor_anterior(self): pass

	@String(max=65535)
	def log_valor_alterado(self): pass

	@DateTime()
	def log_data(self): pass

	@String(max=45)
	def log_ip_usuario(self): pass

	@String(max=65535)
	def log_observacao(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_acompanhante(self): pass

	@Int(fk=True, precision = 10, scale=0)
	def id_usuario(self): pass

	# One-to-One

	@Object(name="Usuario", key="id", reference="id_usuario")
	def usuarios(self):pass

	@Object(name="Acompanhante", key="id", reference="id_acompanhante")
	def acompanhantes(self):pass