from django.contrib import admin

from cvs.models.models import (Case,
                               CaseResume,
                               CustomUser,
                               Education,
                               EducationResume,
                               Experience,
                               ExperienceResume,
                               Feedback,
                               HardSkill,
                               HardSkillResume,
                               Header,
                               Hobby,
                               HobbyResume,
                               LanguageChoice,
                               Manifest,
                               OccupationChoice,
                               Photos,
                               Project,
                               ProjectResume,
                               SizeChoice,
                               SoftSkill,
                               SoftSkillResume,
                               WhyMe,
                               )


# @admin.register(Header)
# class HeaderAdmin(admin.ModelAdmin):
#     exclude = ("user",)


admin.site.register(CustomUser)
admin.site.register(Header)
admin.site.register(Photos)
admin.site.register(Manifest)
admin.site.register(HardSkill)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(SoftSkill)
admin.site.register(Education)
admin.site.register(Hobby)
admin.site.register(Case)
admin.site.register(WhyMe)
admin.site.register(Feedback)
admin.site.register(LanguageChoice)
admin.site.register(SizeChoice)
admin.site.register(OccupationChoice)
admin.site.register(HardSkillResume)
admin.site.register(SoftSkillResume)
admin.site.register(CaseResume)
admin.site.register(ProjectResume)
admin.site.register(ExperienceResume)
admin.site.register(HobbyResume)
admin.site.register(EducationResume)
