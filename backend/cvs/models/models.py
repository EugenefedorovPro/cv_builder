from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class BlockNames(models.Model):
    header_name = models.CharField(max_length = 100, default = "Header")
    hard_skills_name = models.CharField(max_length = 100, default = "Hard Skills")
    manifest_name = models.CharField(max_length = 100, default = "Manifest")
    projects_name = models.CharField(max_length = 100, default = "Projects")
    experience_name = models.CharField(max_length = 100, default = "Experience")
    soft_skills_name = models.CharField(max_length = 100, default = "Soft Skills")
    education_name = models.CharField(max_length = 100, default = "Education")
    hobby_name = models.CharField(max_length = 100, default = "Hobby")
    cases_name = models.CharField(max_length = 100, default = "Cases")
    why_me_name = models.CharField(max_length = 100, default = "Why me?")
    lang = models.ForeignKey("LanguageChoice", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)



class Photos(models.Model):
    photo_url = models.ImageField(blank = True, null = True, upload_to = "photos/")
    description = models.CharField(max_length = 100, blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)

    def __str__(self):
        return f"Photo '{self.description}' by {self.user.username}"

    class Meta:
        db_table = "photos"

class Header(models.Model):
    phone = models.CharField(max_length = 50)
    first_name = models.CharField(max_length = 255)
    second_name = models.CharField(max_length = 255)
    email = models.EmailField()
    linkedin = models.URLField(blank = True, null = True)
    github = models.URLField(blank = True, null = True)
    country = models.CharField(max_length = 100, blank = True, null = True)
    city = models.CharField(max_length = 100, blank = True, null = True)
    district = models.CharField(max_length = 100, blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    photo = models.ForeignKey("Photos", on_delete = models.CASCADE, blank = True, null = True)
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)
    lang = models.ForeignKey("LanguageChoice", on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.first_name} - {self.second_name}"

    class Meta:
        db_table = "header"


class HardSkill(models.Model):
    block_name = models.ForeignKey("BlockNames", on_delete = models.CASCADE)
    category = models.CharField(max_length = 50)
    hard_skill_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    resume = models.ManyToManyField("Resume", through = "HardSkillResume")
    lang = models.ForeignKey("LanguageChoice", on_delete = models.CASCADE)
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)

    def clean(self):
        if self.block_name.lang != self.lang:
            raise ValidationError("Languages do not correspond in HardSkill and BlockName instances")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Hard Skill: {self.user.username} - {self.lang}: {self.hard_skill_text[:15]}..."

    class Meta:
        db_table = "hard_skill"


class Manifest(models.Model):
    manifest_text = models.TextField()
    lang = models.ForeignKey("LanguageChoice", on_delete = models.CASCADE)
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)


    def __str__(self):
        return f"Manifest: {self.manifest_text[:50]}..."

    class Meta:
        db_table = "manifest"


class Project(models.Model):
    project_name = models.CharField(max_length = 255)
    project_text = models.TextField(max_length = 300)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    resume = models.ManyToManyField("Resume", through = "ProjectResume")
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)

    def __str__(self):
        return self.project_name

    class Meta:
        db_table = "project"


class Experience(models.Model):
    company = models.CharField(max_length = 255)
    start_date = models.DateField()
    end_date = models.DateField()
    job_title = models.CharField(max_length = 255)
    achievements = models.TextField(blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    resume = models.ManyToManyField("Resume", through = "ExperienceResume")
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)

    def clean(self):
        if self.start_date and self.end_date and self.start_date > self.end_date:
            raise ValidationError("Start date cannot be after end date.")

    def __str__(self):
        return f"{self.job_title} at {self.company}"

    class Meta:
        db_table = "experience"


class SoftSkill(models.Model):
    soft_skill_text = models.CharField(max_length = 300)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    resume = models.ManyToManyField("Resume", through = "SoftSkillResume")
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)

    def __str__(self):
        return f"Soft Skill: {self.soft_skill_text[:50]}..."

    class Meta:
        db_table = "soft_skill"


class Education(models.Model):
    institution = models.CharField(max_length = 255)
    start_date = models.DateField()
    end_date = models.DateField()
    degree_title = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    resume = models.ManyToManyField("Resume", through = "EducationResume")
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)

    def clean(self):
        if self.start_date and self.end_date and self.start_date > self.end_date:
            raise ValidationError("Start date cannot be after end date.")

    def __str__(self):
        return f"{self.degree_title} at {self.institution}"

    class Meta:
        db_table = "education"


class Hobby(models.Model):
    hobby_text = models.CharField(max_length = 300)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    resume = models.ManyToManyField("Resume", through = "HobbyResume")
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)

    def __str__(self):
        return f"Hobby: {self.hobby_text[:50]}..."

    class Meta:
        db_table = "hobby"


class Case(models.Model):
    task = models.TextField()
    solution = models.TextField()
    optimization = models.TextField(blank = True, null = True)
    result = models.TextField(blank = True, null = True)
    tech_stack = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    resume = models.ManyToManyField("Resume", through = "CaseResume")
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)

    def __str__(self):
        return f"Case: {self.task[:50]}..."

    class Meta:
        db_table = "case"


class WhyMe(models.Model):
    company = models.CharField(max_length = 255)
    why_me_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)

    def __str__(self):
        return f"WhyMe for {self.company or 'Unknown Company'}"

    class Meta:
        db_table = "why_me"


class Feedback(models.Model):
    company = models.CharField(max_length = 255)
    feedback_text = models.CharField(max_length = 10_000)
    contacts = models.CharField(max_length = 255, blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    resume = models.ForeignKey("Resume", on_delete = models.CASCADE)

    def __str__(self):
        return f"Feedback: {self.feedback_text[:50]}..."

    class Meta:
        db_table = "feedback"


class LanguageChoice(models.Model):
    lang = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.lang

    class Meta:
        db_table = "language_choice"


class SizeChoice(models.Model):
    code = models.CharField(max_length = 50, unique = True)
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "size_choice"


class OccupationChoice(models.Model):
    code = models.CharField(max_length = 100, unique = True)
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "occupation_choice"


class HardSkillResume(models.Model):
    hard_skill_id = models.ForeignKey("HardSkill", on_delete = models.CASCADE)
    resume_id = models.ForeignKey("Resume", on_delete = models.CASCADE)
    order = models.PositiveIntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "hard_skill_resume"


class SoftSkillResume(models.Model):
    soft_skill_id = models.ForeignKey("SoftSkill", on_delete = models.CASCADE)
    resume_id = models.ForeignKey("Resume", on_delete = models.CASCADE)
    order = models.PositiveIntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "soft_skill_resume"


class CaseResume(models.Model):
    case_id = models.ForeignKey("Case", on_delete = models.CASCADE)
    resume_id = models.ForeignKey("Resume", on_delete = models.CASCADE)
    order = models.PositiveIntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "case_resume"


class ProjectResume(models.Model):
    project_id = models.ForeignKey("Project", on_delete = models.CASCADE)
    resume_id = models.ForeignKey("Resume", on_delete = models.CASCADE)
    order = models.PositiveIntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "project_resume"


class ExperienceResume(models.Model):
    experience_id = models.ForeignKey("Experience", on_delete = models.CASCADE)
    resume_id = models.ForeignKey("Resume", on_delete = models.CASCADE)
    order = models.PositiveIntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "experience_resume"


class HobbyResume(models.Model):
    hobby_id = models.ForeignKey("Hobby", on_delete = models.CASCADE)
    resume_id = models.ForeignKey("Resume", on_delete = models.CASCADE)
    order = models.PositiveIntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "hobby_resume"


class EducationResume(models.Model):
    education_id = models.ForeignKey("Education", on_delete = models.CASCADE)
    resume_id = models.ForeignKey("Resume", on_delete = models.CASCADE)
    order = models.PositiveIntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "education_resume"


class Resume(models.Model):
    description = models.CharField(max_length = 255)
    unique_url_tail = models.CharField(max_length = 50, unique = True)

    language = models.ForeignKey('LanguageChoice', on_delete = models.SET_NULL, null = True, blank = True)
    occupation = models.ForeignKey('OccupationChoice', on_delete = models.SET_NULL, null = True, blank = True)
    size = models.ForeignKey('SizeChoice', on_delete = models.SET_NULL, null = True, blank = True)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    header = models.ForeignKey("Header", on_delete = models.CASCADE)
    manifest = models.ForeignKey("Manifest", on_delete = models.CASCADE)
    why_me = models.ForeignKey("WhyMe", on_delete = models.CASCADE)
    is_public = models.BooleanField(default = True)
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.unique_url_tail:
            unique_url_tail = uuid4().hex[:12]
            while unique_url_tail in Resume.objects.values_list("unique_url_tail", flat = True):
                unique_url_tail = uuid4().hex[:12]
            self.unique_url_tail = unique_url_tail
        super().save(*args, **kwargs)

    def __str__(self):
        return self.description

    class Meta:
        db_table = "resume"
