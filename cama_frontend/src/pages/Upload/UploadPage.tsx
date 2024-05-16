import React, { useState, useMemo,useEffect } from "react";
import {Dialog, DialogTitle, DialogContent, DialogActions, DialogContentText, Button, Grid,Tab, Box, Typography, Tabs,Input, FilledInput, OutlinedInput, InputLabel, InputAdornment, FormHelperText, FormControl, TextField, MenuItem} from "@mui/material";
import countries from "../../assets/countries.json"
import '@mui/material';
import Studyform from "./study_form"
import Effectform from "./effect_form"
import Experimentform from "./experiment_form"
import AddExperimentDialog from "./addExperimentDialog"
import {AddCircleOutline, RemoveCircleOutline, SavedSearch} from "@mui/icons-material"
import { v4 as uuidv4 } from 'uuid';
import {Experiment, Effect, Study, emptyExperiment, emptyEffect, emptyStudy} from '../../api/newTypes'
import { addStudy, fetchStudyById, addExperiment } from "../../api/dataAPI";
import SearchDialog from "./searchDialog";


const UploadPage: React.FC = () => {

	//EXPERIMENT
	
	const addExperiment = () => {

		setExperimentValues(function(prev) {
			return [...prev, uuidv4()]; //temporary id in frontend
		});
	};

	const removeExperiment = (experimentId: string) => {
        if(window.confirm('Are you sure you want to remove this experiment?')) {
            setExperimentValues(prev => prev.filter((experiment) => experiment !== experimentId));
        }
	}

	const clearExperiments = () => {
		setExperimentValues([]);
	}


	const [experiments, setExperimentValues] = React.useState<string[]>([]);	


	//EFFECT

	const [effects, setEffects] = useState<{experiment_nr: number, effect_size_number:number}[]>([]);

    const addEffect = (experiment_nr: string) => {
        setEffects(function(prev) {
            let effect_size_number = (prev.length + 1);
			let newEffect = {experiment_nr: experiment_nr, effect_size_number:effect_size_number}
            return [...prev, newEffect]
        });  // Ensure you are adding unique identifiers
    };
	const removeEffect = (effect_size_number: number, experiment_nr: string) => {
        if(window.confirm('Are you sure you want to remove this effect?')) {
            setEffects(prev => prev.filter((effect) => !(effect['effect_size_number'] == effect_size_number && effect['experiment_nr'] == experiment_nr)));
        }
    };
	const clearEffects = () => {
		setEffects([]);
	}

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
				if (key != "experiment_nr" && key != "study_id" && key != "effects") { //skip fields that are created in database. Effects are handled below
					newExp[key] = formData.get(experimentId + "_" + key);
				} 
			});

			//Create empty effect for each existing effect connected to this experiment and fill with data from form
			effects.forEach(function(effectListObj) {
				if (effectListObj['experiment_nr'] == experimentId) { //make sure effect is associated with this experiment
					let effect_size_number = effectListObj['effect_size_number'];
					let newEffect = emptyEffect(effect_size_number, experimentId, formEntry['study_id']);
					let effectKeys = Object.keys(newEffect);
					//fill each prop with data from form
					effectKeys.forEach(function(key) {
						if(key!="effect_size_number" && key != "study_id" && key != "experiment_nr") { //skip fields that are created in database
							newEffect[key] = formData.get(experimentId + "_" + effect_size_number + "_" + key);
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
		console.log(formData);
		let formEntry = getFormEntry(formData);
		console.log(formEntry);

		
		
		const fullStudyData:Study = {
			...formEntry,
			experiments: formEntry.experiments.map<Experiment>(experiment => ({
				...experiment,
				effect_datas: experiment.effects //@todo change
			}))
		}

		try {
			const response = await addStudy(fullStudyData);
			if (response) {
			} else {
			}
		} catch (error) {
			console.error('Error adding study:', error);
		}

	};

	//searchDialog
	const [searchDialogOpen, setSearchDialogOpen] = React.useState(false);
	const handleSearchDialogOpen = () => setSearchDialogOpen(true);
	const handleSearchDialogClose = () => setSearchDialogOpen(false);

	//add experiment dialog. Used when adding to existing study
	const [addExperimentDialogOpen, setAddExperimentDialogOpen] = React.useState(false);
	const handleAddExperimentDialogOpen = () => setAddExperimentDialogOpen(true);
	const handleAddExperimentDialogClose = () => {
		fetchExistingStudy();
		setAddExperimentDialogOpen(false);
	}

	const [addToExisting, setAddToExisting] = React.useState(false);
	const [existingStudyId, setExistingStudyId] = React.useState<number>(-1);

	const [existingStudy, setExistingStudy] = React.useState<Study>();

	const setAddNewStudy = () => {
		setAddToExisting(false);
		setExistingStudyId(-1);
		setExistingStudy(undefined);
		clearExperiments();
		clearEffects();
	}
	const fetchExistingStudy = async () => {
		if (existingStudyId != -1) {
			try {
				const study = await fetchStudyById(existingStudyId);
				clearExperiments();
				clearEffects();
				setExistingStudy(study);

			} catch (error) {
				console.error('Error fetching study:', error);
			}
		}

	}

	useEffect(() => { //runs when new study is fetched
		fetchExistingStudy();
	  }, [existingStudyId]);



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
								<Button sx={{ml:2}} size="small" variant="outlined" startIcon={<SavedSearch />} onClick={handleSearchDialogOpen}>
									Add to existing study
								</Button>
							) : (
								<Button sx={{ml:2}} size="small" onClick={setAddNewStudy} variant="outlined">Add new study</Button>
								)
							}
					<SearchDialog dialogOpen={searchDialogOpen} value={existingStudy} handleDialogClose={handleSearchDialogClose} setAddToExisting={setAddToExisting} setExistingStudyId={setExistingStudyId}/>

					</Box>
					<AddExperimentDialog dialogOpen={addExperimentDialogOpen} handleDialogClose={handleAddExperimentDialogClose} study_id={existingStudy?.study_id || 0}/>
					<Box sx={{display:"flex", flexWrap: 'wrap'}}>
						<form onSubmit={handleSubmit}>
							
							<Studyform key={uuidv4()} readOnly={addToExisting} inputs={addToExisting ? existingStudy : {}}/>
							<Box sx={{width:"90%", borderTop: 1, mx:1, my:3}}></Box>

							{!addToExisting ? (
							<Button onClick={addExperiment} variant="outlined">Add Experiment<AddCircleOutline sx={{ml:1}}/></Button>
						) : (
							<Button sx={{ml:2}} size="small" variant="contained" onClick={handleAddExperimentDialogOpen}>
								Add experiment to study
							</Button>
						)}
							

							{experiments.map((experiment) =>
								<Box key={experiment}>
									<Experimentform 
										key={experiment} 
										inputs={{}}
										readOnly={false}
										effects={effects}
										addEffect={addEffect}
										removeEffect={removeEffect}
										experiment_nr={experiment}/>
								
									<Button sx={{mt:1}} size='small' onClick={() => removeExperiment(experiment)} variant="outlined" startIcon={<RemoveCircleOutline />}>
										Remove Experiment
									</Button>	
								</Box>
							)}
							
							{addToExisting ? (existingStudy?.experiments.map((experiment) =>
								<Box key={experiment.experiment_nr}>
									<Experimentform 
										inputs={experiment}
										readOnly={addToExisting}
										addToExisting={true}
										effects={effects}
										addEffect={addEffect}
										removeEffect={removeEffect}
										experiment_nr={experiment.experiment_nr}
										fetchExistingStudy={fetchExistingStudy}
										/>
								
								</Box>
							)) : ""}
							<Box sx={{display:"flex", justifyContent: 'flex-end'}}>
								<Button type="submit" variant="contained" className="float-">Send</Button>
							</Box>
						</form>
					</Box>

		</Box>

		);
	};
	
	export default UploadPage;
