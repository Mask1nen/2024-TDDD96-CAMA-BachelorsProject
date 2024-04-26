
export interface Study {
    study_id: number;
    title: string;
    authors: string;
    keywords: string;
    abstract: string;
    category: string;
    country: string;
    study_year: number;
    doi: string;
    peer_reviewed: boolean;
    approved: boolean;
    experiments: Experiment[];
}

export const emptyStudy = (id: number): Study => ({
    study_id: id,
    title: "",
    authors: "",
    keywords: "",
    abstract: "",
    category: "",
    country: "",
    study_year: 0,
    doi: "",
    peer_reviewed: false,
    experiments: [],
});	

export interface Experiment {
    study_id?: number;
    id?: string;
    source?: string;
    experiment_number: number;
    intervention: string;
    intervention_op: string;
    target_population: string;
    mean_age?: number;
    grade?: string;
    ni: number; //sample size
    study_design: 'RCT' | 'QES';
    participant_design: 'within' | 'between' | 'mixed';
    implementation: 'researcher' | 'teacher' | 'paraprofessional' | null;
    duration_week?: number;
    frequency_n?: number;
    intensity_n?: number;
    robins?: string;
    rob: 'low' | 'moderate' | 'high' | 'NA';
    effects: Effect[];
}

export const emptyExperiment = (id: string, study_id:number): Experiment => ({
    study_id: study_id,
    id: id,
    source: "",
    experiment_number: "",
    intervention: "",
    intervention_op: "",
    target_population: "",
    mean_age: undefined,
    grade: "",
    ni: "",
    study_design: "",
    participant_design: "",
    implementation: "",
    duration_week: "",
    frequency_n: "",
    intensity_n: "",
    robins: "",
    rob: "",
    effects: [],
});

export interface Effect {
    study_id?: number;
    experiment_id?: string;
    id?: string;
    test_time: 'baseline' | 'post-test' | 'follow-up';
    gender_1?: number;
    gender_2?: number;
    gender_3?: number;
    effect_size_type: 'SMD' | 'RR' | 'OR';
    mean_age_1i?: number;
    m1i?: number;
    sd1i?: number;
    n1i?: number;
    mean_age_2i?: number;
    m2i?: number;
    sd2i?: number;
    n2i?: number;
    icc?: number;
    ai?: number;
    bi?: number;
    ci?: number;
    di?: number;
    ri?: number;
    t?: number;
    f_stat?: number;
    d?: number;
    d_var?: number;
    outcome: string;
    test_name?: string;
    outcome_full: string;
    outcome_op?: string;
}
export const emptyEffect = (id: string, experiment_id: string, study_id: number): Effect => ({
    id: id,
    study_id: study_id,
    experiment_id: experiment_id,
    test_time: "",
    gender_1: "",
    gender_2: "",
    gender_3: "",
    effect_size_type: "",
    mean_age_1i: "",
    m1i: "",
    sd1i: "",
    n1i: "",
    mean_age_2i: "",
    m2i: "",
    sd2i: "",
    n2i: "",
    icc: "",
    ai: "",
    bi: "",
    ci: "",
    di: "",
    ri: "",
    t: "",
    f_stat: "",
    d: "",
    d_var: "",
    outcome: "",
    test_name: "",
    outcome_full: "",
    outcome_op: "",
});



