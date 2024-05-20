export interface Field{
    name: string;
    key: string;
    type: string;
    desc: string;
    options?: string[];
    database_name?: string;
}


export interface ExperimentField extends Field{
    options?: string[];
}

export interface EffectField extends Field{
    
}