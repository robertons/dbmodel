#-*- coding: utf-8 -*-
from dbmodel.entity import *

class TipoFisico(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(max=100)
	def tpf_nome(self): pass

	@String(max=100)
	def tpf_url(self): pass

	# One-to-many

	@ObjectList(name="Acompanhante", key="id_tipo_fisico", reference="id")
	def acompanhantes(self):pass