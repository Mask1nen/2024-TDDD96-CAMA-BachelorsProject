import React, { useState, useMemo } from "react";
import {Link} from "react-router-dom";
import { Button, Grid,Tab, Box, Typography, Tabs,Input, FilledInput, OutlinedInput, InputLabel, InputAdornment, FormHelperText, FormControl, TextField, MenuItem} from "@mui/material";
import countries from "../../assets/countries.json"


function Studyform(props) {


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
			<div>	
			<FormControl sx={{width:"45%", m: 1 }} variant="standard">
				<InputLabel htmlFor="">Authors</InputLabel>
				<Input value={props.inputs.authors || ""} name="authors" onChange={props.onChange} id="formAuthors"/>
			</FormControl>
			
			<TextField sx={{width:"45%", m:1}} variant="standard" label="Year" value={inputs.year||""} name="year" onChange={props.onChange} id="formYear"/>
			
			<TextField label="Abstract" multiline sx={{width:"93%", my:2}} value={props.inputs.abstract||""} name="abstract" onChange={props.onChange} id="formAbstract"/>

			<FormControl sx={{width:"45%", m: 1 }} variant="standard">
				<InputLabel htmlFor="">Keywords</InputLabel>
				<Input value={props.inputs.keywords||""} name="keywords" onChange={props.onChange} id="formKeywords"/>
			</FormControl>

			<FormControl sx={{width:"45%", m: 1 }} variant="standard">
				<InputLabel htmlFor="">Category</InputLabel>
				<Input value={props.inputs.category||""} name="category" onChange={props.onChange} id="formCategory"/>
			</FormControl>

			<FormControl sx={{width:"45%", mt: 2, ml:1}} variant="standard">
								
				<TextField
					id="formCountry"
					name="country"
					label="country"
					select
					value={props.inputs.country || "SE"}
					onChange={props.onChange}
					>
					{countries.map((option) => (
						<MenuItem key={option.value} value={option.value}>
						{option.label}
						</MenuItem>
					))}
				</TextField>
				
			</FormControl>
			<FormControl sx={{width:"45%", mt: 2, ml: 1}} variant="standard">
				<TextField
					id="formPeerReview"
					label="Peer review"
					name="peer_review"
					select
					value={props.inputs.peer_review || "yes"}
					onChange={props.onChange}
					>
					
						<MenuItem key="yes" value="yes">
						Yes
						</MenuItem>
						<MenuItem key="no" value="no">
						No
						</MenuItem>
				</TextField>
				
			</FormControl>
			<FormControl sx={{width:"45%", m: 1 }} variant="standard">
				<InputLabel htmlFor="">DOI</InputLabel>
				<Input value={props.inputs.DOI||""} name="DOI" onChange={props.onChange} id="formDOI"/>
			</FormControl>
			</div>
				

	)}

	export default Studyform;
