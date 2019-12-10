from django.test import TestCase
from skills.models import Skill
from jobs.models import Job


class SkillTest(TestCase):
    def setUp(self):
        Skill.objects.create(name='Skill Test')

    def test_skill_create(self):
        skill = Skill.objects.get(name='Skill Test')
        #skill = Skill.objects.all()
        self.assertEqual(skill.name, 'Skill Test')