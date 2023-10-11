from django.db.models.signals import post_save
from django.dispatch import receiver
from series.models.series_relations import SerieRelation


@receiver(post_save, sender=SerieRelation)
def create_reverse_relation(sender, instance, created, **kwargs):
    if created and instance.relation in ['Secuela', 'Precuela']:
        queryset = SerieRelation.objects.filter(referenced=instance.main)
        if instance.relation == 'Secuela' and queryset.filter(relation='Precuela').count() == 0:
            SerieRelation.objects.create(
                main=instance.referenced,
                referenced=instance.main,
                relation='Precuela'
            )

        elif instance.relation == 'Precuela' and queryset.filter(relation='Secuela').count() == 0:
            SerieRelation.objects.create(
                main=instance.referenced,
                referenced=instance.main,
                relation='Secuela'
            )

