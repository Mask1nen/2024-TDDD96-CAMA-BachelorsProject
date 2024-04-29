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
import { searchStudy } from "../../api/dataAPI";	
	
		
const SearchDialog: React.FC = ({dialogOpen, handleDialogClose, setAddToExisting, setExistingStudyId}:any) => {

	const [options, setOptions] = useState([]);
	const [value, setValue] = useState({});
  
	const handleChange = (event, newValue) => {
		console.log(newValue);
		setValue(newValue);
		setExistingStudyId(newValue.study_id);
		console.log(value.title);
	}
	// Fetch options from the API based on the search term
	const fetchOptions = async (query) => {
	  try {
		const studies = await searchStudy(query);
		if (studies) {

			setOptions(studies); // Update the options state
		} else {}
	  } catch (error) {
		console.error('Error fetching options:', error);
	  }
	};


	const getOptionLabel = (option) => option.study_id + ": " + option.title;

	return(

		<Dialog
		open={dialogOpen}
		onClose={handleDialogClose}
		>
			<DialogTitle>Search study</DialogTitle>
			<DialogContent >
				<DialogContentText>
					Search for study to add experiments/effects to.
				</DialogContentText>
				
				<Autocomplete
					sx={{mt:2}}
					options={options}
					getOptionLabel={getOptionLabel}
					onChange={handleChange}
					onInputChange={(event, newInputValue) => fetchOptions(newInputValue)}
					renderInput={(params) => <TextField {...params} label="Search Studies" />}
				/>

			</DialogContent>
			<DialogActions>
			<Button onClick={handleDialogClose}>Cancel</Button>
			<Button onClick={() => {setAddToExisting(true); handleDialogClose()}}>Save</Button>
			</DialogActions>
		</Dialog>
	)
}

export default SearchDialog;