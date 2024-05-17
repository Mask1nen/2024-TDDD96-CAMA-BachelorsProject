from django.contrib import admin



# Register your models here.
from .camauser import CamaUser
from .study import  Category, Study 
from .country import Country
from .experiment import StudyDesign, RiskOfBias, Grade, ParticipantDesign, Implementation, Experiment
from .effect_data import EffectData, TestTime, EffectSizeType

class CamaUserAdmin(admin.ModelAdmin):
    model = CamaUser
    list_display = ['orc_id', 'name', 'nr_uploads']
    search_fields = ['orc_id']

class StudyAdmin(admin.ModelAdmin):
    model = Study
    list_display = ['study_id', 'uploader', 'study_year', 'country', 'category', 'peer_reviewed', 'authors', 'doi', 'abstract', 'keywords', 'nr_downloads']
    search_fields = ['study_id']

class ExperimentAdmin(admin.ModelAdmin):
    model = Experiment
    list_display = ['study_id', 'experiment_nr', 'study_design', 'risks', 'robins', 'grade', 'participant_design', 'implemented',
                    'intensity_n', 'duration_week', 'frequency_n', 'ni', 'intervention', 'intervention_op',
                    'target_population', 'mean_age', 'source', 'approved']
    search_fields = ['study_id', 'title', 'experiment_nr', 'approved']

class EffectDataAdmin(admin.ModelAdmin):
    model = EffectData
    list_display = ['effect_size_number', 'experiment_nr', 'effect_size_type', 'test_time', 'test_name', 'outcome', 'outcome_full', 'outcome_op', 'gender_1', 'gender_2', 'gender_3', 'd_var',
                    'd', 'f_stat', 't', 'ri', 'icc', 'mean_age_1i', 'mean_age_2i', 'ai', 'bi', 'ci', 'di', 
                    'sd1i', 'sd2i', 'n1i', 'n2i', 'm1i', 'm2i', 'approved']
    search_fields = ['effect_size_number', 'experiment_nr', 'approved']
    
class CountryAdmin(admin.ModelAdmin):
    model = Country
    list_display = ['id', 'name']
    search_fields = ['name']

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['id', 'name']
    search_fields = ['name']

class StudyDesignAdmin(admin.ModelAdmin):
    model = StudyDesign
    list_display = ['design']
    search_fields = ['design']

class RiskOfBiasAdmin(admin.ModelAdmin):
    model = RiskOfBias
    list_display = ['id', 'rob']
    search_fields = ['id']

class GradeAdmin(admin.ModelAdmin):
    model = Grade
    list_display = ["k", "first", "second", "third", "fourth", "fifth", "sixth",
                    "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    search_fields = ["k", "first", "second", "third", "forth", "fifth", "sixth",
                    "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

class ParticipantDesignAdmin(admin.ModelAdmin):
    model = ParticipantDesign
    list_display = ['id', 'design']
    search_fields = ['design']

class ImplementationAdmin(admin.ModelAdmin):
    model = Implementation
    list_display = ['id', 'implementor']
    search_fields = ['implementor']

class TestTimeAdmin(admin.ModelAdmin):
    model = TestTime
    list_display = ['id', 'time']
    search_fields = ['time']

class EffectSizeTypeAdmin(admin.ModelAdmin):
    model = EffectSizeType
    list_display = ['id', 'name']
    search_fields = ['name']

admin.site.register(CamaUser, CamaUserAdmin)
admin.site.register(Study, StudyAdmin)
admin.site.register(Experiment, ExperimentAdmin)
admin.site.register(EffectData, EffectDataAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(StudyDesign, StudyDesignAdmin)
admin.site.register(RiskOfBias, RiskOfBiasAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(ParticipantDesign, ParticipantDesignAdmin)
admin.site.register(Implementation, ImplementationAdmin)
admin.site.register(TestTime, TestTimeAdmin)
admin.site.register(EffectSizeType, EffectSizeTypeAdmin)
