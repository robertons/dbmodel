#-*- coding: utf-8 -*-
from dbmodel.entity import *

class Acompanhante(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(max=155)
	def aco_nome_real(self): pass

	@String(max=11)
	def aco_cpf(self): pass

	@String(max=70)
	def aco_rg(self): pass

	@String(max=10)
	def aco_data_nascimento(self): pass

	@String(max=155)
	def aco_email_pessoal(self): pass

	@String(max=11)
	def aco_celular_pessoal(self): pass

	@String(max=11)
	def aco_telefone_pessoal(self): pass

	@Int(precision = 3, scale=0)
	def aco_atendimento_numero_cadastrado(self): pass

	@String(not_null=True, max=155)
	def aco_nome(self): pass

	@Int(not_null=True, precision = 10, scale=0)
	def aco_idade(self): pass

	@Decimal(not_null=True, precision = 19, scale=2)
	def aco_altura(self): pass

	@Int(not_null=True, precision = 10, scale=0)
	def aco_peso(self): pass

	@Int(precision = 19, scale=0)
	def aco_celular(self): pass

	@Int(precision = 19, scale=0)
	def aco_celular_alternativo(self): pass

	@Int(precision = 19, scale=0)
	def aco_whatsapp(self): pass

	@String(max=50)
	def aco_pele(self): pass

	@String(max=50)
	def aco_cabelo(self): pass

	@String(max=50)
	def aco_olhos(self): pass

	@String(max=50)
	def aco_labios(self): pass

	@String(max=50)
	def aco_coxas(self): pass

	@String(max=50)
	def aco_seios(self): pass

	@String(max=50)
	def aco_atm_quando_uteis(self): pass

	@String(max=50)
	def aco_atm_quando_sabados(self): pass

	@String(max=50)
	def aco_atm_quando_domingos(self): pass

	@String(max=50)
	def aco_atm_quando_feriados(self): pass

	@Int(precision = 3, scale=0)
	def aco_aceita_dinheiro(self): pass

	@Int(precision = 3, scale=0)
	def aco_aceita_cartao_credito(self): pass

	@Int(precision = 3, scale=0)
	def aco_aceita_cartao_debito(self): pass

	@Int(precision = 3, scale=0)
	def aco_aceita_visa(self): pass

	@Int(precision = 3, scale=0)
	def aco_aceita_master(self): pass

	@Int(precision = 3, scale=0)
	def aco_aceita_american(self): pass

	@Int(precision = 3, scale=0)
	def aco_aceita_dinners(self): pass

	@Int(precision = 3, scale=0)
	def aco_atende_homens(self): pass

	@Int(precision = 3, scale=0)
	def aco_atende_mulheres(self): pass

	@Int(precision = 3, scale=0)
	def aco_atende_casais(self): pass

	@Int(precision = 3, scale=0)
	def aco_atende_hoteis(self): pass

	@Int(precision = 3, scale=0)
	def aco_atende_moteis(self): pass

	@Int(precision = 3, scale=0)
	def aco_atende_escritorios(self): pass

	@Int(precision = 3, scale=0)
	def aco_atende_residencias(self): pass

	@Int(precision = 3, scale=0)
	def aco_atende_com_local(self): pass

	@Int(precision = 3, scale=0)
	def aco_atende_viagens(self): pass

	@Int(precision = 3, scale=0)
	def aco_veiculo_proprio(self): pass

	@Int(precision = 3, scale=0)
	def aco_atende_toda_regiao(self): pass

	@Int(precision = 3, scale=0)
	def aco_nao_cobra_deslocamento(self): pass

	@Int(precision = 3, scale=0)
	def aco_nao_negocia_cache(self): pass

	@Int(precision = 3, scale=0)
	def aco_nao_atende_ligacao_restrita(self): pass

	@Int(precision = 3, scale=0)
	def aco_nao_responde_sms(self): pass

	@String(max=65535)
	def aco_texto_chamada(self): pass

	@String(max=65535)
	def aco_texto_livre(self): pass

	@String(max=65535)
	def aco_resumo_anuncio(self): pass

	@String(max=55)
	def aco_titulo_caseirinha(self): pass

	@Int(fk=True, precision = 3, scale=0)
	def aco_publicada(self): pass

	@Int(precision = 3, scale=0)
	def aco_em_breve(self): pass

	@Int(precision = 3, scale=0)
	def aco_em_viagem(self): pass

	@Int(precision = 3, scale=0)
	def aco_exclusiva(self): pass

	@DateTime()
	def aco_sms_lembrete(self): pass

	@String(max=45)
	def aco_senha(self): pass

	@DateTime()
	def aco_data_cadastro(self): pass

	@DateTime()
	def aco_data_acesso_painel(self): pass

	@DateTime()
	def aco_data_atualizacao_sitemap(self): pass

	@Int(precision = 10, scale=0)
	def aco_votos(self): pass

	@Int(precision = 19, scale=0)
	def aco_visitas_totais(self): pass

	@Int(precision = 19, scale=0)
	def aco_visitas_totais_unicas(self): pass

	@Int(precision = 19, scale=0)
	def aco_visitas_mes(self): pass

	@Int(precision = 19, scale=0)
	def aco_visitas_mes_unicas(self): pass

	@Int(precision = 19, scale=0)
	def aco_visitas_dia(self): pass

	@Int(precision = 19, scale=0)
	def aco_visitas_dia_unicas(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_tipo_fisico(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_tipo_cadastro(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_sexo(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_cep(self): pass

	@String(not_null=True, max=255)
	def aco_estado(self): pass

	@String(not_null=True, max=2)
	def aco_uf(self): pass

	@String(not_null=True, max=100)
	def aco_regiao(self): pass

	@String(not_null=True, max=255)
	def aco_cidade(self): pass

	@String(not_null=True, max=100)
	def aco_geolocalizacao(self): pass

	@String(not_null=True, max=155)
	def aco_bairro(self): pass

	@String(max=155)
	def aco_logradouro(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_estado(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_cidade(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_regiao(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_bairro(self): pass

	@DateTime(not_null=True)
	def aco_vencimento(self): pass

	@Int(not_null=True, precision = 10, scale=0)
	def aco_score(self): pass

	# One-to-One

	@Object(name="Bairro", key="id", reference="id_bairro")
	def bairros(self):pass

	@Object(name="Regiao", key="id", reference="id_regiao")
	def regioes(self):pass

	@Object(name="Cep", key="id", reference="id_cep")
	def ceps(self):pass

	@Object(name="Sexo", key="id", reference="id_sexo")
	def sexos(self):pass

	@Object(name="Cidade", key="id", reference="id_cidade")
	def cidades(self):pass

	@Object(name="TipoCadastro", key="id", reference="id_tipo_cadastro")
	def tipos_cadastros(self):pass

	@Object(name="TipoFisico", key="id", reference="id_tipo_fisico")
	def tipos_fisicos(self):pass

	@Object(name="Estado", key="id", reference="id_estado")
	def estados(self):pass

	# One-to-many

	@ObjectList(name="AcompanhanteAlteracao", key="id_acompanhante", reference="id")
	def acompanhantes_alteracoes(self):pass

	@ObjectList(name="AcompanhanteAnuncio", key="id_acompanhante", reference="id")
	def acompanhantes_anuncios(self):pass

	@ObjectList(name="AcompanhanteAtendimento", key="id_acompanhante", reference="id")
	def acompanhantes_atendimentos(self):pass

	@ObjectList(name="AcompanhanteAvaliacao", key="id_acompanhante", reference="id")
	def acompanhantes_avaliacoes(self):pass

	@ObjectList(name="AcompanhanteBairro", key="id_acompanhante", reference="id")
	def acompanhantes_bairros(self):pass

	@ObjectList(name="AcompanhanteCaseiraAdicional", key="id_acompanhante", reference="id")
	def acompanhantes_caseiras_adicionais(self):pass

	@ObjectList(name="AcompanhanteCaseiraOrdem", key="id_acompanhante", reference="id")
	def acompanhantes_caseiras_ordens(self):pass

	@ObjectList(name="AcompanhanteCaseiraVip", key="id_acompanhante", reference="id")
	def acompanhantes_caseiras_vips(self):pass

	@ObjectList(name="AcompanhanteCidade", key="id_acompanhante", reference="id")
	def acompanhantes_cidades(self):pass

	@ObjectList(name="AcompanhanteCompra", key="id_acompanhante", reference="id")
	def acompanhantes_compras(self):pass

	@ObjectList(name="AcompanhanteDestaque", key="id_acompanhante", reference="id")
	def acompanhantes_destaques(self):pass

	@ObjectList(name="AcompanhanteEnsaio", key="id_acompanhante", reference="id")
	def acompanhantes_ensaios(self):pass

	@ObjectList(name="AcompanhanteEnsaioEdicao", key="id_acompanhante", reference="id")
	def acompanhantes_ensaios_edicoes(self):pass

	@ObjectList(name="AcompanhanteEstatistica", key="id_acompanhante", reference="id")
	def acompanhantes_estatisticas(self):pass

	@ObjectList(name="AcompanhanteEstatisticaDia", key="id_acompanhante", reference="id")
	def acompanhantes_estatisticas_dias(self):pass

	@ObjectList(name="AcompanhanteEstatisticaDiaTrafego", key="id_acompanhante", reference="id")
	def acompanhantes_estatisticas_dias_trafegos(self):pass

	@ObjectList(name="AcompanhanteFotoCaseira", key="id_acompanhante", reference="id")
	def acompanhantes_fotos_caseiras(self):pass

	@ObjectList(name="AcompanhanteLog", key="id_acompanhante", reference="id")
	def acompanhantes_logs(self):pass

	@ObjectList(name="AcompanhanteLogSms", key="id_acompanhante", reference="id")
	def acompanhantes_logs_sms(self):pass

	@ObjectList(name="AcompanhanteNotificacao", key="id_acompanhante", reference="id")
	def acompanhantes_notificacoes(self):pass

	@ObjectList(name="AcompanhanteNovidade", key="id_acompanhante", reference="id")
	def acompanhantes_novidades(self):pass

	@ObjectList(name="AcompanhanteOrdemServico", key="id_acompanhante", reference="id")
	def acompanhantes_ordens_servicos(self):pass

	@ObjectList(name="AcompanhantePublicacao", key="id_acompanhante", reference="id")
	def acompanhantes_publicacoes(self):pass

	@ObjectList(name="AcompanhanteRestricao", key="id_acompanhante", reference="id")
	def acompanhantes_restricoes(self):pass

	@ObjectList(name="AcompanhanteTrafego", key="id_acompanhante", reference="id")
	def acompanhantes_trafegos(self):pass

	@ObjectList(name="Bela", key="id_acompanhante", reference="id")
	def belas(self):pass

	@ObjectList(name="Financeiro", key="id_acompanhante", reference="id")
	def financeiros(self):pass