
export interface Study {
    id?: string;
    title: string;
    authors: string;
    keywords: string;
    abstract: string;
    category: string;
    country: string;
    study_year: number;
    doi: string;
    peer_reviewed: boolean;
    experiments: Experiment[];
}

export interface Experiment {
    study_id?: string;
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

export interface Effect {
    study_id?: string;
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


