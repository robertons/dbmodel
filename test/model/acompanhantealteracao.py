#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhanteAlteracao(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(max=45)
	def alt_cod_validacao(self): pass

	@String(max=45)
	def alt_campo(self): pass

	@String(max=65535)
	def alt_valor(self): pass

	@String(max=65535)
	def alt_valor_anterior(self): pass

	@String(max=100)
	def alt_motivo_recusa(self): pass

	@Int(precision = 3, scale=0)
	def alt_validado(self): pass

	@Int(precision = 3, scale=0)
	def alt_pendente(self): pass

	@Int(precision = 3, scale=0)
	def alt_realizado(self): pass

	@Int(precision = 3, scale=0)
	def alt_visualizado(self): pass

	@DateTime()
	def alt_data(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_acompanhante(self): pass

	# One-to-One

	@Object(name="Acompanhante", key="id", reference="id_acompanhante", table="acompanhantes")
	def acompanhantes(self):pass