#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhantePublicacao(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_acompanhante(self): pass

	@String(not_null=True, max=155)
	def pub_local(self): pass

	@DateTime()
	def pub_data(self): pass

	@String(max=65535)
	def pub_texto(self): pass

	@String(max=155)
	def pub_image(self): pass

	@String(max=155)
	def pub_video(self): pass

	@Int(precision = 10, scale=0)
	def pub_likes(self): pass

	@String(max=45)
	def pub_ip(self): pass

	@Int(precision = 3, scale=0)
	def pub_publicado(self): pass

	@Int(precision = 3, scale=0)
	def pub_moderado(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_cidade(self): pass

	@Int(not_null=True, precision = 3, scale=0)
	def pub_processada(self): pass

	@Int(precision = 3, scale=0)
	def pub_video_expanded(self): pass

	@Int(precision = 3, scale=0)
	def pub_video_auth(self): pass

	@String(max=155)
	def pub_video_original(self): pass

	# One-to-One

	@Object(name="Cidade", key="id", reference="id_cidade")
	def cidades(self):pass

	@Object(name="Acompanhante", key="id", reference="id_acompanhante")
	def acompanhantes(self):pass

	# One-to-many

	@ObjectList(name="AcompanhanteAvaliacao", key="id_acompanhante_publicacao", reference="id")
	def acompanhantes_avaliacoes(self):pass