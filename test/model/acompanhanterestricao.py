#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhanteRestricao(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@DateTime()
	def rest_data(self): pass

	@String(max=65535)
	def rest_motivo(self): pass

	@Int(precision = 3, scale=0)
	def rest_pendente(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_acompanhante(self): pass

	# One-to-One

	@Object(name="Acompanhante", key="id", reference="id_acompanhante", table="acompanhantes")
	def acompanhantes(self):pass