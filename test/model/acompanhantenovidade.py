#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhanteNovidade(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@DateTime()
	def nov_data(self): pass

	@String(max=45)
	def nov_atualizacao(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_acompanhante(self): pass

	# One-to-One

	@Object(name="Acompanhante", key="id", reference="id_acompanhante")
	def acompanhantes(self):pass