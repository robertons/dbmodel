#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhanteLogSms(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@DateTime()
	def sms_data_criacao(self): pass

	@DateTime()
	def sms_data_envio(self): pass

	@String(max=255)
	def sms_mensagem(self): pass

	@Int(precision = 19, scale=0)
	def sms_numero_destino(self): pass

	@String(max=45)
	def sms_codigo_confirmacao(self): pass

	@String(not_null=True, max=45)
	def sms_status(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_acompanhante(self): pass

	# One-to-One

	@Object(name="Acompanhante", key="id", reference="id_acompanhante")
	def acompanhantes(self):pass