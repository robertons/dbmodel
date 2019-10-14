#-*- coding: utf-8 -*-
from dbmodel.entity import *

class TipoCadastro(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(max=45)
	def tipo_cadastro_nome(self): pass

	# One-to-many

	@ObjectList(name="Acompanhante", key="id_tipo_cadastro", reference="id")
	def acompanhantes(self):pass