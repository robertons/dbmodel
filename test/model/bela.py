#-*- coding: utf-8 -*-
from dbmodel.entity import *

class Bela(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_acompanhante(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_estado(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_sexo(self): pass

	@Int(precision = 10, scale=0)
	def bela_semana(self): pass

	@String(max=45)
	def bela_mes(self): pass

	@Int(precision = 10, scale=0)
	def bela_votos(self): pass

	@DateTime()
	def bela_data_apuracao(self): pass

	@Int(precision = 10, scale=0)
	def bela_colocacao(self): pass

	# One-to-One

	@Object(name="Sexo", key="id", reference="id_sexo")
	def sexos(self):pass

	@Object(name="Estado", key="id", reference="id_estado")
	def estados(self):pass

	@Object(name="Acompanhante", key="id", reference="id_acompanhante")
	def acompanhantes(self):pass