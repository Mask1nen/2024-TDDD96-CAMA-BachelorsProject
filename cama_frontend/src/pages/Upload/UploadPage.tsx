import React, { useState, useMemo } from "react";
import {Dialog, DialogTitle, DialogContent, DialogActions, DialogContentText, Button, Grid,Tab, Box, Typography, Tabs,Input, FilledInput, OutlinedInput, InputLabel, InputAdornment, FormHelperText, FormControl, TextField, MenuItem} from "@mui/material";
import countries from "../../assets/countries.json"
import '@mui/material';
import Studyform from "./study_form"
import Effectform from "./effect_form"
import Experimentform from "./experiment_form"
import {AddCircleOutline, RemoveCircleOutline, SavedSearch} from "@mui/icons-material"
import { v4 as uuidv4 } from 'uuid';
import {Experiment, Effect, Study, emptyExperiment, emptyEffect, emptyStudy} from '../../api/newTypes'
import { addStudy } from "../../api/dataAPI";
import SearchDialog from "./searchDialog";


interface inputEvent {
	target: {
		name: 'title' | 'authors' | 'keywords' | 'abstract' | 'category' | 'country' | 'year' | 'doi' | 'peer_reviewed' | 'source' | 'experiment_number' | 'intervention' | 'intervention_op' | 'target_population' | 'mean_age' | 'grade' | 'ni' | 'study_design' | 'participant_design' | 'implementation' | 'duration_week' | 'frequency_n' | 'intensity_n' | 'robins' | 'rob' | 'test_time' | 'gender_1' | 'gender_2' | 'gender_3' | 'effect_size_type' | 'mean_age_1i' | 'm1i' | 'sd1i' | 'n1i' | 'mean_age_2i' | 'm2i' | 'sd2i' | 'n2i' | 'icc' | 'ai' | 'bi' | 'ci' | 'di' | 'ri' | 't' | 'f_stat' | 'd' | 'd_var' | 'outcome' | 'test_name' | 'outcome_full' | 'outcome_op' ; 
		value: string;
	}
}

const UploadPage: React.FC = () => {

	//EXPERIMENT
	
	const addExperiment = () => {

		setExperimentValues(function(prev) {
			return [...prev, uuidv4()];
		});
	};

	const removeExperiment = (experimentId: string) => {
        if(window.confirm('Are you sure you want to remove this experiment?')) {
            setExperimentValues(prev => prev.filter((experiment) => experiment !== experimentId));
        }
	}


	const [experiments, setExperimentValues] = React.useState<string[]>([]);	


	//EFFECT

	const [effects, setEffects] = useState<{experiment_id: string, id:string}[]>([]);

    const addEffect = (experimentId: string) => {
        setEffects(function(prev) {
            let id = (prev.length + 1).toString();
			let newEffect = {experiment_id: experimentId, id:id}
            return [...prev, newEffect]
        });  // Ensure you are adding unique identifiers
    };
	const removeEffect = (effectId: string, experimentId: string) => {
        if(window.confirm('Are you sure you want to remove this effect?')) {
            setEffects(prev => prev.filter((effect) => !(effect['id'] === effectId && effect['experiment_id'] === experimentId)));
        }
    };

	//STUDY

	const getFormEntry = (formData:FormData) => {

		//Create empty study 
		let formEntry = emptyStudy(0);
		//fill with values from form
		let studyKeys = Object.keys(formEntry);
		studyKeys.forEach(function(key){
			if (key != "experiments" && key != "id") {
				formEntry[key] = formData.get(key);
			}
		})

		//Create empty experiment for each existing experiment
		experiments.forEach(function(experimentId) {
			let newExp = emptyExperiment(experimentId, formEntry['study_id']);
			let experimentKeys = Object.keys(newExp);
			//fill each prop with data from form
			experimentKeys.forEach(function(key) {
				if (key != "id" && key != "study_id" && key != "effects") {
					newExp[key] = formData.get(experimentId + "_" + key);
				} 
				
			});

			//Create empty effect for each existing effect connected to this experiment and fill with data from form
			effects.forEach(function(effectListObj) {
				if (effectListObj['experiment_id'] == experimentId) { //make sure effect is associated with this experiment
					let effectId = effectListObj['id'];
					let newEffect = emptyEffect(effectId, experimentId, formEntry['study_id']);
					let effectKeys = Object.keys(newEffect);
					//fill each prop with data from form
					effectKeys.forEach(function(key) {
						if(key!="id" && key != "study_id" && key != "experiment_id") {
							newEffect[key] = formData.get(experimentId + "_" + effectId + "_" + key);
						}
						
					});
					newExp.effects.push(newEffect);
				}
			});

			formEntry.experiments.push(newExp);

		});
		return formEntry
	}


	
	const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
		event.preventDefault();

		const formData = new FormData(event.target);
		let formEntry = getFormEntry(formData);

		
		
		const fullStudyData:Study = {
			...formEntry,
			experiments: formEntry.experiments.map<Experiment>(experiment => ({
				...experiment,
				effect_datas: experiment.effects //@todo change
			}))
		}
		
		console.log(fullStudyData)
		
		try {
			const response = await addStudy(fullStudyData);
			if (response) {
			} else {
			}
		} catch (error) {
			console.error('Error adding study:', error);
		}

	};

	//Dialog
	const [dialogOpen, setDialogOpen] = React.useState(false);
	const handleDialogOpen = () => setDialogOpen(true);
	const handleDialogClose = () => setDialogOpen(false);

	const [addToExisting, setAddToExisting] = React.useState(false);
	const [existingStudy, setExistingStudyId] = React.useState(null);



	return (
		<Box sx={{py:2, pl:2, textAlign:"left"}}>
			<Typography variant="h3" gutterBottom>
        		Upload
      		</Typography>
			<Typography gutterBottom>
				Are you adding a new study to an existing dataset or a whole new meta-analysis?
			</Typography>
			
				<Box sx={{ borderBottom: 1, borderColor: 'divider', my:1}}>
				</Box>
				
					<Box sx={{display:"flex", justifyContent:"start"}}>

						<Typography variant="h5">
							Study information
						</Typography>
						
						{!addToExisting ? (
								<Button sx={{ml:2}} size="small" variant="outlined" startIcon={<SavedSearch />} onClick={handleDialogOpen}>
									Add to existing study
								</Button>
							) : (
								<Button sx={{ml:2}} size="small" onClick={() => setAddToExisting(false)} variant="outlined">Add new study</Button>
								)
							}
					<SearchDialog dialogOpen={dialogOpen} handleDialogClose={handleDialogClose} setAddToExisting={setAddToExisting} setExistingStudyId={setExistingStudyId}/>

					</Box>
					<Box sx={{display:"flex", flexWrap: 'wrap'}}>
						<form onSubmit={handleSubmit}>
							<Studyform inputs={{}}/>
							<Box sx={{width:"90%", borderTop: 1, mx:1, my:3}}></Box>

							<Button onClick={addExperiment} variant="outlined">Add Experiment<AddCircleOutline sx={{ml:1}}/></Button>
							
							{experiments.map((experiment) =>
								<Box key={experiment}>
									<Experimentform 
										key={experiment} 
										inputs={{}}
										effects={effects}
										addEffect={addEffect}
										removeEffect={removeEffect}
										experimentId={experiment}/>
								
									<Button sx={{mt:1}} size='small' onClick={() => removeExperiment(experiment)} variant="outlined" startIcon={<RemoveCircleOutline />}>
										Remove Experiment
									</Button>	
								</Box>
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
