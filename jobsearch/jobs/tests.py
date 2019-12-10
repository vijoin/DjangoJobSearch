from django.test import TestCase
from jobs.models import Job, JobComments

from skills.models import Skill


class JobTestCaste(TestCase):
    def setUp(self):
        job = Job.objects.create(title="Testing Job", pay_amount=500)
        JobComments.objects.create(comment="Testing comment", job_id=job)

    def test_comment_state(self):
        job = Job.objects.get(title="Testing Job")
        comment = JobComments.objects.filter(job_id=job)[0]
        self.assertEqual(comment.state, 'notsent')

    def test_jobs_m2m_skills(self):
        skill = Skill.objects.create(name='Skill Test')
        job = Job.objects.get(title="Testing Job")
        job.skills.add(skill)
        self.assertEqual(job.skills.all()[0].name, 'Skill Test')