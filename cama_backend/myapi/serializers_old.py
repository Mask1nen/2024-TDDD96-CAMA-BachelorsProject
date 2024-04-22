'''class StudySerializer(serializers.ModelSerializer):
    uploader = CamaUserSerializer()
    study_year = YearSerializer()
    country = CountrySerializer()
    category = CategorySerializer()

    class Meta:
        model = Study
        fields = '__all__'

    
    def create(self, validated_data):
        uploader_data = validated_data.pop('uploader')
        study_year_data = validated_data.pop('study_year')
        country_data = validated_data.pop('country')
        category_data = validated_data.pop('category')

        uploader, _ = CamaUser.objects.get_or_create(**uploader_data)
        study_year, _ = Year.objects.get_or_create(**study_year_data)
        country, _ = Country.objects.get_or_create(**country_data)
        category, _ = Category.objects.get_or_create(**category_data)

        study = Study.objects.create(
            uploader=uploader,
            study_year=study_year,
            country=country,
            category=category,
            **validated_data
        )
        return study


    # def get_study_year(self, obj):
    #     return obj.study_year.study_year
'''

'''class ExperimentSerializer(serializers.ModelSerializer):
    study_id = StudySerializer()
    study_design = StudyDesignSerializer()
    risks = RiskOfBiasSerializer()
    grade = GradeSerializer()
    participant_design = ParticipantDesignSerializer()
    implemented = ImplementationSerializer()

    class Meta:
        model = Experiment
        fields = ['gender_2', 'study_design', 'risks','grade','participant_design','implemented','study_id']

    
    def create(self, validated_data):
        study_id = validated_data.pop('study_id')
        study_design_data = validated_data.pop('study_design')
        risks_data = validated_data.pop('risks')
        grade_data = validated_data.pop('grade')
        participant_design_data = validated_data.pop('participant_design')
        implemented_data = validated_data.pop('implemented')

        study_id, _ = Study.objects.get_or_create(**study_id)      
        study_design, _ = StudyDesign.objects.get_or_create(**study_design_data)
        risks, _ = RiskOfBias.objects.get_or_create(**risks_data)
        grade, _ = Grade.objects.get_or_create(**grade_data)
        participant_design, _ = ParticipantDesign.objects.get_or_create(**participant_design_data)
        implemented, _ = Implementation.objects.get_or_create(**implemented_data)

        experiment = Experiment.objects.create(
            study_id=study_id,
            study_design=study_design,
            risks=risks,
            grade=grade,
            participant_design=participant_design,
            implemented=implemented,
            **validated_data
        )
        return experiment
'''  

#EXEMPEL PÅ NESTED RELATIONS
'''from rest_framework import serializers
from .models import Profile,Hobby


class HobbySerializer(serializers.ModelSerializer):

    class Meta:
        model = Hobby
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user_hobby = HobbySerializer(many=True)

    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        user_hobby = validated_data.pop('user_hobby')
        profile_instance = Profile.objects.create(**validated_data)
        for hobby in user_hobby:
            Hobby.objects.create(user=profile_instance,**hobby)
        return profile_instance

    def update(self, instance, validated_data):
        user_hobby_list = validated_data.pop('user_hobby')
        instance.display_name = validated_data.get('display_name', instance.display_name)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.address = validated_data.get('address', instance.address)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.email = validated_data.get('email', instance.email)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()

        hobbies_with_same_profile_instance = Hobby.objects.filter(user=instance.pk).values_list('id', flat=True)

        hobbies_id_pool = []

        for hobby in user_hobby_list:
            if "id" in hobby.keys():
                if Hobby.objects.filter(id=hobby['id']).exists():
                    hobby_instance = Hobby.objects.get(id=hobby['id'])
                    hobby_instance.name = hobby.get('name', hobby_instance.name)
                    hobby_instance.description = hobby.get('description',hobby_instance.description)
                    hobby_instance.save()
                    hobbies_id_pool.append(hobby_instance.id)
                else:
                    continue
            else:
                hobbies_instance = Hobby.objects.create(user=instance, **hobby)
                hobbies_id_pool.append(hobbies_instance.id)

        for hobby_id in hobbies_with_same_profile_instance:
            if hobby_id not in hobbies_id_pool:
                Hobby.objects.filter(pk=hobby_id).delete()

        return instance

    '''