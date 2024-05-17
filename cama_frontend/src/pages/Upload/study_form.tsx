import React, { useState, useMemo } from "react";
import {Link} from "react-router-dom";
import {styled, Button, Grid,Tab, Box, Typography, Tabs,Input, FilledInput, OutlinedInput, InputLabel, InputAdornment, FormHelperText, FormControl, TextField, MenuItem} from "@mui/material";
import countries from "../../assets/countries.json"


function Studyform({inputs = {}, readOnly = false}) {

	  const disabledStyling = {
		"& .MuiInputBase-input.Mui-disabled": {
			WebkitTextFillColor: "#010101",
		  },
	  };

	return (
			<div>
			<TextField defaultValue={inputs["title"] || ""} disabled={readOnly} sx={{width:"45%", m:1, ...disabledStyling}} variant="standard" label="Title" name="title" id="formTitle"/>

			<TextField defaultValue={inputs["authors"] || ""} disabled={readOnly} sx={{width:"45%", m: 1 , ...disabledStyling}} variant="standard" label="Authors"  name="authors" id="formAuthors"/>
			
			<TextField defaultValue={inputs["study_year"] || ""} disabled={readOnly} sx={{width:"45%", m:1, ...disabledStyling}} variant="standard" label="Year" name="study_year" id="formYear"/>
			
			<TextField defaultValue={inputs["keywords"] || ""} disabled={readOnly} sx={{width:"45%", m: 1 , ...disabledStyling}} variant="standard" label="Keywords" name="keywords" id="formKeywords"/>

			<TextField defaultValue={inputs["abstract"] || ""} disabled={readOnly} sx={{width:"93%", my:2, ...disabledStyling}} variant="standard" label="Abstract" multiline name="abstract" id="formAbstract"/>

								
			<TextField
				sx={{width:"45%", mt: 2, ml:1, ...disabledStyling}} variant="standard"
				disabled={readOnly} 
				id="formCountry"
				name="country"
				label="Country"
				select
				defaultValue={inputs["country"]||""}
				>
				{countries.map((option) => (
					<MenuItem key={option.value} value={option.label}>
					{option.label}
					</MenuItem>
				))}
			</TextField>
			
			<TextField
				sx={{width:"45%", mt: 2, ml: 1, ...disabledStyling}} variant="standard"
				disabled={readOnly} 
				id="formPeerReview"
				label="Peer reviewed"
				name="peer_reviewed"
				defaultValue={inputs["peer_reviewed"] ? "yes" : (inputs["peer_reviewed"] === false ? "no" : "")}
				select
				>
					<MenuItem key="yes" value="yes">
					Yes
					</MenuItem>
					<MenuItem key="no" value="no">
					No
					</MenuItem>
			</TextField>
				


			<TextField
				sx={{width:"45%", mt: 2, ml: 1, ...disabledStyling}} variant="standard"
				disabled={readOnly} 
				id="formCategory"
				label="Category"
				name="category"
				defaultValue={inputs.category||""}
				select
				>
					<MenuItem key="STEM" value="STEM">
					STEM
					</MenuItem>
					<MenuItem key="Math" value="Math">
					Math
					</MenuItem>
					<MenuItem key="Language" value="Language">
					Language
					</MenuItem>
			</TextField>

			<TextField defaultValue={inputs["doi"]||""} disabled={readOnly}  sx={{width:"45%", m: 1 , ...disabledStyling}} variant="standard" label="DOI" name="doi" id="formDOI"/>
			</div>
				

	)}

	export default Studyform;
