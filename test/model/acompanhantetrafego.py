#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhanteTrafego(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_acompanhante(self): pass

	@DateTime()
	def traf_data(self): pass

	@String(max=45)
	def traf_ip(self): pass

	@String(max=150)
	def traf_http_referer(self): pass

	@String(max=45)
	def traf_local_clique(self): pass

	# One-to-One

	@Object(name="Acompanhante", key="id", reference="id_acompanhante", table="acompanhantes")
	def acompanhantes(self):pass