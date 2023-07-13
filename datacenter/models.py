from django.db import models
import datetime
from django.utils import timezone
from datacenter.format_duration import format_duration


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        if self.leaved_at:
            seconds = self.leaved_at - self.entered_at
        else:
            seconds = datetime.datetime.now(timezone.utc) - self.entered_at
        return seconds.total_seconds()

    def is_visit_long(self, minutes=60):
        delta_minutes = format_duration(self.get_duration()).split(":")
        return int(delta_minutes[0]) * 60 + int(delta_minutes[1]) > minutes
        
