import React, { useState, useMemo } from "react";
import {Link} from "react-router-dom";
import { Button, Grid,Tab, Box, Typography, Tabs,Input, FilledInput, OutlinedInput, InputLabel, InputAdornment, FormHelperText, FormControl, TextField, MenuItem} from "@mui/material";
import countries from "../../assets/countries.json"


function Studyform() {


	const [inputs, setInputs] = useState({});
	const handleSubmit = (event) => {
		event.preventDefault();
		console.log(inputs);
	  };
	  
	const handleChange = (event) => {
		const { name, value } = event.target;
		setInputs(prev => ({ ...prev, [name]: value }));
	  };


	return (
		
		<form onSubmit={handleSubmit}>
			<FormControl sx={{width:"45%", m: 1 }} variant="standard">
				<InputLabel htmlFor="">Authors</InputLabel>
				<Input value={inputs.authors || ""} name="authors" onChange={handleChange} id="formAuthors"/>
			</FormControl>
			
			<FormControl sx={{width:"45%", m: 1 }} variant="standard">
				<InputLabel htmlFor="">Year</InputLabel>
				<Input value={inputs.year||""} name="year" onChange={handleChange} id="formYear"/>
			</FormControl>

			<FormControl sx={{width:"45%", m: 1 }} variant="standard">
				<InputLabel htmlFor="">Abstract</InputLabel>
				<Input value={inputs.abstract||""} name="abstract" onChange={handleChange} id="formAbstract"/>
			</FormControl>

			<FormControl sx={{width:"45%", m: 1 }} variant="standard">
				<InputLabel htmlFor="">Keywords</InputLabel>
				<Input value={inputs.keywords||""} name="keywords" onChange={handleChange} id="formKeywords"/>
			</FormControl>

			<FormControl sx={{width:"45%", m: 1 }} variant="standard">
				<InputLabel htmlFor="">Category</InputLabel>
				<Input value={inputs.category||""} name="category" onChange={handleChange} id="formCategory"/>
			</FormControl>

			<FormControl sx={{width:"45%", m: 1 }} variant="standard">
				<InputLabel htmlFor="">DOI</InputLabel>
				<Input value={inputs.DOI||""} name="DOI" onChange={handleChange} id="formDOI"/>
			</FormControl>

			<FormControl sx={{width:"45%", mt: 2, ml:1}} variant="standard">
								
				<TextField
					id="formCountry"
					name="country"
					label="country"
					select
					value={inputs.country || "SE"}
					onChange={handleChange}
					>
					{countries.map((option) => (
						<MenuItem key={option.value} value={option.value}>
						{option.label}
						</MenuItem>
					))}
				</TextField>
				
			</FormControl>
			<FormControl sx={{width:"45%", mt: 2, ml: 2}} variant="standard">
				<TextField
					id="formPeerReview"
					label="Peer review"
					name="peer_review"
					select
					value={inputs.peer_review || "yes"}
					onChange={handleChange}
					>
					
						<MenuItem key="yes" value="yes">
						Yes
						</MenuItem>
						<MenuItem key="no" value="no">
						No
						</MenuItem>
				</TextField>
				
			</FormControl>

				
		</form>

	)}

	export default Studyform;
