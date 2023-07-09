from datacenter.models import Passcard, Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from django.utils import timezone
from datacenter.models import format_duration
import locale


def storage_information_view(request):
    locale.setlocale(locale.LC_ALL, 'ru_RU')
    localtime(timezone.now())
    visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits, non_closed_names = [], []
    for visit in visits:
        for passcard in Passcard.objects.filter(is_active=True):
            if passcard.owner_name in str(visit.passcard):
                non_closed_names.append(passcard.owner_name)
    for num, visit in enumerate(visits):
        non_closed_visits.append(dict({'who_entered': non_closed_names[num]}, **{'entered_at': localtime(visit.entered_at)}, **{'duration':  format_duration(visit.get_duration())}, **{'is_strange': visit.is_visit_long}))
    context = {'non_closed_visits': non_closed_visits, }
    return render(request, 'storage_information.html', context)
