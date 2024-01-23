from django.db import models
import uuid
# Create your models here.

class CanDetails(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    tc = models.CharField(null=False, unique=True, blank=False, editable=False, max_length=45)
    vc = models.CharField(null=False, blank=False, max_length=45)
    verification_status = models.CharField(null=False, blank=False, max_length=45)
    can_count = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
    lc = models.CharField(null=True,blank=False, max_length=45)
    stc = models.CharField(null=True, blank=False, max_length=45)
    ptc = models.CharField(null=True, blank=False, max_length=45)
    mfg = models.DateTimeField(null=False)
    bb = models.DateTimeField(null=True)
    manufacturing_time = models.DateTimeField(null=True)
    last_updated = models.DateTimeField(null=True)
    image_path = models.CharField(null=True,max_length=45)