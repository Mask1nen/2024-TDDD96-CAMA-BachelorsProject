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
import { searchStudy, addEffect } from "../../api/dataAPI";	
	
		
const AddEffectDialog: React.FC = ({dialogOpen, handleDialogClose, experiment_nr, study_id}:any) => {

	const closeDialog = () => {
		handleDialogClose();
	}

	const effect_size_number = -1; //temporary "unique" ID. Id is set in backend later
	
	const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
		event.preventDefault();
		event.stopPropagation();

		const formData = new FormData(event.target);
		console.log(formData);

		let newEffect = emptyEffect(effect_size_number, experiment_nr, study_id);
		let effectKeys = Object.keys(newEffect);
		//fill each prop with data from form
		effectKeys.forEach(function(key) {
			if(key!="effect_size_number" && key != "study_id" && key != "experiment_nr") { //skip fields that are created in database
				newEffect[key] = formData.get(experiment_nr + "_" + effect_size_number + "_" + key);
			}
		});
		console.log(newEffect);

		try {
			const response = await addEffect(newEffect);
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

						<Effectform 
							experiment_nr={experiment_nr}
							effect_size_number={effect_size_number}
							expanded={true}
							inputs={[]}
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

export default AddEffectDialog;