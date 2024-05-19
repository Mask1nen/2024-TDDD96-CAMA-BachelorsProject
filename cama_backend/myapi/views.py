from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CamaUser, Experiment, Study, EffectData, Country, Category, StudyDesign, RiskOfBias, Grade, ParticipantDesign, Implementation, TestTime, EffectSizeType
from .serializers.cama_user import CamaUserSerializer
from .serializers.study import StudySerializer, StudyCreateSerializer, CountrySerializer, CategorySerializer
from .serializers.experiment import ExperimentSerializer, ExperimentCreateSerializer, StudyDesignSerializer, RiskOfBiasSerializer, GradeSerializer, ParticipantDesignSerializer, ImplementationSerializer
from .serializers.effect_data import EffectDataSerializer, EffectDataCreateSerializer, EffectSizeTypeSerializer, TestTimeSerializer
from django.http import JsonResponse
from django.db.models import Q
import csv
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


import logging
logger = logging.getLogger(__name__)

def filter_helper(parameters, fields):
    """A helper functions which creates a Q filter based on the parameters 
    which are provided.

    Arguments:
        parameters -- The parameters provided in the request.
        fields -- The fields which exists in the table.

    Returns:
        A Q filter containing filters based on the provided parameters.
    """    
    filter_container = Q()
    for key, value in parameters.items():
            # Handles refrences to other tables and thier fields
            if '__' in key:
                related_field, attribute = key.split('__')
                if related_field in fields:
                    filter_condition = {f"{related_field}__{attribute}": value}
                    filter_container &= Q(**filter_condition)
                
            else:
                if key in fields:
                    filter_condition = {f"{key}": value}
                    filter_container &= Q(**filter_condition)
    return filter_container

class FieldsView(APIView):
    """View to list all fields in the `Study`, `Experiment` and `EffectData` tables.
    """
    def get(self, request):
        """Handle GET requests to list all fields of `Study`, `Experiment` and `EffectData`.

        This method retrieves all the fields of the `Study`, `Experiment` and `EffectData` tables 
        and returns them as a JSON response.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing a list of all the fields.
        """
        study_fields = {field.name: {
            'type': field.get_internal_type(),
            'required': not field.blank,
            'help_text': getattr(field, 'help_text', '')
        } for field in Study._meta.fields}

        experiment_fields = {field.name: {
            'type': field.get_internal_type(),
            'required': not field.blank,
            'help_text': getattr(field, 'help_text', '')
        } for field in Experiment._meta.fields}
    
        effect_fields = {field.name: {
            'type': field.get_internal_type(),
            'required': not field.blank,
            'help_text': getattr(field, 'help_text', '')
        } for field in EffectData._meta.fields}

        return JsonResponse({
            'study_fields': study_fields,
            'experiment_fields': experiment_fields,
            'effect_fields': effect_fields
    })

class CamaUserView(APIView):
    """View to list all cama users and create new cama user.
    """ 
    def get(self, request):
        """Handle GET requests to list all cama users.

        This method retrieves all `CamaUser` objects from the database,
        serializes them, and returns them as a JSON response.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing a list of all serialized
                      cama users.
        """
        cama_users = CamaUser.objects.all()
        serializer = CamaUserSerializer(cama_users, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Handle POST requests to create new cama user.

        This method serializes the data from the request to create a new
        `CamaUser` object. If the data is valid, the effect data is saved
        and returned as a JSON response with a 201 Created status. If the data
        is invalid, a 400 Bad Request response is returned with the errors.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing the serialized data of the
                      newly created cama user if successful, or the errors
                      if the data is invalid.
        """
        data = request.data
        # Serialize the data and create a Study instance
        serializer = CamaUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudyView(APIView):
    """View to list all studies and create new studies.

    """    
    def get(self, request):
        """Handle GET requests to list all studies.

        This method retrieves all `Study` objects from the database,
        serializes them, and returns them as a JSON response.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing a list of all serialized
                      studies.
        """
        study = Study.objects.all()
        serializer = StudySerializer(study, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Handle POST requests to create new study.

        This method serializes the data from the request to create a new
        `Study` object. If the data is valid, the effect data is saved
        and returned as a JSON response with a 201 Created status. If the data
        is invalid, a 400 Bad Request response is returned with the errors.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing the serialized data of the
                      newly created study if successful, or the errors
                      if the data is invalid.
        """
        serializer = StudyCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(StudySerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class StudyFilterView(APIView):
    """View to filter and retrieve studies based on query parameters.

    This view handles GET requests to filter the `Study` objects
    based on the provided query parameters. It returns the filtered
    studies as a JSON response.
    """
    def get(self, request):
        """Handle GET requests to filter and retrieve studies.

        This method retrieves all the provided query parameters from
        the request, constructs the necessary filters, and applies
        them to the `Study` model. The filtered studies are then serialized
        and returned as a JSON response.

        Args:
            request: The HTTP request object containing query parameters.

        Returns:
            Response: A JSON response containing the serialized data
                      of the filtered studies.
        """        
        # Get all the provided parameters from the query string
        parameters = request.GET.dict()
        fields = [field.name for field in Study._meta.get_fields()]
        filters = filter_helper(parameters, fields)
        studies = Study.objects.all().filter(filters)
        serializer = StudySerializer(studies, many=True)
        return Response(serializer.data)
    
    
class ExperimentFilterView(APIView):
    """View to filter and retrieve experiments based on query parameters.

    This view handles GET requests to filter the `Experiment` objects
    based on the provided query parameters. It returns the filtered
    experiments as a JSON response.
    """
    def get(self, request):
        """Handle GET requests to filter and retrieve studies.

        This method retrieves all the provided query parameters from
        the request, constructs the necessary filters, and applies
        them to the `Experiment` model. The filtered studies are then serialized
        and returned as a JSON response.

        Args:
            request: The HTTP request object containing query parameters.

        Returns:
            Response: A JSON response containing the serialized data
                      of the filtered studies.
        """
        # Get all the provided parameters from the query string
        parameters = request.GET.dict()
        fields = [field.name for field in Experiment._meta.get_fields()]
        filters = filter_helper(parameters, fields)
        experiments = Experiment.objects.all().filter(filters)
        serializer = ExperimentSerializer(experiments, many=True)
        return Response(serializer.data)
    
class EffectDataFilterView(APIView):
    """View to filter and retrieve experiments based on query parameters.

    This view handles GET requests to filter the `Effect Data` objects
    based on the provided query parameters. It returns the filtered
    effect datas as a JSON response.
    """
    def get(self, request):
        """ Handles get requests whith provided filters in the url

        Arguments:
            request -- the request

        Returns:
            A HTTP response whith the filterd data in json format
        """
        # Get all the provided parameters from the query string
        parameters = request.GET.dict()
        fields = [field.name for field in EffectData._meta.get_fields()]
        filters = filter_helper(parameters, fields)
        effect_data = EffectData.objects.all().filter(filters)
        serializer = EffectDataSerializer(effect_data, many=True)
        return Response(serializer.data)
    
class StudySearchView(APIView):
    """View to search for studies based on title or authors.

    This view handles GET requests to search for `Study` objects
    based on the provided title or author query parameters. It returns
    the matching studies as a JSON response.
    """
    def get(self, request):
        """Handles GET requests to search for studies.

        This method retrieves all the provided query parameters from
        the request, constructs the necessary filters for title or
        authors, and applies them to the `Study` model. The matching
        studies are then serialized and returned as a JSON response.

        Args:
            request: The HTTP request object containing query parameters.

        Returns:
            Response: A JSON response containing the serialized data
                      of the matching studies.
        """      
        parameters = request.GET.dict() # Get all the provided parameters from the query string
        filters = Q() # Create an empty Q object to hold the filters
        for key, value in parameters.items():
            if key == 'title' or key == 'authors':
                filter_condition = {f"{key}__contains": value}
                filters &= Q(**filter_condition)
        studies = Study.objects.all().filter(filters)
        serializer = StudySerializer(studies, many=True)
        return Response(serializer.data)

class StudyDetailView(APIView):
    """View to retrieve a specific study.

    This view handles GET requests to retrieve a `Study` object
    based on its primary key (ID). If the study exists, its details
    are returned as a JSON response. If the study does not exist,
    a 404 Not Found response is returned.
    """
    def get(self, request, id):
        """Handle GET requests to retrieve a study by its ID.

        This method attempts to retrieve a `Study` object using the provided
        primary key (ID). If the study is found, it is serialized and returned
        as a JSON response. If the study is not found, a 404 Not Found response
        is returned.

        Args:
            request: The HTTP request object.
            id (int): The primary key of the `Study` object to be retrieved.

        Returns:
            Response: A JSON response containing the serialized data
                      of the study if found, otherwise a 404 Not Found response.
        """
        try: 
            study = Study.objects.get(pk=id)
            serializer = StudySerializer(study)
            return Response(serializer.data)
        except Study.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ExperimentView(APIView):
    """View to list all experiments and create new experiments.

    This view handles GET requests to list all `Experiment` objects
    and POST requests to create a new `Experiment` object.
    """
    def get(self, request):
        """Handle GET requests to list all experiments.

        This method retrieves all `Experiment` objects from the database,
        serializes them, and returns them as a JSON response.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing a list of all serialized
                      experiments.
        """
        experiments = Experiment.objects.all()
        serializer = ExperimentSerializer(experiments, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Handle POST requests to create a new experiment.

        This method serializes the data from the request to create a new
        `Experiment` object. If the data is valid, the experiment is saved
        and returned as a JSON response with a 201 Created status. If the data
        is invalid, a 400 Bad Request response is returned with the errors.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing the serialized data of the
                      newly created experiment if successful, or the errors
                      if the data is invalid.
        """
        serializer = ExperimentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(ExperimentSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EffectDataView(APIView):
    """View to list all effect data and create new effect data.

    This view handles GET requests to list all `EffectData` objects
    and POST requests to create a new `EffectData` object.
    """
    def get(self, request):
        """Handle GET requests to list all effect data.

        This method retrieves all `EffectData` objects from the database,
        serializes them, and returns them as a JSON response.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing a list of all serialized
                      effect data.
        """
        effect_data = EffectData.objects.all()
        serializer = EffectDataSerializer(effect_data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Handle POST requests to create new effect data.

        This method serializes the data from the request to create a new
        `EffectData` object. If the data is valid, the effect data is saved
        and returned as a JSON response with a 201 Created status. If the data
        is invalid, a 400 Bad Request response is returned with the errors.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing the serialized data of the
                      newly created effect data if successful, or the errors
                      if the data is invalid.
        """
        serializer = EffectDataCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class CountryOptionsView(APIView):
    """View to list all country options and create new country options.

    This view handles GET requests to list all `Country` objects
    and POST requests to create a new `Country` object.
    """
    def get(self, request):
        """Handle GET requests to list all country options.

        This method retrieves all `Country` objects from the database,
        serializes them, and returns them as a JSON response.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing a list of all serialized
                      country options.
        """
        options = Country.objects.all()
        serializer = CountrySerializer(options, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Handle POST requests to create new country options.

        This method serializes the data from the request to create a new
        `Country` object. If the data is valid, the country is saved and
        returned as a JSON response with a 201 Created status. If the data
        is invalid, a 400 Bad Request response is returned with the errors.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing the serialized data of the
                      newly created country option if successful, or the
                      errors if the data is invalid.
        """
        name = request.data.pop('name')
        serializer = CountrySerializer(data={'name': name})
        logger.info(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryOptionsView(APIView):
    """View to list all category options and create new category options.

    This view handles GET requests to list all `Category` objects
    and POST requests to create a new `Category` object.
    """
    def get(self, request):
        """Handle GET requests to list all category options.

        This method retrieves all `Category` objects from the database,
        serializes them, and returns them as a JSON response.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing a list of all serialized
                      category options.
        """
        options = Category.objects.all()
        serializer = CategorySerializer(options, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Handle POST requests to create new category options.

        This method serializes the data from the request to create a new
        `Category` object. If the data is valid, the category is saved and
        returned as a JSON response with a 201 Created status. If the data
        is invalid, a 400 Bad Request response is returned with the errors.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing the serialized data of the
                      newly created category option if successful, or the
                      errors if the data is invalid.
        """
        name = request.data.pop('name')
        serializer = CategorySerializer(data={'name': name})
        logger.info(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class StudyDesignOptionsView(APIView):
    """View to list all study design options and create new study design options.

    This view handles GET requests to list all `StudyDesign` objects
    and POST requests to create a new `StudyDesign` object.
    """
    def get(self, request):
        """Handle GET requests to list all study design options.

        This method retrieves all `StudyDesign` objects from the database,
        serializes them, and returns them as a JSON response.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing a list of all serialized
                      study design options.
        """
        options = StudyDesign.objects.all()
        serializer = StudyDesignSerializer(options, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Handle POST requests to create new study design options.

        This method serializes the data from the request to create a new
        `StudyDesign` object. If the data is valid, the study design is saved
        and returned as a JSON response with a 201 Created status. If the data
        is invalid, a 400 Bad Request response is returned with the errors.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing the serialized data of the
                      newly created study design option if successful, or the
                      errors if the data is invalid.
        """
        design = request.data.pop('design')
        serializer = StudyDesignSerializer(data={'design': design})
        logger.info(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RiskOfBiasOptionsView(APIView):
    """View to list all risk of bias options and create new risk of bias options.

    This view handles GET requests to list all `RiskOfBias` objects
    and POST requests to create a new `RiskOfBias` object.
    """
    def get(self, request):
        """Handle GET requests to list all risk of bias options.

        This method retrieves all `RiskOfBias` objects from the database,
        serializes them, and returns them as a JSON response.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing a list of all serialized
                      risk of bias options.
        """
        options = RiskOfBias.objects.all()
        serializer = RiskOfBiasSerializer(options, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Handle POST requests to create new risk of bias options.

        This method serializes the data from the request to create a new
        `RiskOfBias` object. If the data is valid, the risk of bias is saved
        and returned as a JSON response with a 201 Created status. If the data
        is invalid, a 400 Bad Request response is returned with the errors.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing the serialized data of the
                      newly created risk of bias option if successful, or the
                      errors if the data is invalid.
        """
        rob = request.data.pop('rob')
        serializer = RiskOfBiasSerializer(data={'rob': rob})
        logger.info(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class GradeOptionsView(APIView):
    """View to list all grade options and create new grade options.

    This view handles GET requests to list all `Grade` objects
    and POST requests to create a new `Grade` object.
    """
    def get(self, request):
        """Handle GET requests to list all grade options.

        This method retrieves all `Grade` objects from the database,
        serializes them, and returns them as a JSON response.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing a list of all serialized
                      grade options.
        """
        options = Grade.objects.all()
        serializer = GradeSerializer(options, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Handle POST requests to create new grade options.

        This method serializes the data from the request to create a new
        `Grade` object. If the data is valid, the grade is saved and
        returned as a JSON response with a 201 Created status. If the data
        is invalid, a 400 Bad Request response is returned with the errors.

        Args:
            request: The HTTP request object.
            
        Returns:
            Response: A JSON response containing the serialized data of the
                      newly created grade option if successful, or the
                      errors if the data is invalid.
        """
        grade = request.data.pop('grade')
        serializer = GradeSerializer(data={'grade': grade})
        logger.info(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ParticipantDesignOptionsView(APIView):
    """View to list all participant design options and create new participant design options.

    This view handles GET requests to list all `ParticipantDesign` objects
    and POST requests to create a new `ParticipantDesign` object.
    """
    def get(self, request):
        """Handle GET requests to list all participant design options.

        This method retrieves all `ParticipantDesign` objects from the database,
        serializes them, and returns them as a JSON response.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing a list of all serialized
                      participant design options.
        """
        options = ParticipantDesign.objects.all()
        serializer = ParticipantDesignSerializer(options, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Handle POST requests to create new participant design options.

        This method serializes the data from the request to create a new
        `ParticipantDesign` object. If the data is valid, the participant design
        is saved and returned as a JSON response with a 201 Created status. If the
        data is invalid, a 400 Bad Request response is returned with the errors.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing the serialized data of the
                      newly created participant design option if successful, or
                      the errors if the data is invalid.
        """
        design = request.data.pop('design')
        serializer = ParticipantDesignSerializer(data={'design': design})
        logger.info(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImplementationOptionsView(APIView):
    """View to list all implementation options and create new implementation options.

    This view handles GET requests to list all `Implementation` objects
    and POST requests to create a new `Implementation` object.
    """
    def get(self, request):
        """Handle GET requests to list all implementation options.

        This method retrieves all `Implementation` objects from the database,
        serializes them, and returns them as a JSON response.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing a list of all serialized
                      implementation options.
        """
        options = Implementation.objects.all()
        serializer = ImplementationSerializer(options, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Handle POST requests to create new implementation options.

        This method serializes the data from the request to create a new
        `Implementation` object. If the data is valid, the implementation is
        saved and returned as a JSON response with a 201 Created status. If the
        data is invalid, a 400 Bad Request response is returned with the errors.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing the serialized data of the
                      newly created implementation option if successful, or
                      the errors if the data is invalid.
        """
        implementor = request.data.pop('implementor')
        serializer = ImplementationSerializer(data={'implementor': implementor})
        logger.info(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TestTimeOptionsView(APIView):
    """View to list all test time options and create new test time options.

    This view handles GET requests to list all `TestTime` objects
    and POST requests to create a new `TestTime` object.
    """
    def get(self, request):
        """Handle GET requests to list all test time options.

        This method retrieves all `TestTime` objects from the database,
        serializes them, and returns them as a JSON response.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing a list of all serialized
                      test time options.
        """
        options = TestTime.objects.all()
        serializer = TestTimeSerializer(options, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Handle POST requests to create new test time options.

        This method serializes the data from the request to create a new
        `TestTime` object. If the data is valid, the test time is saved and
        returned as a JSON response with a 201 Created status. If the data is
        invalid, a 400 Bad Request response is returned with the errors.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing the serialized data of the
                      newly created test time option if successful, or the
                      errors if the data is invalid.
        """
        time = request.data.pop('time')
        serializer = TestTimeSerializer(data={'time': time})
        logger.info(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class EffectSizeTypeOptionsView(APIView):
    """View to list all effect size type options and create new effect size type options.

    This view handles GET requests to list all `EffectSizeType` objects
    and POST requests to create a new `EffectSizeType` object.
    """
    def get(self, request):
        """Handle GET requests to list all effect size type options.

        This method retrieves all `EffectSizeType` objects from the database,
        serializes them, and returns them as a JSON response.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing a list of all serialized
                      effect size type options.
        """
        options = EffectSizeType.objects.all()
        serializer = EffectSizeTypeSerializer(options, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Handle POST requests to create new effect size type options.

        This method serializes the data from the request to create a new
        `EffectSizeType` object. If the data is valid, the effect size type
        is saved and returned as a JSON response with a 201 Created status. If
        the data is invalid, a 400 Bad Request response is returned with the errors.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing the serialized data of the
                      newly created effect size type option if successful, or
                      the errors if the data is invalid.
        """
        name = request.data.pop('name')
        serializer = EffectSizeTypeSerializer(data={'name': name})
        logger.info(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class DownloadCSV(APIView):
    """View to download filtered study, experiment, and effect data as a CSV file.

    This view handles GET requests to fetch data from the `Study`, `Experiment`,
    and `EffectData` models based on provided query parameters and returns it
    as a CSV file download.
    """
    def get(self, request):
        """Handle GET requests to download data as a CSV file.

        This method fetches data from the `Study`, `Experiment`, and `EffectData`
        models based on the provided query parameters, filters the data, and
        returns it as a CSV file download. The return data is structured based on the
        effect data obtained through the filters applied to the query parameters.
        Each row in the return CSV represents one effect data object.

        Args:
            request: The HTTP request object containing query parameters for filtering.

        Returns:
            HttpResponse: A response object containing the CSV file for download.
        """
        # Query the database to fetch data
        parameters = request.GET.dict()
        # Create field lists which contains the fiels of the tables
        fields_studies = [field.name for field in Study._meta.get_fields()]
        fields_experiments = [field.name for field in Experiment._meta.get_fields()]
        fields_effect_data = [field.name for field in EffectData._meta.get_fields()]
        
        # Go through all studies and find the ones which mactch study fitlers
        study_filters = filter_helper(parameters, fields_studies)
        studies = Study.objects.filter(study_filters)
        study_ids = [study.study_id for study in studies]
        
        
        # Filter through the experiments
        experiment_filters = filter_helper(parameters, fields_experiments)
        # Create filter condition on experiments so only experiment from the filterd studies are filterd
        experiment_filters &= Q(study_id__in=study_ids)
        experiments = Experiment.objects.filter(experiment_filters)     
        experiment_ids = [experiment.experiment_nr for experiment in experiments]

        
        effect_data_filters = filter_helper(parameters, fields_effect_data)  
        # Create filter condition on effekt_data so only effekt_data from the filterd experiments are filterd
        effect_data_filters &= Q(experiment_nr__in=experiment_ids)
        effect_datas = EffectData.objects.filter(effect_data_filters)

        # Create a CSV response
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'

        # Write data to CSV
        writer = csv.writer(response)
        # Write header row
        writer.writerow(['title','authors', 'keywords', 'abstract', 'category', 'country',  'year', 'DOI', 
                         'peer_reviewed', 'source', 'experiment_number',
                         'test_time', 'effect_size_number', 'intervention', 'intervention_op', 'target_population',
                         'mean_age', 'grade_k', 'grade_1', 'grade_2', 'grade_3', 'grade_4', 'grade_5',
                         'grade_6', 'grade_7', 'grade_8', 'grade_9', 'grade_10', 'grade_11', 'grade_12',
                         'ni', 'gender_1', 'gender_2', 'gender_3', 'study_design',
                         'participant_design', 'implementation', 'duration_week', 'frequency_n',
                         'intensity_n', 'effect_size_type', 'mean_age_1i', 'm1i', 'sd1i', 'n1i',
                         'mean_age_2i', 'm2i', 'sd2i', 'n2i', 'icc', 'ai', 'bi', 'ci', 'di', 'ri',
                         't', 'f_stat', 'd', 'd_var', 'rob', 'robins', 'outcome', 'test_name',
                         'outcome_full', 'outcome_op'])  # Add column names
      
        # For each effect in effect_datas write a row in the csv file with all variables defined above.
        for effekt_data in effect_datas:
            # Define the paths to the experiment of the effekt_data and the study of that experiment
            experiment = effekt_data.experiment_nr
            study = effekt_data.experiment_nr.study_id
            # Write the rows to the CSV response
            writer.writerow([study.title, study.authors, study.keywords, study.category.name, study.country.name,
                             study.study_year, study.doi, study.peer_reviewed, experiment.source, experiment.experiment_nr,
                             effekt_data.test_time.time, effekt_data.effect_size_number, experiment.intervention, 
                             experiment.intervention_op, experiment.target_population, experiment.mean_age, experiment.grade.k,
                             experiment.grade.first, experiment.grade.second, experiment.grade.third, experiment.grade.fourth,
                             experiment.grade.fifth, experiment.grade.sixth, experiment.grade.seventh,
                             experiment.grade.eighth, experiment.grade.ninth, experiment.grade.tenth, 
                             experiment.grade.eleventh, experiment.grade.twelfth,
                             experiment.ni, effekt_data.gender_1, effekt_data.gender_2, effekt_data.gender_3, 
                             experiment.study_design.design, experiment.participant_design.design, experiment.implemented.implementor,
                             experiment.duration_week, experiment.frequency_n, experiment.intensity_n, 
                             effekt_data.effect_size_type.name, effekt_data.mean_age_1i, effekt_data.m1i, effekt_data.sd1i,
                             effekt_data.n1i, effekt_data.mean_age_2i, effekt_data.m2i, effekt_data.sd2i,
                             effekt_data.n2i, effekt_data.icc, effekt_data.ai, effekt_data.bi, effekt_data.ci,
                             effekt_data.di, effekt_data.ri, effekt_data.t, effekt_data.f_stat, effekt_data.d,
                             effekt_data.d_var, experiment.risks.rob, experiment.robins, effekt_data.outcome, 
                             effekt_data.test_name, effekt_data.outcome_full, effekt_data.outcome_op])  

        return response

    
class get_orcid_infoAPIView(APIView):
    """View to retrieve ORCID information using OAuth2 authorization code flow.

    This view handles GET and POST requests to retrieve ORCID information by
    exchanging an authorization code for an access token and refresh token
    using the ORCID OAuth2 authorization code flow.
    """
    def get(self, request):
        return 
    
    def post(self, request):
        """Handle POST requests to retrieve ORCID information.

        This method handles POST requests and retrieves ORCID information
        by exchanging an authorization code for an access token and refresh token
        using the ORCID OAuth2 authorization code flow.

        Args:
            request: The HTTP request object containing the authorization code.

        Returns:
            Response: An HTTP response containing the retrieved ORCID information
            if successful, or an error response if unsuccessful.
        """
        code = request.data.get('code')
    
        client_id = 'APP-IZWWE416AT5JC4N6',
        client_secret = '51bd4130-6aad-4777-9102-4755f7a5c01a',
        redirect_uri = 'http://192.168.0.34:3000/Login'

        # Make a request to the ORCID API to get the auth token
        token_url = 'https://orcid.org/oauth/token'
        headers = {'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': redirect_uri
        }
        response = requests.post(token_url, headers=headers, data=data)

        # Check if the request was successful
        if response.status_code == 200:
            json_response = response.json()
            access_token = json_response.get('access_token')
            refresh_token = json_response.get('refresh_token')
            name = json_response.get('name')
            orcid = json_response.get('orcid')
            return Response({'access_token': access_token, 'refresh_token': refresh_token, 'name': name, 'orcid': orcid}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Failed to get auth token', "response": response}, status=status.HTTP_400_BAD_REQUEST)


class StudyViewDetail(APIView):
    """View to retrieve and modify individual study details.

    This view provides methods to retrieve details of a specific study
    and to approve a study by setting its 'approved' field to True.
    """
    @staticmethod
    def get(request, study_id):
        """
        Retrieve details of a specific study.

        This method retrieves the details of a study identified by its ID
        and returns a response with the serialized study data.

        Args:
            request: The HTTP request object.
            study_id (int): The ID of the study to retrieve.

        Returns:
            Response: An HTTP response containing the serialized study data
            if the study is found, or a 404 error response if not found.
        """

        study = get_object_or_404(Study, pk=study_id)
        return Response(StudySerializer(study).data)

    @staticmethod
    def patch(request, study_id):
        """
        Approve a study.

        This method approves a study by setting its 'approved' field to True.
        It also approves all nested experiments and effects associated with the study.

        Args:
            request: The HTTP request object.
            study_id (int): The ID of the study to approve.

        Returns:
            Response: An HTTP response containing the serialized study data
            with the approval status updated, or a 404 error response if the study is not found.
        """

        study = get_object_or_404(Study, pk=study_id)

        
        # Update the 'approved' field in the instance and all nested tables
        study.approved = True
        for experiment in study.experiments.all():
            experiment.approved = True

            for effect in experiment.effects.all():
                effect.approved = True
                effect.save()
            experiment.save()
        study.save()

        # Serialize the instance to return it in the response
        return Response(StudySerializer(study).data, status=status.HTTP_200_OK)