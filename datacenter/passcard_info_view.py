from datacenter.models import Passcard, Visit, format_duration
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime
from django.utils import timezone


def passcard_info_view(request, passcode):
    localtime(timezone.now())
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        this_passcard_visits.append(dict({'entered_at': localtime(visit.entered_at)}, **{'duration': format_duration(visit.get_duration())}, **{'is_strange': visit.is_visit_long}))

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
