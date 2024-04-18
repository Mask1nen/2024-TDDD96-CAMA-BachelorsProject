from pytest_factoryboy import register

from .factories import CamaUserFactory, CountryFactory, \
                        CategoryFactory, StudyFactory, StudyDesignFactory, \
                        RiskOfBiasFactory, GradeFactory, ParticipantDesignFactory,\
                        ImplementationFactory, ExperimentFactory, EffectDataFactory
                        
register(CamaUserFactory)
register(CountryFactory)
register(CategoryFactory)
register(StudyFactory)
register(StudyDesignFactory)
register(RiskOfBiasFactory)
register(GradeFactory)
register(ParticipantDesignFactory)
register(ImplementationFactory)
register(ExperimentFactory)
register(EffectDataFactory)
                        
