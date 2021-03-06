from django.test import TestCase
from datetime import datetime
from profiles.models import Skill, Profile, WorkExperience, ProjectExperience

class SkillModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Skill.objects.create(skill="Test Skill", category="Test Skill Category")

    ############################################################################################
    # Verbose name tests
    def test_skill_label(self):
        skill_instance = Skill.objects.get(id=1)
        field_label = skill_instance._meta.get_field('skill').verbose_name
        self.assertEqual(field_label, 'skill')

    def test_category_label(self):
        skill_instance = Skill.objects.get(id=1)
        field_label = skill_instance._meta.get_field('category').verbose_name
        self.assertEqual(field_label, 'category')

    ############################################################################################
    # Max length tests
    def test_skill_max_length(self):
        skill_instance = Skill.objects.get(id=1)
        max_length = skill_instance._meta.get_field('skill').max_length
        self.assertEqual(max_length, 50)

    def test_display_name_max_length(self):
        skill_instance = Skill.objects.get(id=1)
        max_length = skill_instance._meta.get_field('category').max_length
        self.assertEqual(max_length, 50)

    ############################################################################################
    # Custom methods tests
    def test__str__(self):
        skill_instance = Skill.objects.get(id=1)
        self.assertEqual(skill_instance.__str__(), skill_instance.skill)


class ProfileModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Profile.objects.create(name="Simon Says", email="simon@says.com", about="Test purposes")

    ############################################################################################
    # Permit null or blank tests
    def test_user_account_null_and_blank_are_true(self):
        profile_instance = Profile.objects.get(id=1)
        null_set_as = profile_instance._meta.get_field('user_account').null
        blank_set_as = profile_instance._meta.get_field('user_account').blank
        self.assertTrue(null_set_as and blank_set_as)

    def test_display_name_blank_is_true(self):
        profile_instance = Profile.objects.get(id=1)
        blank_set_as = profile_instance._meta.get_field('display_name').blank
        self.assertTrue(blank_set_as)

    def test_spoken_languages_blank_is_true(self):
        profile_instance = Profile.objects.get(id=1)
        blank_set_as = profile_instance._meta.get_field('spoken_languages').blank
        self.assertTrue(blank_set_as)

    def test_github_blank_is_true(self):
        profile_instance = Profile.objects.get(id=1)
        blank_set_as = profile_instance._meta.get_field('github').blank
        self.assertTrue(blank_set_as)

    def test_linkedin_blank_is_true(self):
        profile_instance = Profile.objects.get(id=1)
        blank_set_as = profile_instance._meta.get_field('linkedin').blank
        self.assertTrue(blank_set_as)

    ############################################################################################
    # Verbose name tests
    def test_user_account_label(self):
        profile_instance = Profile.objects.get(id=1)
        field_label = profile_instance._meta.get_field('user_account').verbose_name
        self.assertEqual(field_label, 'user account')

    def test_skills_label(self):
        profile_instance = Profile.objects.get(id=1)
        field_label = profile_instance._meta.get_field('skills').verbose_name
        self.assertEqual(field_label, 'skills')

    def test_name_label(self):
        profile_instance = Profile.objects.get(id=1)
        field_label = profile_instance._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_display_name_label(self):
        profile_instance = Profile.objects.get(id=1)
        field_label = profile_instance._meta.get_field('display_name').verbose_name
        self.assertEqual(field_label, 'display name')

    def test_email_label(self):
        profile_instance = Profile.objects.get(id=1)
        field_label = profile_instance._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_about_label(self):
        profile_instance = Profile.objects.get(id=1)
        field_label = profile_instance._meta.get_field('about').verbose_name
        self.assertEqual(field_label, 'about')

    def test_spoken_languages_label(self):
        profile_instance = Profile.objects.get(id=1)
        field_label = profile_instance._meta.get_field('spoken_languages').verbose_name
        self.assertEqual(field_label, 'spoken languages')

    def test_github_label(self):
        profile_instance = Profile.objects.get(id=1)
        field_label = profile_instance._meta.get_field('github').verbose_name
        self.assertEqual(field_label, 'github')

    def test_linkedin_label(self):
        profile_instance = Profile.objects.get(id=1)
        field_label = profile_instance._meta.get_field('linkedin').verbose_name
        self.assertEqual(field_label, 'linkedin')

    ############################################################################################
    # Max length tests
    def test_name_max_length(self):
        profile_instance = Profile.objects.get(id=1)
        max_length = profile_instance._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

    def test_display_name_max_length(self):
        profile_instance = Profile.objects.get(id=1)
        max_length = profile_instance._meta.get_field('display_name').max_length
        self.assertEqual(max_length, 50)

    def test_about_max_length(self):
        profile_instance = Profile.objects.get(id=1)
        max_length = profile_instance._meta.get_field('about').max_length
        self.assertEqual(max_length, 1000)

    def test_spoken_languages_max_length(self):
        profile_instance = Profile.objects.get(id=1)
        max_length = profile_instance._meta.get_field('spoken_languages').max_length
        self.assertEqual(max_length, 200)

    ############################################################################################
    # Custom methods tests
    def test_get_absolute_url(self):
        profile_instance = Profile.objects.get(id=1)
        self.assertEqual(profile_instance.get_absolute_url(), '/about/1')

    def test_display_skills(self):
        profile_instance = Profile.objects.get(id=1)
        Skill.objects.create(skill="Test1", category="Test1")
        Skill.objects.create(skill="Test2", category="Test2")
        profile_instance.skills.add(1)
        profile_instance.skills.add(2)
        self.assertEqual(profile_instance.display_skills(), 'Test1, Test2')

    def test__str__(self):
        profile_instance = Profile.objects.get(id=1)
        self.assertEqual(profile_instance.__str__(), profile_instance.name)


class WorkExperienceModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Profile.objects.create(name="Simon Says", email="simon@says.com", about="Test purposes")
        WorkExperience.objects.create(company="Some company", start_date="2020-01-01",
                                      job_title="Junior - Earliest Start date",
                                      duties="Work hard", profile_id=1)
        WorkExperience.objects.create(company="One more company", start_date="2020-01-03",
                                      job_title="Manager - Latest Start date",
                                      duties="Work hard", profile_id=1)
        WorkExperience.objects.create(company="Another company", start_date="2020-01-02",
                                      job_title="Senior - Middle Start date",
                                      duties="Work hard", profile_id=1)

    ############################################################################################
    # Permit null or blank tests
    def test_end_date_null_and_blank_are_true(self):
        work_experience_instance = WorkExperience.objects.get(id=1)
        null_set_as = work_experience_instance._meta.get_field('end_date').null
        blank_set_as = work_experience_instance._meta.get_field('end_date').blank
        self.assertTrue(null_set_as and blank_set_as)

    def test_company_alias_blank_is_true(self):
        work_experience_instance = WorkExperience.objects.get(id=1)
        blank_set_as = work_experience_instance._meta.get_field('company_alias').blank
        self.assertTrue(blank_set_as)

    ############################################################################################
    # Verbose name tests
    def test_profile_label(self):
        work_experience_instance = WorkExperience.objects.get(id=1)
        field_label = work_experience_instance._meta.get_field('profile').verbose_name
        self.assertEqual(field_label, 'profile')

    def test_company_label(self):
        work_experience_instance = WorkExperience.objects.get(id=1)
        field_label = work_experience_instance._meta.get_field('company').verbose_name
        self.assertEqual(field_label, 'company')

    def test_company_alias_label(self):
        work_experience_instance = WorkExperience.objects.get(id=1)
        field_label = work_experience_instance._meta.get_field('company_alias').verbose_name
        self.assertEqual(field_label, 'company alias')

    def test_start_date_label(self):
        work_experience_instance = WorkExperience.objects.get(id=1)
        field_label = work_experience_instance._meta.get_field('start_date').verbose_name
        self.assertEqual(field_label, 'start date')

    def test_end_date_label(self):
        work_experience_instance = WorkExperience.objects.get(id=1)
        field_label = work_experience_instance._meta.get_field('end_date').verbose_name
        self.assertEqual(field_label, 'end date')

    def test_job_title_label(self):
        work_experience_instance = WorkExperience.objects.get(id=1)
        field_label = work_experience_instance._meta.get_field('job_title').verbose_name
        self.assertEqual(field_label, 'job title')

    def test_duties_label(self):
        work_experience_instance = WorkExperience.objects.get(id=1)
        field_label = work_experience_instance._meta.get_field('duties').verbose_name
        self.assertEqual(field_label, 'duties')

    ############################################################################################
    # Max length tests
    def test_company_max_length(self):
        work_experience_instance = WorkExperience.objects.get(id=1)
        max_length = work_experience_instance._meta.get_field('company').max_length
        self.assertEqual(max_length, 50)

    def test_company_alias_max_length(self):
        work_experience_instance = WorkExperience.objects.get(id=1)
        max_length = work_experience_instance._meta.get_field('company_alias').max_length
        self.assertEqual(max_length, 100)

    def test_job_title_max_length(self):
        work_experience_instance = WorkExperience.objects.get(id=1)
        max_length = work_experience_instance._meta.get_field('job_title').max_length
        self.assertEqual(max_length, 100)

    def test_duties_max_length(self):
        work_experience_instance = WorkExperience.objects.get(id=1)
        max_length = work_experience_instance._meta.get_field('duties').max_length
        self.assertEqual(max_length, 1500)

    ############################################################################################
    # Custom methods tests
    def test_ordering(self):
        work_experience_objects = WorkExperience.objects.all()
        most_recent_work_experience = work_experience_objects[0].start_date
        expected_date = datetime.strptime("2020-01-03", "%Y-%m-%d").date()
        self.assertEqual(most_recent_work_experience, expected_date)

    def test__str__(self):
        work_experience_instance = WorkExperience.objects.get(id=1)
        self.assertEqual(work_experience_instance.__str__(), work_experience_instance.job_title)


class ProjectExperienceModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Profile.objects.create(name="Simon Says", email="simon@says.com", about="Test purposes")

        for i in range(3, 10):
            ProjectExperience.objects.create(project_title=f"{i}project", link=f"www.{i}life.com",
                                          duties="Work hard", profile_id=1, programming_languages=f"{i}All of them")

        ProjectExperience.objects.create(project_title="1project", link=f"www.1life.com",
                                         duties="Work hard", profile_id=1, programming_languages=f"1All of them")

    ###########################################################################################
    # Verbose name tests
    def test_profile_label(self):
        project_experience_instance = ProjectExperience.objects.get(id=1)
        field_label = project_experience_instance._meta.get_field('profile').verbose_name
        self.assertEqual(field_label, 'profile')

    def test_project_title_label(self):
        project_experience_instance = ProjectExperience.objects.get(id=1)
        field_label = project_experience_instance._meta.get_field('project_title').verbose_name
        self.assertEqual(field_label, 'project title')

    def test_duties_label(self):
        project_experience_instance = ProjectExperience.objects.get(id=1)
        field_label = project_experience_instance._meta.get_field('duties').verbose_name
        self.assertEqual(field_label, 'duties')

    def test_programming_languages_label(self):
        project_experience_instance = ProjectExperience.objects.get(id=1)
        field_label = project_experience_instance._meta.get_field('programming_languages').verbose_name
        self.assertEqual(field_label, 'programming languages')

    def test_link_label(self):
        project_experience_instance = ProjectExperience.objects.get(id=1)
        field_label = project_experience_instance._meta.get_field('link').verbose_name
        self.assertEqual(field_label, 'link')

    ############################################################################################
    # Max length tests
    def test_project_title_max_length(self):
        project_experience_instance = ProjectExperience.objects.get(id=1)
        max_length = project_experience_instance._meta.get_field('project_title').max_length
        self.assertEqual(max_length, 100)

    def test_duties_max_length(self):
        project_experience_instance = ProjectExperience.objects.get(id=1)
        max_length = project_experience_instance._meta.get_field('duties').max_length
        self.assertEqual(max_length, 1500)

    def test_programming_languages_max_length(self):
        project_experience_instance = ProjectExperience.objects.get(id=1)
        max_length = project_experience_instance._meta.get_field('programming_languages').max_length
        self.assertEqual(max_length, 200)

############################################################################################
    # Custom methods tests
    def test_ordering(self):
        project_experience_objects = ProjectExperience.objects.all()
        self.assertEqual(project_experience_objects[0].project_title, '1project')
        self.assertEqual(project_experience_objects[1].project_title, '3project')

    def test__str__(self):
        project_experience_instance = ProjectExperience.objects.get(id=1)
        self.assertEqual(project_experience_instance.__str__(), project_experience_instance.project_title)
