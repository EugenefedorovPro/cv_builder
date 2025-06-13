from django.contrib import admin

from cvs.models.models import (Case,
                               CustomUser,
                               Education,
                               Experience,
                               Feedback,
                               HardSkill,
                               Header,
                               Interest,
                               LanguageChoice,
                               Manifest,
                               OccupationChoice,
                               Photos,
                               Project,
                               SoftSkill,
                               WhyMe,
                               )


admin.site.register(CustomUser)
admin.site.register(Header)
admin.site.register(Photos)
admin.site.register(Manifest)
admin.site.register(HardSkill)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(SoftSkill)
admin.site.register(Education)
admin.site.register(Interest)
admin.site.register(Case)
admin.site.register(WhyMe)
admin.site.register(Feedback)
admin.site.register(LanguageChoice)
admin.site.register(OccupationChoice)
