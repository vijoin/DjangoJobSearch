from django.contrib import admin
from jobs.models import Job, JobComments


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass

@admin.register(JobComments)
class JobCommentsAdmin(admin.ModelAdmin):
    pass