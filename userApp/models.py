from django.db import models
from django.contrib.auth.models import AbstractUser
from conferenceApp.models import Conference
from django.core.validators import ValidationError, MaxValueValidator,FileExtensionValidator, MinValueValidator, EmailValidator, RegexValidator
import re, datetime

# Create your models here.
def validate_cin(value):
    if not re.match(r'^\d{8}$', value):
        raise ValidationError('Invalid Cin')
# Create your models here.
def validate_email(value):
    if not value.endswith('@esprit.tn'):
        raise ValidationError('Invalid Email')

# Create your models here.
class Participant(AbstractUser):
    email = models.EmailField(unique=True, max_length=255, validators=[EmailValidator, validate_email])
    cin = models.CharField(primary_key=True, max_length=8, validators=[validate_cin, RegexValidator('[0-9]{8}$','Invalid Cin')])
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=250, unique=True)
    USERNAME_FIELD = 'username'
    CHOIX= (
        ('ETUDIANT', 'ETUDIANT'),
        ('CHERCHEUR', 'CHERCHEUR'),
        ('ENSEIGNANT', 'ENSEIGNANT'),
        ('DOCTEUR', 'DOCTEUR')
    )
    participant_category = models.CharField('Category', choices=CHOIX, max_length=255)
    reservations = models.ManyToManyField(Conference, through='Reservation', related_name='reservations')
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Participant'

class Reservation(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField()
    confirmed = models.BooleanField(default=False)
    def clean(self):
        if self.conference.start_date < self.reservation_date:
            raise ValidationError('Only reservations on upcoming conferences')
    class Meta:
        verbose_name_plural = 'Reservations'
        unique_together = ('participant', 'conference')
    