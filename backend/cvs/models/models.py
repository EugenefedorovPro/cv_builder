from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


# TODO: manage order - remoce Resume (many - to many filds) - add occupation to every many folded model???
# TODO: link to this cv

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class LanguageChoice(models.Model):
    lang = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.lang

    class Meta:
        db_table = "language_choice"


class OccupationChoice(models.Model):
    occupation = models.CharField(max_length = 100, default = "Backend")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.occupation

    class Meta:
        db_table = "occupation_choice"


class BlockNames(models.Model):
    """
    # _name postfix is reserved for names of big blocks
    _title - for names inside some blocks
    no postfix as in current for other auxiliary fields
    """
    # block names
    photo_name = models.CharField(max_length = 100, blank = True, null = True)
    header_name = models.CharField(max_length = 100, blank = True, null = True)
    hard_skills_name = models.CharField(max_length = 100, blank = True, null = True)
    manifest_name = models.CharField(max_length = 100, blank = True, null = True)
    projects_name = models.CharField(max_length = 100, blank = True, null = True)
    experience_name = models.CharField(max_length = 100, blank = True, null = True)
    soft_skills_name = models.CharField(max_length = 100, blank = True, null = True)
    education_name = models.CharField(max_length = 100, blank = True, null = True)
    natural_lang_name = models.CharField(max_length = 100, blank = True, null = True)
    interest_name = models.CharField(max_length = 100, blank = True, null = True)
    cases_name = models.CharField(max_length = 100, blank = True, null = True)
    why_me_name = models.CharField(max_length = 100, blank = True, null = True)
    feedback_name = models.CharField(max_length = 100, blank = True, null = True)
    # datetime
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # foreign keys
    lang = models.ForeignKey("LanguageChoice", on_delete = models.CASCADE)
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)
    occupation = models.ForeignKey("OccupationChoice", on_delete = models.CASCADE)
    # names within the block
    ## header
    github_title = models.CharField(max_length = 50, blank = True, null = True)
    linkedin_title = models.CharField(max_length = 50, blank = True, null = True)
    country_title = models.CharField(max_length = 50, blank = True, null = True)
    city_title = models.CharField(max_length = 50, blank = True, null = True)
    district_title = models.CharField(max_length = 50, blank = True, null = True)
    ## experience
    company_title = models.CharField(max_length = 50, blank = True, null = True)
    exp_period_title = models.CharField(max_length = 50, blank = True, null = True)
    position_title = models.CharField(max_length = 50, blank = True, null = True)
    achievements_title = models.CharField(max_length = 50, blank = True, null = True)
    ## education
    institution_title = models.CharField(max_length = 50, blank = True, null = True)
    ed_period_title = models.CharField(max_length = 50, blank = True, null = True)
    degree_title = models.CharField(max_length = 50, blank = True, null = True)
    ## natural language
    level_title = models.CharField(max_length = 50, blank = True, null = True)
    ## case
    task_title = models.CharField(max_length = 50, blank = True, null = True)
    solution_title = models.CharField(max_length = 50, blank = True, null = True)
    optimization_title = models.CharField(max_length = 50, blank = True, null = True)
    result_title = models.CharField(max_length = 50, blank = True, null = True)
    tech_stack_title = models.CharField(max_length = 50, blank = True, null = True)
    ## feedback
    contacts_title = models.CharField(max_length = 50, blank = True, null = True)
    # placeholder for no time
    current = models.CharField(max_length = 50, blank = True, null = True)

    def __str__(self):
        return f"{self.lang} - {self.user} - {self.occupation}"


class Photos(models.Model):
    photo_url = models.ImageField(blank = True, null = True, upload_to = "photos/")
    description = models.CharField(max_length = 100, blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)
    lang = models.ForeignKey("LanguageChoice", on_delete = models.CASCADE)
    occupation = models.ForeignKey("OccupationChoice", on_delete = models.CASCADE)

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
    # date time
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    photo = models.ForeignKey("Photos", on_delete = models.CASCADE, blank = True, null = True)
    # foreign keys
    lang = models.ForeignKey("LanguageChoice", on_delete = models.CASCADE)
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)
    occupation = models.ForeignKey("OccupationChoice", on_delete = models.CASCADE)


    def __str__(self):
        return f"{self.first_name} - {self.second_name}"

    class Meta:
        db_table = "header"


class Manifest(models.Model):
    manifest_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    lang = models.ForeignKey("LanguageChoice", on_delete = models.CASCADE)
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)
    occupation = models.ForeignKey("OccupationChoice", on_delete = models.CASCADE)


    def __str__(self):
        return f"Manifest: {self.manifest_text[:50]}..."

    class Meta:
        db_table = "manifest"


class HardSkill(models.Model):
    category = models.CharField(max_length = 50)
    hard_skill_text = models.TextField()
    # date time
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # foreign keys
    lang = models.ForeignKey("LanguageChoice", on_delete = models.CASCADE)
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)
    occupation = models.ForeignKey("OccupationChoice", on_delete = models.CASCADE)

    def __str__(self):
        return f"Hard Skill: {self.user.username} - {self.lang}: {self.hard_skill_text[:15]}..."

    class Meta:
        db_table = "hard_skill"


class Project(models.Model):
    project_name = models.CharField(max_length = 255)
    project_text = models.TextField(max_length = 300)
    web_url = models.URLField(null = True, blank = True)
    git_url = models.URLField(null = True, blank = True)
    # date time
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # foreign keys
    lang = models.ForeignKey("LanguageChoice", on_delete = models.CASCADE)
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)
    occupation = models.ForeignKey("OccupationChoice", on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.project_name} - pk: {self.pk}"

    class Meta:
        db_table = "project"


class Experience(models.Model):
    company = models.CharField(max_length = 255)
    start_date = models.DateField()
    end_date = models.DateField(null = True, blank = True)
    position = models.CharField(max_length = 255)
    achievements = models.TextField(blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    order = models.PositiveIntegerField(default = 0)
    lang = models.ForeignKey("LanguageChoice", on_delete = models.CASCADE)
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)
    occupation = models.ForeignKey("OccupationChoice", on_delete = models.CASCADE)

    def clean(self):
        if self.start_date and self.end_date and self.start_date > self.end_date:
            raise ValidationError("Start date cannot be after end date.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.company} - {self.lang.lang}"

    class Meta:
        db_table = "experience"


class SoftSkill(models.Model):
    soft_skill_text = models.CharField(max_length = 300)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    lang = models.ForeignKey("LanguageChoice", on_delete = models.CASCADE)
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)
    occupation = models.ForeignKey("OccupationChoice", on_delete = models.CASCADE)

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
    lang = models.ForeignKey("LanguageChoice", on_delete = models.CASCADE)
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)
    occupation = models.ForeignKey("OccupationChoice", on_delete = models.CASCADE)

    def clean(self):
        if self.start_date and self.end_date and self.start_date > self.end_date:
            raise ValidationError("Start date cannot be after end date.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.degree_title} at {self.institution}"

    class Meta:
        db_table = "education"


class NaturalLanguage(models.Model):
    natural_lang = models.CharField(max_length = 30, default = 'Ukrainian')
    level = models.CharField(max_length = 30, default = 'fluent')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    lang = models.ForeignKey("LanguageChoice", on_delete = models.CASCADE)
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)
    occupation = models.ForeignKey("OccupationChoice", on_delete = models.CASCADE)


class Interest(models.Model):
    interest_text = models.CharField(max_length = 300)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    lang = models.ForeignKey("LanguageChoice", on_delete = models.CASCADE)
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)
    occupation = models.ForeignKey("OccupationChoice", on_delete = models.CASCADE)

    def __str__(self):
        return f"Interest: {self.interest_text[:50]}..."

    class Meta:
        db_table = "Interest"


class Case(models.Model):
    task = models.TextField()
    solution = models.TextField()
    optimization = models.TextField(blank = True, null = True)
    result = models.TextField(blank = True, null = True)
    tech_stack = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    lang = models.ForeignKey("LanguageChoice", on_delete = models.CASCADE)
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)
    occupation = models.ForeignKey("OccupationChoice", on_delete = models.CASCADE)

    def __str__(self):
        return f"Case: {self.task[:50]}..."

    class Meta:
        db_table = "case"


class WhyMe(models.Model):
    company = models.CharField(max_length = 255)
    why_me_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    lang = models.ForeignKey("LanguageChoice", on_delete = models.CASCADE)
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)
    occupation = models.ForeignKey("OccupationChoice", on_delete = models.CASCADE)

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
    lang = models.ForeignKey("LanguageChoice", on_delete = models.CASCADE)
    user = models.ForeignKey("CustomUser", on_delete = models.CASCADE)
    occupation = models.ForeignKey("OccupationChoice", on_delete = models.CASCADE)

    def __str__(self):
        return f"Feedback: {self.feedback_text[:50]}..."

    class Meta:
        db_table = "feedback"
