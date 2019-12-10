from django.db import models
from skills.models import Skill


class Job(models.Model):
    STATES = [
        ('notsent', 'not sent'),
        ('sent', 'Sent'),
        ('interviews', 'Interviews'),
        ('rejected', 'Reject'),
        ('lost', 'Lost'),
    ]

    title = models.CharField(max_length=120)
    pay_amount = models.FloatField()
    description = models.TextField()
    state = models.CharField(max_length=60, choices=STATES, default='notsent')
    #company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    company_id = models.CharField(max_length=60)
    # contact_ids = models.ManyToManyField(Contact)
    contact_ids = models.CharField(max_length=60)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return f"Job: {self.title}@{self.company_id}"


class JobComments(models.Model):

    comment = models.TextField()
    date = models.DateField(auto_now_add=True)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='comments')
    state = models.CharField(max_length=60)

    def save(self, *args, **kwargs):
        if not self.state:
            self.state = self.job_id.state
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.comment}"


