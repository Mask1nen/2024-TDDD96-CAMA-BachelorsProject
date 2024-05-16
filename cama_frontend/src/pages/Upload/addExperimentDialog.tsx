import React, { useState, useMemo } from "react";
import {Autocomplete, Dialog, DialogTitle, DialogContent, DialogActions, DialogContentText, Button, Grid,Tab, Box, Typography, Tabs,Input, FilledInput, OutlinedInput, InputLabel, InputAdornment, FormHelperText, FormControl, TextField, MenuItem} from "@mui/material";
import countries from "../../assets/countries.json"
import '@mui/material';
import Studyform from "./study_form"
import Effectform from "./effect_form"
import Experimentform from "./experiment_form"
import {AddCircleOutline, RemoveCircleOutline, SavedSearch} from "@mui/icons-material"
import { v4 as uuidv4 } from 'uuid';
import {Experiment, Effect, Study, emptyExperiment, emptyEffect, emptyStudy} from '../../api/newTypes'
import { searchStudy, addExperiment } from "../../api/dataAPI";	
	
		
const AddExperimentDialog: React.FC = ({dialogOpen, handleDialogClose, study_id}:any) => {

	const closeDialog = () => {
		clearEffect();
		handleDialogClose();
	}

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

	const clearEffect = () => {
		setEffects([]);
	}
	
	const experiment_nr = -1;

	const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
		event.preventDefault();
		let experimentId = -1; //temporary unique ID. Id is set in backend later

		const formData = new FormData(event.target);
		console.log(formData);

		let newExp = emptyExperiment(experimentId, study_id);
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
				let newEffect = emptyEffect(effect_size_number, experimentId, study_id);
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

		try {
			const response = await addExperiment(newExp);
			if (response) {
			} else {
			}
		} catch (error) {
			console.error('Error adding study:', error);
		}
		handleDialogClose();
	};

	return(

		<Dialog
		maxWidth="md" fullWidth 
		open={dialogOpen}
		onClose={handleDialogClose}
		>
			<form onSubmit={handleSubmit}>
				<DialogTitle>Add Experiment</DialogTitle>
				<DialogContent >
					<DialogContentText>
						Search for study to add experiments/effects to.
					</DialogContentText>

						<Experimentform 
							experiment_nr={experiment_nr}
							addEffect={addEffect}
							removeEffect={removeEffect}
							effects={effects}
							expanded={true}
							/>
					

				</DialogContent>
				<DialogActions>
					<Button onClick={closeDialog}>Cancel</Button>
					<Button type="submit" variant="contained" className="float-">Send</Button>
				</DialogActions>
			</form>
		</Dialog>
	)
}

export default AddExperimentDialog;