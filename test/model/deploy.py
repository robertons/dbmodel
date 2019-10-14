#-*- coding: utf-8 -*-
from dbmodel.entity import *

class Deploy(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(max=100)
	def deploy_url(self): pass

	@DateTime()
	def deploy_data(self): pass

	@Int(precision = 3, scale=0)
	def deploy_realizado(self): pass

	@DateTime()
	def deploy_data_realizacao(self): pass