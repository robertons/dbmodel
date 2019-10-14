#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhanteAvaliacao(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_acompanhante(self): pass

	@DateTime()
	def ava_data(self): pass

	@String(max=45)
	def ava_usuario(self): pass

	@Int(precision = 10, scale=0)
	def ava_likes(self): pass

	@String(max=65535)
	def ava_comentario(self): pass

	@Int(precision = 3, scale=0)
	def ava_aprovado(self): pass

	@String(max=45)
	def ava_ip(self): pass

	@Int(precision = 3, scale=0)
	def ava_moderado(self): pass

	@Int(precision = 3, scale=0)
	def ava_excluido(self): pass

	@Int(precision = 3, scale=0)
	def ava_resposta_verificada(self): pass

	@Int(fk=True, precision = 10, scale=0)
	def id_acompanhante_avaliacao(self): pass

	@String(precision = 12)
	def ava_ordem_resposta(self): pass

	@Int(fk=True, precision = 10, scale=0)
	def id_acompanhante_publicacao(self): pass

	# One-to-One

	@Object(name="AcompanhanteAvaliacao", key="id", reference="id_acompanhante_avaliacao")
	def acompanhantes_avaliacoes(self):pass

	@Object(name="AcompanhantePublicacao", key="id", reference="id_acompanhante_publicacao")
	def acompanhantes_publicacoes(self):pass

	@Object(name="Acompanhante", key="id", reference="id_acompanhante")
	def acompanhantes(self):pass

	# One-to-many

	@ObjectList(name="AcompanhanteAvaliacao", key="id_acompanhante_avaliacao", reference="id")
	def acompanhantes_avaliacoes(self):pass