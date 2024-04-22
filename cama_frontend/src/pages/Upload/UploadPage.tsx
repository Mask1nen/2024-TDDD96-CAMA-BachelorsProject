import React, { useState, useMemo } from "react";
import { Button, Grid,Tab, Box, Typography, Tabs,Input, FilledInput, OutlinedInput, InputLabel, InputAdornment, FormHelperText, FormControl, TextField, MenuItem} from "@mui/material";
import countries from "../../assets/countries.json"
import '@mui/material';
import Studyform from "./study_form"
import Effectform from "./effect_form"
import Experimentform from "./experiment_form"
import {AddCircleOutline} from "@mui/icons-material"
import { v4 as uuidv4 } from 'uuid';
import {Experiment, Effect, Study } from '../../api/newTypes'
import { addStudy } from "../../api/dataAPI";

interface inputEvent {
	target: {
		name: 'title' | 'authors' | 'keywords' | 'abstract' | 'category' | 'country' | 'year' | 'doi' | 'peer_reviewed' | 'source' | 'experiment_number' | 'intervention' | 'intervention_op' | 'target_population' | 'mean_age' | 'grade' | 'ni' | 'study_design' | 'participant_design' | 'implementation' | 'duration_week' | 'frequency_n' | 'intensity_n' | 'robins' | 'rob' | 'test_time' | 'gender_1' | 'gender_2' | 'gender_3' | 'effect_size_type' | 'mean_age_1i' | 'm1i' | 'sd1i' | 'n1i' | 'mean_age_2i' | 'm2i' | 'sd2i' | 'n2i' | 'icc' | 'ai' | 'bi' | 'ci' | 'di' | 'ri' | 't' | 'f_stat' | 'd' | 'd_var' | 'outcome' | 'test_name' | 'outcome_full' | 'outcome_op' ; 
		value: string;
	}
}

const UploadPage: React.FC = () => {

	const [value, setValue] = React.useState(0);



	const emptyStudy = (id): Study => ({
		id: id,
		title: "",
		authors: "",
		keywords: "",
		abstract: "",
		category: "",
		country: "",
		year: 0,
		doi: "",
		peer_reviewed: false,
		experiments: [],
	});	

	//EXPERIMENT
	
	const emptyExperiment = (id: number): Experiment => ({
		studyID: inputs.id,
		id: id,
		source: "",
		experiment_number: "",
		intervention: "",
		intervention_op: "",
		target_population: "",
		mean_age: "",
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

	const addExperiment = () => {
		console.log("click")

		setExperimentValues(function(prev) {
			let id = uuidv4();
			return [...prev, emptyExperiment(id)];
		});
		console.log(experimentValues)
	};
	const [experimentValues, setExperimentValues] = React.useState<Experiment[]>([]);	

	const handleExperimentChange = (event: inputEvent, experimentId: number) => {
		const { name, value } = event.target;

		setExperimentValues(function(prev) {
			console.log([prev,experimentId])
			const res = [...prev];
			const index = prev.findIndex(e => e.id == experimentId)
			res[index][name] = value;

			return res;
		})
		console.log(experimentValues);
	}

	//EFFECT

	const emptyEffect = (id: number, experiment_id: number): Effect => ({
		id: id,
		study_id: inputs.id,
		experiment_id: experiment_id,
		source: "",
		experiment_number: -1,
		intervention: "",
		intervention_op: "",
		target_population: "",
		mean_age: "",
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


	const [effects, setEffects] = useState<number[]>([]);

    const addEffect = (experimentId: string) => {
		console.log(experimentId)
        setEffects(function(prev) {
            let id = prev.length + 1;
			let newEffect = emptyEffect(id, experimentId);
			newEffect["experiment_id"] = experimentId;
            return [...prev, newEffect]
        });  // Ensure you are adding unique identifiers
    };
	const removeEffect = (index: number) => {
        if(window.confirm('Are you sure you want to remove this effect?')) {
            setEffects(prev => prev.filter((_, idx) => idx !== index));
        }
    };

	const handleEffectChange = (event: any, experimentId: string, effectId: string) => {
		console.log(experimentId, effectId);
		const { name, value } = event.target;
		console.log(effects);
		setEffects(function(prev) {
			const res = [...prev];
			const index = prev.findIndex((e: any) => e.id == effectId && e.experiment_id == experimentId)
			res[index][name] = value;

			return res;
		});
		
	}
	const [inputs, setInputs] = useState<Study>(emptyStudy(uuidv4()));
	const handleChange = (event: any) => {
		const { name, value } = event.target;
		setInputs(prev => ({...prev, [name]: value }));
	};


	
	const handleSubmit = async (event: Event) => {
		event.preventDefault();
		
		const fullStudyData:Study = {
			...inputs,
			experiments: experimentValues.map<Experiment>(experiment => ({
				...experiment,
				effects: effects.filter<Effect>(eff => eff.experiment_id == experiment.id ).map<Effect>((eff:Effect) => ({...eff}))
			}))
		}
		console.log("Final data to submit", fullStudyData);
		
		
	
		
	


	try {
		const response = await addStudy(fullStudyData);
		if (response) {
			console.log("Study added successfully");
		} else {
			console.log("Error adding study");
		}
	} catch (error) {
		console.error('Error adding study:', error);
	}

};
	
	




	return (
		<Box sx={{py:2, pl:2, textAlign:"left"}}>
			<Typography variant="h3" gutterBottom>
        		Upload
      		</Typography>
			<Typography gutterBottom>
				Are you adding a new study to an existing dataset or a whole new meta-analysis?
			</Typography>
			
				<Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
				</Box>
				
					<Typography variant="h5">
						Study information
					</Typography>
					<Box sx={{display:"flex", flexWrap: 'wrap'}}>
						<form onSubmit={handleSubmit}>
							<Studyform onChange={handleChange} inputs={inputs}/>
							<Box sx={{width:"90%", borderTop: 1, mx:1, my:3}}></Box>

							<Button onClick={addExperiment} variant="outlined">Add Experiment<AddCircleOutline sx={{ml:1}}/></Button>
							
							{experimentValues.map((experiment, index) =>  
								<Experimentform 
									key={experiment['id']} 
									onChangeEffect={handleEffectChange} 
									onChange={handleExperimentChange} 
									inputs={experimentValues} 
									index={index}
									effects={effects}
									addEffect={addEffect}
									removeEffect={removeEffect}
									experimentId={experiment['id']}/>
							)}
							<Box sx={{display:"flex", justifyContent: 'flex-end'}}>
								<Button type="submit" variant="contained" className="float-">Send</Button>
							</Box>
						</form>
					</Box>

		</Box>

		
		);
	};
	
	export default UploadPage;
