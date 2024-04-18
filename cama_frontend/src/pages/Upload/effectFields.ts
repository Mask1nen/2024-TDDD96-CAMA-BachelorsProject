import { EffectField } from '../../types/formFieldTypes';

export const effectFields: EffectField[] = [
    {"name": "Number of the effect size", "key": "effect_size_number", "type": "int", "desc":"Which effect size in the study was it"},
	{"name": "Standard deviation of experimental group", "key": "sd1i", "type": "Float", "desc":""},
	{"name": "Number of participants in experimental grp", "key": "n1i", "type": "Float", "desc":""},
	{"name": "Number of participants in control group", "key": "n2i", "type": "Float", "desc":""},
	{"name": "Standard deviation in control group", "key": "sd2i", "type": "Float", "desc":""},
	{"name": "Mean of experimental group", "key": "m1i", "type": "Float", "desc":""},
	{"name": "Mean in control group", "key": "m2i", "type": "Float", "desc":""},
	{"name": "d_var", "key": "d_var", "type": "Float", "desc":"Cohen’ D variance"},
	{"name": "Cohen's D", "key": "d", "type": "Float", "desc":"Cohen's D"},
	{"name": "F-statistics", "key": "f_stat", "type": "Float", "desc":"F-statistics"},
	{"name": "T-test", "key": "t", "type": "Float", "desc":"T-test statistics"},
	{"name": "Pearson’s correlation", "key": "ri", "type": "Integer", "desc":"Pearson’s correlation"},
	{"name": "Age mean", "key": "mean_age", "type": "Float", "desc":"State mean of age in years"},
	{"name": "Sample size", "key": "ni", "type": "Integer", "desc":"Total sample size"},
	{"name": "Intracluster correlation coefficient", "key": "icc", "type": "Float", "desc":"Intracluster correlation coefficient"},
	{"name": "ai", "key": "ai", "type": "Integer", "desc":"Events in group a"},
	{"name": "bi", "key": "bi", "type": "Integer", "desc":"Events in group b"},
	{"name": "ci", "key": "ci", "type": "Integer", "desc":"Events in group c"},
	{"name": "di", "key": "di", "type": "Integer", "desc":"Events in group d"}
];