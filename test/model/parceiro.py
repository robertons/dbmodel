#-*- coding: utf-8 -*-
from dbmodel.entity import *

class Parceiro(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(max=255)
	def par_url(self): pass

	@String(max=255)
	def par_url_link(self): pass

	@String(max=255)
	def par_our_link(self): pass

	@String(max=45)
	def par_link_rel(self): pass

	@Int(precision = 10, scale=0)
	def par_da(self): pass

	@Int(precision = 10, scale=0)
	def par_pa(self): pass

	@Int(precision = 10, scale=0)
	def par_domain_links(self): pass

	@Int(precision = 10, scale=0)
	def par_domain_external_links(self): pass

	@DateTime()
	def par_last_moz_crawled(self): pass

	@DateTime()
	def par_last_idp_crawled(self): pass

	@Int(precision = 3, scale=0)
	def par_verified(self): pass

	@String(max=45)
	def par_title(self): pass

	@String(max=255)
	def par_description(self): pass

	@String(max=255)
	def par_icon(self): pass

	@String(max=45)
	def par_categoria(self): pass

	@Int(precision = 3, scale=0)
	def par_verify(self): pass

	@Int(precision = 3, scale=0)
	def par_show(self): pass