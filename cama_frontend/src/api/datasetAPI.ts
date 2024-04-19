import { DataEntry } from "./types";
import { apiUrl } from "./apiConfig";


export const fetchDatasets = async (): Promise<DataEntry[] | null> => {
    try {
        const response = await fetch(`${apiUrl}/datasets`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        });

        if (!response.ok) {
            console.error("Failed to fetch datasets");
            return null;
        }

        const datasets: DataEntry[] = (await response.json()).map((dataset: any) => ({
            id: dataset.id,
            //image: dataset.image,
            title: dataset.title,
            authors: dataset.authors,
            keywords: dataset.keywords,
            abstract: dataset.abstract,
            category: dataset.category,
            country: dataset.country,
            year: dataset.year,
            doi: dataset.doi,
            peer_reviewed: dataset.peer_reviewed,
            experiment_number: dataset.experiment_number,
            effect_size_number: dataset.effect_size_number,
            mean_age: dataset.mean_age,
            grade: dataset.grade,
            ni: dataset.ni,
            gender_1: dataset.gender_1,
            gender_2: dataset.gender_2,
            study_design: dataset.study_design,
            participant_design: dataset.participant_design,
            implementation: dataset.implementation,
            duration_week: dataset.duration_week,
            frequency_n: dataset.frequency_n,
            intensity_n: dataset.intensity_n,
            m1i: dataset.m1i,
            sd1i: dataset.sd1i,
            n1i: dataset.n1i,
            m2i: dataset.m2i,
            sd2i: dataset.sd2i,
            n2i: dataset.n2i,
            icc: dataset.icc,
            ai: dataset.ai,
            bi: dataset.bi,
            ci: dataset.ci,
            di: dataset.di,
            ri: dataset.ri,
            ni__1: dataset.ni__1,
            t: dataset.t,
            f_stat: dataset.f_stat,
            d: dataset.d,
            d_var: dataset.d_var,
            rob: dataset.rob,
            robins: dataset.robins,
            outcome: dataset.outcome,
            outcome_full: dataset.outcome_full,
        }));
        return datasets;
    } catch (error) {
        console.error("Failed to fetch datasets", error);
        return null;
    }
};

export const fetchDatasetById = async (id: string): Promise<DataEntry | null> => {
    try {
        const response = await fetch(`${apiUrl}/datasets/${id}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        });

        if (!response.ok) {
            console.error(`Failed to fetch dataset with ID ${id}`);
            return null;
        }

        const dataset: DataEntry = await response.json();
        return dataset;
    } catch (error) {
        console.error(`Failed to fetch dataset with ID ${id}`, error);
        return null;
    }
};

export async function addDataset(dataset: DataEntry, token: string): Promise<string | null> {
    try {
        const response = await fetch(`${apiUrl}/datasets`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Authorization: "Bearer" + token,
            },
            body: JSON.stringify(dataset),
        });

        if (response.ok) {
            const responseData = await response.json();
            return responseData.id;
        } else {
            const error = await response.json();
            throw new Error(error.message);
        }
    } catch (error) {
        console.error("Failed to add dataset", error);
        return null;
    }
}
