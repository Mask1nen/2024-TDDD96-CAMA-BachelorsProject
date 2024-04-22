import { EffectField } from '../../types/formFieldTypes';

export const effectFields: EffectField[] = [
    { name: "Number of the effect size", key: "effect_size_number", type: "number", desc: "Which effect size in the study was it" },
    { name: "Standard deviation of experimental group", key: "sd1i", type: "number", desc: "" },
    { name: "Number of participants in experimental group", key: "n1i", type: "number", desc: "" },
    { name: "Number of participants in control group", key: "n2i", type: "number", desc: "" },
    { name: "Standard deviation in control group", key: "sd2i", type: "number", desc: "" },
    { name: "Mean of experimental group", key: "m1i", type: "number", desc: "" },
    { name: "Mean in control group", key: "m2i", type: "number", desc: "" },
    { name: "d_var", key: "d_var", type: "number", desc: "Cohen’s D variance" },
    { name: "Cohen's D", key: "d", type: "number", desc: "Cohen's D" },
    { name: "F-statistics", key: "f_stat", type: "number", desc: "F-statistics" },
    { name: "T-test", key: "t", type: "number", desc: "T-test statistics" },
    { name: "Pearson’s correlation", key: "ri", type: "number", desc: "Pearson’s correlation" },
    { name: "Age mean", key: "mean_age", type: "number", desc: "State mean of age in years" },
    { name: "Sample size", key: "ni", type: "number", desc: "Total sample size" },
    { name: "Intracluster correlation coefficient", key: "icc", type: "number", desc: "Intracluster correlation coefficient" },
    { name: "ai", key: "ai", type: "number", desc: "Events in group a" },
    { name: "bi", key: "bi", type: "number", desc: "Events in group b" },
    { name: "ci", key: "ci", type: "number", desc: "Events in group c" },
    { name: "di", key: "di", type: "number", desc: "Events in group d" }
];
