from django.db import models


# Create your models here.

class Terminal(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now_add=True, verbose_name="Created At")
    name = models.CharField(max_length=50, null=True, db_index=True)
    is_active = models.BooleanField(db_index=True, default=True)

    def __str__(self):
        return self.name



class Telemetry(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now_add=True, verbose_name="Created At")
    terminal = models.ForeignKey(
        'device.Terminal',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="terminal_telemetry"
    )
    longitude = models.DecimalField(max_digits=20, decimal_places=15)
    latitude = models.DecimalField(max_digits=20, decimal_places=15)

    def __str__(self):
        return f"{self.terminal.name} - {self.created_at}"


