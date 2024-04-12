from django.contrib import admin



# Register your models here.
from .user import User
from .study import Year, Country, Category, Study 
from .experiment import StudyDesign, RiskOfBias, Grade, ParticipantDesign, Implementation, Experiment
from .effect_data import EffectData

class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['orc_id', 'name', 'email', 'organization', 'nr_uploads']
    search_fields = ['orc_id']

class StudyAdmin(admin.ModelAdmin):
    model = Study
    list_display = ['study_id', 'uploader', 'study_year', 'country', 'category', 'peer_reviewed', 'authors', 'doi', 'abstract', 'keywords', 'nr_downloads']
    search_fields = ['study_id']

class ExperimentAdmin(admin.ModelAdmin):
    model = Experiment
    list_display = ['study_id', 'experiment_nr', 'study_design', 'risks', 'grade', 'participant_design', 'implemented', 'gender_1',
                    'gender_2', 'intensity_n', 'duration_week', 'frequency_n', 'outcome', 'outcome_full']
    search_fields = ['study_id', 'experiment_nr']

class EffectDataAdmin(admin.ModelAdmin):
    model = EffectData
    list_display = ['effect_size_number', 'study_id', 'experiment_nr', 'sd1i', 'sd2i', 'n1i', 'n2i', 'm1i', 'm2i', 'd_var',
                    'd', 'f_stat', 't', 'ri', 'mean_age', 'ni', 'icc', 'ai', 'bi', 'ci', 'di']
    search_fields = ['effect_size_number', 'study_id', 'experiment_nr']

class YearAdmin(admin.ModelAdmin):
    model = Year
    list_display = ['study_year']
    search_fields = ['study_year']
    
class CountryAdmin(admin.ModelAdmin):
    model = Country
    list_display = ['name']
    search_fields = ['name']

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['name']
    search_fields = ['name']

class StudyDesignAdmin(admin.ModelAdmin):
    model = StudyDesign
    list_display = ['design']
    search_fields = ['design']

class RiskOfBiasAdmin(admin.ModelAdmin):
    model = RiskOfBias
    list_display = ['id', 'rob', 'robins']
    search_fields = ['id']

class GradeAdmin(admin.ModelAdmin):
    model = Grade
    list_display = ['grade']
    search_fields = ['grade']

class ParticipantDesignAdmin(admin.ModelAdmin):
    model = ParticipantDesign
    list_display = ['design']
    search_fields = ['design']

class ImplementationAdmin(admin.ModelAdmin):
    model = Implementation
    list_display = ['implementor']
    search_fields = ['implementor']

admin.site.register(User, UserAdmin)
admin.site.register(Study, StudyAdmin)
admin.site.register(Experiment, ExperimentAdmin)
admin.site.register(EffectData, EffectDataAdmin)
admin.site.register(Year, YearAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(StudyDesign, StudyDesignAdmin)
admin.site.register(RiskOfBias, RiskOfBiasAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(ParticipantDesign, ParticipantDesignAdmin)
admin.site.register(Implementation, ImplementationAdmin)
