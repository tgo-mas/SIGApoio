from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ReservaDiaUnico, ReservaSemanal, Local

@receiver(post_save, sender=ReservaDiaUnico)
@receiver(post_save, sender=ReservaSemanal)
def atualizar_reserva(sender, instance, **kwargs):
    local = instance.local
    # Marca o local como reservado
    local.reservado = True
    local.save()
