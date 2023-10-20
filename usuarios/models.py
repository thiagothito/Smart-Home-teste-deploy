from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome completo")
    email = models.EmailField(unique=True)

    MODELOS_AR_CONDICIONADO = [
        ('modelo1', 'Ar Condicionado Split Hi Wall Inverter LG Dual Voice 9000 BTU/h Frio S4UQ09AA31B.EB2GAMZ - 220 Volts'),
        ('modelo2', 'Ar Condicionado Split 12000 BTUs Midea Frio Springer AirVolution Hi Wall 42TFCA/38TFCA 220V'),
        ('modelo3', 'Ar Condicionado Hi Wall Samsung WindFree Connect Inverter 9.000 Btus Frio 220v'),
        ('modelo4', 'Ar Condicionado Split LG Dual Inverter Voice 12.000 BTU/h Frio Monofásico S4NQ12JA31F.EB1GAMZ – 127 Volts'),
        ('outro', 'Outro modelo'),
        ('sem_ar_condicionado', 'Não possuo ar condicionado em minha residência'),
    ]

    modelo_ar_condicionado = models.CharField(
        max_length=20,
        choices=MODELOS_AR_CONDICIONADO,
        verbose_name="Modelo de ar condicionado presente em sua casa",
    )

    outro_modelo = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Outro",
    )

    MODELOS_BATERIA = [
        ('modelo1', 'Bateria Solar de Lítio 5kWh - Unipower UPLFP48 6000 ciclos'),
        ('modelo2', 'Bateria Estacionária Moura Solar 12MS234 (220Ah)'),
        ('modelo3', 'Bateria Estacionaria Freedom Df4001 240ah Painel Solar'),
        ('modelo4', 'Bateria Estacionaria Freedom Df2500 165ah Nobreak, Solar'),
        ('modelo5', 'Bateria Estacionária Fulguris FGCL150 (150Ah)'),
        ('modelo6', 'Bateria Estacionária Heliar Freedom DF1000 (70Ah / 60Ah)'),
        ('outro', 'Outro modelo'),
        ('sem_bateria', 'Não possuo bateria em minha residência'),
    ]

    modelo_bateria = models.CharField(
        max_length=20,
        choices=MODELOS_BATERIA,
        verbose_name="Modelo de bateria utilizada em sua casa",
    )

    outro_modelo_bateria = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Outro",
    )

    MODELOS_AQUECEDOR = [
        ('modelo1', 'Aquecedor Ventisol Halógeno Ah-01 Preto - 220V'),
        ('modelo2', 'Aquecedor Halogênio Britânia 800W AB800B - 220v'),
        ('modelo3', 'Aquecedor Philco 2000W PAQ2000B - 220v'),
        ('modelo4', 'Aquecedor Quartzo 220V Aq-02 Premium'),
        ('modelo5', 'Aquecedor Domestico Mod A1-02 220V Premium'),
        ('sem_aquecedor', 'Não possuo aquecedor em minha residência'),
        ('outro', 'Outro modelo'),
    ]

    modelo_aquecedor = models.CharField(
        max_length=20,
        choices=MODELOS_AQUECEDOR,
        verbose_name="Selecione o modelo de aquecedor presente em sua casa",
    )

    outro_modelo_aquecedor = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Outro",
    )

    MODELOS_WATER_HEATER = [
        ('modelo1', 'Boiler Solar Baixa Pressão Desnível 200L New Econotec Bivolt Ouro Fino'),
        ('modelo2', 'Boiler Solar Alta Pressão Desnível 400L MKP400 Alumínio e Aço Heliotek'),
        ('modelo3', 'Reservatório Boiller 500 Litros Para Aquecedor Solar Baixa Pressão Nível'),
        ('modelo4', 'Boiler 400 Litros Alta Pressao Aço316 - Soria'),
        ('modelo5', 'Reservatório Térmico(boiler)400l Nivel Fechado 316'),
        ('modelo6', 'Reservatório Térmico (boiler) 800l Fechado 316 - Alta Pressão 220v'),
        ('modelo7', 'Aquecedor Solar Acoplado Ecologic À Vácuo 313L Aço 316 Com 36 Tubos Estrutura Em Alumíni'),
        ('modelo8', 'Aquecedor Solar a Vácuo 150 Litros UNISOL 15 Tubos Aço Inox 316 + Caixa Auxiliar'),
        ('sem_water_heater', 'Não possuo water heater em minha residência'),
        ('outro', 'Outro modelo'),
    ]

    modelo_water_heater = models.CharField(
        max_length=20,
        choices=MODELOS_WATER_HEATER,
        verbose_name="Selecione o modelo de water heater presente em sua casa",
    )

    outro_modelo_water_heater = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Outro",
    )

    MODELOS_CHUVEIRO = [
        ('modelo1', 'Ducha Chuveiro 25x25 Inox Com Braço 40cm Solar Gás Piscina Rose Gold'),
        ('modelo2', 'Chuveiro Loren Shower Eletrônico 7500w 220v~ LORENZETTI Branco'),
        ('modelo3', 'Chuveiro Soft Rubi Square Articulavel'),
        ('modelo4', 'Chuveiro Tradição 127V 5500W, Lorenzetti, 7514205, Cromado, Pequeno'),
        ('modelo5', 'Hydra DPOP.E.772BR, Ducha Eletrônica Optima 7700W, 220V, Branco'),
        ('modelo6', 'Chuveiro Elétrico 7800w 220v Acqua Duo Ultra'),
        ('modelo7', 'Ducha Advanced Turbo Eletrônico 220V 7500W, Lorenzetti, 7510528, Branco, Pequeno'),
        ('modelo8', 'Chuveiro Lorenzetti Acqua Duo Flex Ultra Eletrônico Branco 127v'),
        ('modelo9', 'Chuveiro Eletrônico Digital 220V 8800W Híbrido Prata KDT'),
        ('outro', 'Outro modelo'),
        ('sem_chuveiro', 'Não possuo chuveiro em minha residência'),
    ]

    modelo_chuveiro = models.CharField(
        max_length=20,
        choices=MODELOS_CHUVEIRO,
        verbose_name="Selecione o modelo de chuveiro presente em sua casa",
    )

    outro_modelo_chuveiro = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Outro",
    )

    MODELOS_GELADEIRA = [
        ('modelo1', 'Geladeira Brastemp BRM44HK Frost Free Duplex com Compartimento Extrafrio e Fresh Zone 375L Inox 127v'),
        ('modelo2', 'Geladeira/Refrigerador Frost Free cor Inox 310L Electrolux (TF39S) 220V'),
        ('modelo3', 'Geladeira Consul Frost Free Duplex 386 litros com Altura Flex cor Inox  CRM44AK'),
        ('modelo4', 'Geladeira Brastemp Frost Free Duplex 375L Branca BRM44HB'),
        ('modelo5', 'Geladeira Consul 334L CRD37EB Cycle Defrost com Freezer Supercapacidade Branca'),
        ('modelo6', 'Geladeira Side By Side Eco Inverter Philco 434 Litros Inox PRF533ID - 220V'),
        ('modelo7', 'Geladeira / Refrigerador Consul Frost Free, Duplex, 340L, Prateleiras Altura Flex, Evox - CRM39AK'),
        ('modelo8', 'Geladeira/Refrigerador Frost Free 310 Litros Branco Electrolux (TF39) 220V'),
        ('modelo9', 'Geladeira Consul Frost Free 342 litros cor Inox com Gavetão Hortifruti - CRB39AK'),
        ('modelo10', 'Outro modelo'),
        ('sem_geladeira', 'Não possuo geladeira em minha casa'),
    ]

    modelo_geladeira = models.CharField(
        max_length=20,
        choices=MODELOS_GELADEIRA,
        verbose_name="Selecione o modelo de geladeira presente em sua casa",
    )

    outro_modelo_geladeira = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Outro",
    )

    def __str__(self):
        return "{} ({})".format(self.nome, self.email)
