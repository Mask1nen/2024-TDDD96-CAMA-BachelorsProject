import React, { useState} from "react";
import {Autocomplete, Dialog, DialogTitle, DialogContent, DialogActions, DialogContentText, Button, TextField} from "@mui/material";
import { searchStudy } from "../../api/dataAPI";	
	
		
const SearchDialog: React.FC = ({dialogOpen, handleDialogClose, setAddToExisting, setExistingStudyId, value}:any) => {

	const [options, setOptions] = useState([]);
  
	const handleChange = (event, newValue) => {
		console.log(newValue);
		if (newValue) {
			setExistingStudyId(newValue.study_id);
		}
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


	const getOptionLabel = (option) => option === "" ? "" : option.study_id + ": " + option.title;

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
					value={value || ""}
					onInputChange={(event, newInputValue) => fetchOptions(newInputValue)}
					renderInput={(params) => <TextField {...params} label="Search Studies" />}
				/>

			</DialogContent>
			<DialogActions>
			<Button onClick={handleDialogClose}>Cancel</Button>
			<Button disabled={!value} onClick={() => {setAddToExisting(true); handleDialogClose()}}>Fetch</Button>
			</DialogActions>
		</Dialog>
	)
}

export default SearchDialog;