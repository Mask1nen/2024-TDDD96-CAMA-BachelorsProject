import { Study, Experiment, Effect } from "./newTypes.ts"
import { apiUrl } from "./apiConfig.ts"

export const fetchFieldDefinitions = async (): Promise<any> => {
    try {
        const response = await fetch(`${apiUrl}/api/field-definitions/`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }
        });
        if (!response.ok) throw new Error('Failed to fetch field definitions');
        return await response.json();
    } catch (error) {
        console.error('Error fetching field definitions:', error);
        return null;
    }
};

export const addStudy = async (study: Study): Promise<Study | null> => {
    try {
        study.experiments = study.experiments.map(experiment => ({implemented: experiment.implementation, ...experiment, source:"frontenden såkalrt"}))
        const response = await fetch(`${apiUrl}/api/studies/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                uploader:"0000-0002-1825-0097", nr_downloads: 0, source:"felix är arg" , ...study, }
                
            ),
        });
        if (!response.ok) {
            throw new Error('Failed to post study');
        }
        return await response.json() as Study;
    } catch (error) {
        console.error('Error submitting study:', error);
        return null;
    }
};

export const fetchStudies = async (): Promise<Study[] | null> => {
    try {
        const response = await fetch(`${apiUrl}/api/studies/`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }
        }
        );
        if (!response.ok) {
            throw new Error('Failed to get studies');
        }
        return await response.json() as Study[];
    } catch (error) {
        console.error('Error getting studies:', error);
        return null;
    }
};

export const fetchStudyById = async (id: number): Promise<Study | null> => {
    try {
        const response = await fetch(`${apiUrl}/api/studies/${id}`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }
        });
        if (!response.ok) throw new Error(`Failed to fetch study with ID: ${id}`);
        return await response.json() as Study;
    } catch (error) {
        console.error(`Error fetching study with ID ${id}:`, error);
        return null;
    }
};
export const searchStudy = async (search_term: string): Promise<Study[] | null> => {
    try {
        const response = await fetch(`${apiUrl}/api/studies-filterd/?title=${search_term}`, {
            method: 'GET',
        });
        if (!response.ok) throw new Error(`Failed to search for study with title ${search_term}`);
        return await response.json() as Study[];
    } catch (error) {
        console.error(`Error searching for study with title ${search_term}:`, error);
        return null;
    }
};


export const updateStudy = async (id: number, study: Study): Promise<Study | null> => {
    try {
        const response = await fetch(`${apiUrl}/studies/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(study)
        });
        if (!response.ok) throw new Error('Failed to update study');
        return await response.json() as Study;
    } catch (error) {
        console.error('Error updating study:', error);
        return null;
    }
};

export const deleteStudy = async (id: number): Promise<boolean> => {
    try {
        const response = await fetch(`${apiUrl}/studies/${id}`, {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' }
        });
        if (!response.ok) throw new Error('Failed to delete study');
        return true;
    } catch (error) {
        console.error('Error deleting study:', error);
        return false;
    }
};

export const addExperiment = async (studyId: number, experiment: Experiment): Promise<Experiment | null> => {
    try {
        const response = await fetch(`${apiUrl}/studies/${studyId}/experiments`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(experiment)
        });
        if (!response.ok) throw new Error('Failed to add experiment');
        return await response.json() as Experiment;
    } catch (error) {
        console.error('Error adding experiment:', error);
        return null;
    }
};

export const fetchExperiments = async (studyId: number): Promise<Experiment[] | null> => {
    try {
        const response = await fetch(`${apiUrl}/studies/${studyId}/experiments`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }
        });
        if (!response.ok) throw new Error('Failed to fetch experiments');
        return await response.json() as Experiment[];
    } catch (error) {
        console.error('Error fetching experiments:', error);
        return null;
    }
};

export const fetchExperimentById = async (id: number): Promise<Experiment | null> => {
    try {
        const response = await fetch(`${apiUrl}/experiments/${id}`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }
        });
        if (!response.ok) throw new Error(`Failed to fetch experiment with ID: ${id}`);
        return await response.json() as Experiment;
    } catch (error) {
        console.error(`Error fetching experiment with ID ${id}:`, error);
        return null;
    }
};

export const updateExperiment = async (id: number, experiment: Experiment): Promise<Experiment | null> => {
    try {
        const response = await fetch(`${apiUrl}/experiments/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(experiment)
        });
        if (!response.ok) throw new Error('Failed to update experiment');
        return await response.json() as Experiment;
    } catch (error) {
        console.error('Error updating experiment:', error);
        return null;
    }
};

export const deleteExperiment = async (id: number): Promise<boolean> => {
    try {
        const response = await fetch(`${apiUrl}/experiments/${id}`, {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' }
        });
        if (!response.ok) throw new Error('Failed to delete experiment');
        return true;
    } catch (error) {
        console.error('Error deleting experiment:', error);
        return false;
    }
};

export const fetchEffects = async (experimentId: number): Promise<Effect[] | null> => {
    try {
        const response = await fetch(`${apiUrl}/experiments/${experimentId}/effects`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }
        });
        if (!response.ok) throw new Error('Failed to fetch effects');
        return await response.json() as Effect[];
    } catch (error) {
        console.error('Error fetching effects:', error);
        return null;
    }
};

export const fetchEffectById = async (id: number): Promise<Effect | null> => {
    try {
        const response = await fetch(`${apiUrl}/effects/${id}`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }
        });
        if (!response.ok) throw new Error(`Failed to fetch effect with ID: ${id}`);
        return await response.json() as Effect;
    } catch (error) {
        console.error(`Error fetching effect with ID ${id}:`, error);
        return null;
    }
};

export const updateEffect = async (id: number, effect: Effect): Promise<Effect | null> => {
    try {
        const response = await fetch(`${apiUrl}/effects/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(effect)
        });
        if (!response.ok) throw new Error('Failed to update effect');
        return await response.json() as Effect;
    } catch (error) {
        console.error('Error updating effect:', error);
        return null;
    }
};

export const deleteEffect = async (id: number): Promise<boolean> => {
    try {
        const response = await fetch(`${apiUrl}/effects/${id}`, {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' }
        });
        if (!response.ok) throw new Error('Failed to delete effect');
        return true;
    } catch (error) {
        console.error('Error deleting effect:', error);
        return false;
    }
};

