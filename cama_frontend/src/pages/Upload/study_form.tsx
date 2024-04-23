import React, { useState, useMemo } from "react";
import {Link} from "react-router-dom";
import {styled, Button, Grid,Tab, Box, Typography, Tabs,Input, FilledInput, OutlinedInput, InputLabel, InputAdornment, FormHelperText, FormControl, TextField, MenuItem} from "@mui/material";
import countries from "../../assets/countries.json"


function Studyform(props) {



	  const disabledStyling = {
		"& .MuiInputBase-input.Mui-disabled": {
			WebkitTextFillColor: "#010101",
		  },
	  };

	return (
			<div>
			<TextField disabled={(props.readOnly||false)} sx={{width:"45%", m:1, ...disabledStyling}} variant="standard" label="Title" value={props.inputs.title||""} name="title" onChange={props.onChange} id="formTitle"/>

			<TextField disabled={(props.readOnly||false)} sx={{width:"45%", m: 1 , ...disabledStyling}} variant="standard" label="Authors"  value={props.inputs.authors || ""} name="authors" onChange={props.onChange} id="formAuthors"/>
			
			<TextField disabled={(props.readOnly||false)} sx={{width:"45%", m:1, ...disabledStyling}} variant="standard" label="Year" value={props.inputs.study_year||""} name="study_year" onChange={props.onChange} id="formYear"/>
			
			<TextField disabled={(props.readOnly||false)} sx={{width:"45%", m: 1 , ...disabledStyling}} variant="standard" label="Keywords" value={props.inputs.keywords||""} name="keywords" onChange={props.onChange} id="formKeywords"/>

			<TextField disabled={(props.readOnly||false)} sx={{width:"93%", my:2, ...disabledStyling}} label="Abstract" multiline value={props.inputs.abstract||""} name="abstract" onChange={props.onChange} id="formAbstract"/>

								
			<TextField
				sx={{width:"45%", mt: 2, ml:1, ...disabledStyling}} variant="standard"
				disabled={(props.readOnly||false)} 
				id="formCountry"
				name="country"
				label="country"
				select
				value={props.inputs.country || ""}
				onChange={props.onChange}
				>
				{countries.map((option) => (
					<MenuItem key={option.value} value={option.value}>
					{option.label}
					</MenuItem>
				))}
			</TextField>
			
			<TextField
				sx={{width:"45%", mt: 2, ml: 1, ...disabledStyling}} variant="standard"
				disabled={(props.readOnly||false)} 
				id="formPeerReview"
				label="Peer review"
				name="peer_review"
				select
				value={props.inputs.peer_review || ""}
				onChange={props.onChange}
				>
				
					<MenuItem key="yes" value="yes">
					Yes
					</MenuItem>
					<MenuItem key="no" value="no">
					No
					</MenuItem>
			</TextField>
				

			<TextField disabled={(props.readOnly||false)}  sx={{width:"45%", m: 1 , ...disabledStyling}} variant="standard" value={props.inputs.category||""} label="Category" name="category" onChange={props.onChange} id="formCategory"/>

			<TextField disabled={(props.readOnly||false)}  sx={{width:"45%", m: 1 , ...disabledStyling}} variant="standard" value={props.inputs.doi||""} label="DOI" name="doi" onChange={props.onChange} id="formDOI"/>
			</div>
				

	)}

	export default Studyform;
