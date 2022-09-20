from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.urls import reverse
 
#Custom queryset
class EventsQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active = True)

    def featured(self):
        return self.filter(featured = True, active = True)

class EventsManager(models.Manager):
    
    def get_queryset(self):
        return EventsQuerySet(self.model, using = self._db)
    
    def all(self):
        return self.get_queryset().active()

    def featured(self):
        #return self.get_queryset().filter(featured = True)
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id = id)
        if qs.count() == 1:
            return qs.first()
        return None


# Create your models here.
class Events(models.Model): #event_category
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank = True, unique= True)
    day_event = models.DateField()
    total_enrolled = models.DecimalField(decimal_places=0, max_digits=2, default=50)
    enrolled = models.DecimalField(decimal_places=0, max_digits=2, blank=True, null=True)
    featured = models.BooleanField(default = False)
    active = models.BooleanField(default = True)

    objects = EventsManager()

    def get_absolute_url(self):
        return "/events/{slug}/".format(slug = self.slug)

    #python 3
    def __str__(self):
        return self.title
    #python 2
    def __unicode__(self):
        return self.title
    
def events_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(events_pre_save_receiver, sender = Events)
