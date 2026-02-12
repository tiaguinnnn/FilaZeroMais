from django.core.management.base import BaseCommand
from core_app.models import UnidadeSaude 

class Command(BaseCommand):
    help = 'Popula o banco com unidades realistas'

    def handle(self, *args, **kwargs):
        unidades = [
            {'nome': 'UBS Central Vila Maria', 'endereco': 'Rua das Flores, 123', 'espera': 12},
            {'nome': 'Hospital Municipal de Urgências', 'endereco': 'Av. dos Estados, 500', 'espera': 45},
            {'nome': 'UPA 24h Leste', 'endereco': 'Rua da Esperança, s/n', 'espera': 8},
            {'nome': 'Posto de Saúde Jardim Norte', 'endereco': 'Praça da Matriz, 10', 'espera': 3},
        ]

        self.stdout.write('🌱 Semeando unidades de saúde...')

        for dados in unidades:
            # AJUSTADO: Usando 'pacientes_em_espera' conforme seu models.py
            unidade, created = UnidadeSaude.objects.get_or_create(
                nome=dados['nome'],
                defaults={
                    'endereco': dados['endereco'], 
                    'pacientes_em_espera': dados['espera'] 
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✅ Criada: {unidade.nome}'))

        self.stdout.write(self.style.SUCCESS('🚀 Fomento concluído! Agora dê F5 no site.'))