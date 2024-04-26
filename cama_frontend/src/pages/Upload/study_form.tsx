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
			<TextField defaultValue={props.inputs["title"] || ""} disabled={(props.readOnly||false)} sx={{width:"45%", m:1, ...disabledStyling}} variant="standard" label="Title" name="title" id="formTitle"/>

			<TextField defaultValue={props.inputs["authors"] || ""} disabled={(props.readOnly||false)} sx={{width:"45%", m: 1 , ...disabledStyling}} variant="standard" label="Authors"  name="authors" id="formAuthors"/>
			
			<TextField defaultValue={props.inputs["study_year"] || ""} disabled={(props.readOnly||false)} sx={{width:"45%", m:1, ...disabledStyling}} variant="standard" label="Year" name="study_year" id="formYear"/>
			
			<TextField defaultValue={props.inputs["keywords"] || ""} disabled={(props.readOnly||false)} sx={{width:"45%", m: 1 , ...disabledStyling}} variant="standard" label="Keywords" name="keywords" id="formKeywords"/>

			<TextField defaultValue={props.inputs["abstract"] || ""} disabled={(props.readOnly||false)} sx={{width:"93%", my:2, ...disabledStyling}} variant="standard" label="Abstract" multiline name="abstract" id="formAbstract"/>

								
			<TextField
				sx={{width:"45%", mt: 2, ml:1, ...disabledStyling}} variant="standard"
				disabled={(props.readOnly||false)} 
				id="formCountry"
				name="country"
				label="Country"
				select
				defaultValue={props.inputs["country"]||""}
				>
				{countries.map((option) => (
					<MenuItem key={option.value} value={option.label}>
					{option.label}
					</MenuItem>
				))}
			</TextField>
			
			<TextField
				sx={{width:"45%", mt: 2, ml: 1, ...disabledStyling}} variant="standard"
				disabled={(props.readOnly||false)} 
				id="formPeerReview"
				label="Peer reviewed"
				name="peer_reviewed"
				defaultValue={props.inputs["peer_reviewed"] ? "yes" : (props.inputs["peer_reviewed"] === false ? "no" : "")}
				select
				>
					<MenuItem key="yes" value="yes">
					Yes
					</MenuItem>
					<MenuItem key="no" value="no">
					No
					</MenuItem>
			</TextField>
				

			<TextField defaultValue={props.inputs["category"]||""} disabled={(props.readOnly||false)}  sx={{width:"45%", m: 1 , ...disabledStyling}} variant="standard" label="Category" name="category" id="formCategory"/>

			<TextField defaultValue={props.inputs["doi"]||""} disabled={(props.readOnly||false)}  sx={{width:"45%", m: 1 , ...disabledStyling}} variant="standard" label="DOI" name="doi" id="formDOI"/>
			</div>
				

	)}

	export default Studyform;
