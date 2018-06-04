from django.db import models

MUSIC = "MUS"
MOVIE = "MOV"
CONFERENCE = "CON"
TICKET_TYPES = (
    (MUSIC,'Music'),
    (MOVIE,'Movie'),
    (CONFERENCE,'Conference')
)
# Create your models here.
class Ticket(models.Model):

    enum_type = models.CharField(max_length=3,choices=TICKET_TYPES)
    code = models.CharField(max_length=150,default="")
    title = models.CharField(max_length=150,default="")
    date = models.DateField(auto_now=False)
    startTime = models.TimeField(auto_now=False)
    endTime = models.TimeField(auto_now=False)
    address = models.CharField(max_length=150,blank=True,default="")
    detail = models.TextField(blank=True,null=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)
    url_img = models.URLField(blank=True)
    def __str__(self):  # 0 param method
        return  self.title