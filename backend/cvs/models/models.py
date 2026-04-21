import uuid

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


class UuidUrl(models.Model):
    uuid_url = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    # foreign keys
    user = models.ForeignKey("CustomUser", on_delete=models.CASCADE)
    occupation = models.ForeignKey("OccupationChoice", on_delete=models.CASCADE)
    # date_time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class LanguageChoice(models.Model):
    # obligatory fields
    lang = models.CharField(max_length=100, default="eng")
    # date time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # foreign keys
    user = models.ForeignKey(
        "CustomUser", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.lang

    class Meta:
        db_table = "language_choice"


class OccupationChoice(models.Model):
    # obligatory fields
    occupation = models.CharField(max_length=100, default="Backend", unique=True)
    # date time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # foreign keys
    user = models.ForeignKey(
        "CustomUser", on_delete=models.CASCADE, null=True, blank=True
    )

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
    photo_name = models.CharField(max_length=100, default="Photo")
    header_name = models.CharField(max_length=100, default="Header")
    hard_skills_name = models.CharField(max_length=100, default="Hard Skills")
    manifest_name = models.CharField(max_length=100, default="Manifest")
    projects_name = models.CharField(max_length=100, default="Projects")
    experience_name = models.CharField(max_length=100, default="Experience")
    soft_skills_name = models.CharField(max_length=100, default="Soft Skills")
    education_name = models.CharField(max_length=100, default="Education")
    natural_lang_name = models.CharField(max_length=100, default="Natural Languages")
    interest_name = models.CharField(max_length=100, default="Interests")
    cases_name = models.CharField(max_length=100, default="Cases")
    why_me_name = models.CharField(max_length=100, default="Why me?")
    feedback_name = models.CharField(max_length=100, default="Feedback")

    # datetime
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # foreign keys
    lang = models.ForeignKey("LanguageChoice", on_delete=models.CASCADE)
    uuid_url = models.ForeignKey(
        "UuidUrl", on_delete=models.CASCADE, null=True, blank=True
    )

    # names within the block
    ## header
    github_title = models.CharField(max_length=50, default="github")
    linkedin_title = models.CharField(max_length=50, default="linkedin")
    country_title = models.CharField(max_length=50, default="Country: ")
    city_title = models.CharField(max_length=50, default="City: ")
    district_title = models.CharField(max_length=50, default="District: ")

    ## experience
    company_title = models.CharField(max_length=50, default="Company")
    exp_period_title = models.CharField(max_length=50, default="Period")
    position_title = models.CharField(max_length=50, default="Position")
    achievements_title = models.CharField(max_length=50, default="Achievements")

    ## education
    institution_title = models.CharField(max_length=50, default="Institution")
    ed_period_title = models.CharField(max_length=50, default="Period")
    degree_title = models.CharField(max_length=50, default="Degree")

    ## natural language
    level_title = models.CharField(max_length=50, default="level: ")

    ## case
    task_title = models.CharField(max_length=50, default="Task")
    solution_title = models.CharField(max_length=50, default="Solution")
    optimization_title = models.CharField(max_length=50, default="Optimization")
    result_title = models.CharField(max_length=50, default="Result")
    tech_stack_title = models.CharField(max_length=50, default="Tech Stack")

    ## feedback
    contacts_title = models.CharField(max_length=50, default="Contacts")

    # placeholder for no time
    current = models.CharField(max_length=50, default="current")

    def __str__(self):
        return f"{self.lang} - {self.uuid_url.user} - {self.uuid_url.occupation.occupation}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["uuid_url", "lang"],
                name="unique_blocknames_per_uuid_and_lang",
            )
        ]


class Photos(models.Model):
    photo_url = models.ImageField(blank=True, null=True, upload_to="photos/")
    description = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # foreign keys
    uuid_url = models.ForeignKey(
        "UuidUrl", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"Photo '{self.description}' by {self.uuid_url.user.username}"

    class Meta:
        db_table = "photos"


class Header(models.Model):
    # obligatory fields
    phone = models.CharField(max_length=50)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    email = models.EmailField()
    # mandatory fields
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    # foreign keys
    photo = models.ForeignKey("Photos", on_delete=models.CASCADE, blank=True, null=True)
    lang = models.ForeignKey("LanguageChoice", on_delete=models.CASCADE)
    uuid_url = models.ForeignKey(
        "UuidUrl", on_delete=models.CASCADE, null=True, blank=True
    )
    # date time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.photo and self.photo.uuid_url_id != self.uuid_url_id:
            raise ValidationError("Photo must belong to the same uuid_url.")

    def __str__(self):
        return f"{self.first_name} - {self.second_name}"

    class Meta:
        db_table = "header"
        constraints = [
            models.UniqueConstraint(
                fields=["uuid_url", "lang"],
                name="unique_header_per_uuid_and_lang",
            )
        ]


class Manifest(models.Model):
    # mandatory fields
    manifest_text = models.TextField()
    # date time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # foreign keys
    lang = models.ForeignKey("LanguageChoice", on_delete=models.CASCADE)
    uuid_url = models.ForeignKey(
        "UuidUrl", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"Manifest: {self.manifest_text[:50]}..."

    class Meta:
        db_table = "manifest"
        constraints = [
            models.UniqueConstraint(
                fields=["uuid_url", "lang"],
                name="unique_manifest_per_uuid_and_lang",
            )
        ]


class HardSkill(models.Model):
    # obligatory fields
    category = models.CharField(max_length=50)
    hard_skill_text = models.TextField()
    # date time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # foreign keys
    lang = models.ForeignKey("LanguageChoice", on_delete=models.CASCADE)
    uuid_url = models.ForeignKey(
        "UuidUrl", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"Hard Skill: {self.uuid_url.user.username} - {self.lang}: {self.hard_skill_text[:15]}..."

    class Meta:
        db_table = "hard_skills"


class Project(models.Model):
    # obligatory fields
    project_name = models.CharField(max_length=255)
    project_text = models.TextField()
    # mandatory fields
    web_url = models.URLField(null=True, blank=True)
    git_url = models.URLField(null=True, blank=True)
    # date time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # foreign keys
    lang = models.ForeignKey("LanguageChoice", on_delete=models.CASCADE)
    uuid_url = models.ForeignKey(
        "UuidUrl", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"{self.project_name} - pk: {self.pk}"

    class Meta:
        db_table = "project"


class Experience(models.Model):
    # obligatory fields
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    order = models.PositiveIntegerField(default=0)
    # mandatory fields
    end_date = models.DateField(null=True, blank=True)
    achievements = models.TextField(blank=True, null=True)
    # date time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # foreign keys
    lang = models.ForeignKey("LanguageChoice", on_delete=models.CASCADE)
    uuid_url = models.ForeignKey(
        "UuidUrl", on_delete=models.CASCADE, null=True, blank=True
    )

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
    # obligatory fields
    soft_skill_text = models.CharField(max_length=300)
    # date time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # foreign keys
    lang = models.ForeignKey("LanguageChoice", on_delete=models.CASCADE)
    uuid_url = models.ForeignKey(
        "UuidUrl", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"Soft Skill: {self.soft_skill_text[:50]}..."

    class Meta:
        db_table = "soft_skills"


class Education(models.Model):
    # obligatory fields
    institution = models.CharField(max_length=255)
    start_date = models.DateField()
    degree_title = models.CharField(max_length=255)
    end_date = models.DateField()
    # date time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # foreign keys
    lang = models.ForeignKey("LanguageChoice", on_delete=models.CASCADE)
    uuid_url = models.ForeignKey(
        "UuidUrl", on_delete=models.CASCADE, null=True, blank=True
    )

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
    # obligatory fields
    natural_lang = models.CharField(max_length=30, default="Ukrainian")
    level = models.CharField(max_length=30, default="fluent")
    # data time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # foreign keys
    lang = models.ForeignKey("LanguageChoice", on_delete=models.CASCADE)
    uuid_url = models.ForeignKey(
        "UuidUrl", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"{self.natural_lang}"

    class Meta:
        db_table = "natural_lang"


class Interest(models.Model):
    # mandatory fields
    interest_text = models.CharField(max_length=300, null=True, blank=True)
    # date time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # foreign keys
    lang = models.ForeignKey("LanguageChoice", on_delete=models.CASCADE)
    uuid_url = models.ForeignKey(
        "UuidUrl", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"Interest: {(self.interest_text or '')[:50]}..."

    class Meta:
        db_table = "interest"


class Case(models.Model):
    # obligatory fields
    task = models.TextField()
    solution = models.TextField()
    tech_stack = models.TextField()
    # mandatory fields
    optimization = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    # date time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # foreign keys
    lang = models.ForeignKey("LanguageChoice", on_delete=models.CASCADE)
    uuid_url = models.ForeignKey(
        "UuidUrl", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"Case: {self.task[:50]}..."

    class Meta:
        db_table = "case"


class WhyMe(models.Model):
    # mandatory fields
    company = models.CharField(max_length=255, null=True, blank=True)
    why_me_text = models.TextField(null=True, blank=True)
    # date time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # foreign keys
    lang = models.ForeignKey("LanguageChoice", on_delete=models.CASCADE)
    uuid_url = models.ForeignKey(
        "UuidUrl", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"WhyMe for {self.company or 'Unknown Company'}"

    class Meta:
        db_table = "why_me"
        constraints = [
            models.UniqueConstraint(
                fields=["uuid_url", "lang"],
                name="unique_why_me_per_uuid_and_lang",
            )
        ]


class Feedback(models.Model):
    # obligatory fields
    company = models.CharField(max_length=255)
    feedback_text = models.TextField()
    # mandatory fields
    contacts = models.CharField(max_length=255, blank=True, null=True)
    # date time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # foreign keys
    lang = models.ForeignKey("LanguageChoice", on_delete=models.CASCADE)
    uuid_url = models.ForeignKey(
        "UuidUrl", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"Feedback: {self.feedback_text[:50]}..."

    class Meta:
        db_table = "feedback"
