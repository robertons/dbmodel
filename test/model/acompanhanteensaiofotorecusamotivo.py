#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhanteEnsaioFotoRecusaMotivo(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(not_null=True, max=155)
	def rec_motivo(self): pass