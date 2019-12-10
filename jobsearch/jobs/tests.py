from django.test import TestCase
from jobs.models import Job, JobComments


class JobTestCaste(TestCase):
    def setUp(self):
        job = Job.objects.create(title="Testing Job", pay_amount=500)
        JobComments.objects.create(comment="Testing comment", job_id=job)

    def test_comment_state(self):
        job = Job.objects.get(title="Testing Job")
        comment = JobComments.objects.filter(job_id=job)[0]
        self.assertEqual(comment.state, 'notsent')
