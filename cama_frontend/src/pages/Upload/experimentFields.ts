import { ExperimentField } from '../../types/formFieldTypes';

export const experimentFields: ExperimentField[] = [
    { "name": "Participant Design", "key": "participant_design", "type": "option", "desc": "E.g. within or between subject design", "options": ["within", "between", "mixed"] },
    { "name": "Implementation", "key": "implementation", "type": "option", "desc": "Who conducted/implemented the intervention", "options": ["researcher", "teacher", "paraprofessional"] },
    { "name": "Study Design", "key": "study_design", "type": "option", "desc": "Eg. RCT, QES", "options": ["RCT", "QES"] },
    { "name": "Number of the experiment", "key": "experiment_number", "type": "int", "desc": "Which experiment in the study was it" },
    { "name": "Risk of Bias (Cochrane)", "key": "rob", "type": "string", "desc": "Risk of bias assessment for randomized studies - final score for the entire study" },
    { "name": "School grade", "key": "grade", "type": "string", "desc": "State the grades (eg. K-12)" },
    { "name": "Males", "key": "gender_1", "type": "int", "desc": "Total number of males included in the study" },
    { "name": "Females", "key": "gender_2", "type": "int", "desc": "Total number of females included in the study" },
    { "name": "Other (gender)", "key": "gender_3", "type": "int", "desc": "Total number of other/do not want to answer included in the study" },
    { "name": "Intensity of the sessions", "key": "intensity_n", "type": "int", "desc": "How long were each session in minutes?" },
    { "name": "Duration in weeks", "key": "duration_week", "type": "int", "desc": "How long was the intervention?" },
    { "name": "Frequency of sessions", "key": "frequency_n", "type": "int", "desc": "How many occasions did the intervention run?" },
    { "name": "Outcome", "key": "outcome", "type": "string", "desc": "Machine readable (eg. phon_aware)" },
    { "name": "Full outcome Name", "key": "outcome_full", "type": "string", "desc": "Full name of the outcome as stated in the study (eg. Phonological awareness)" }

];

