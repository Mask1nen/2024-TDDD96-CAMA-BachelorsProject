import React, { useState, useMemo } from "react";
import {Link} from "react-router-dom";
import { Button, Grid,Tab, Box, Typography, Tabs,Input, FilledInput, OutlinedInput, InputLabel, InputAdornment, FormHelperText, FormControl, TextField, MenuItem, Accordion, AccordionDetails, AccordionSummary} from "@mui/material";
import countries from "../../assets/countries.json"
import fields from "./fields_experiment.json"
import Effectform from "./effect_form"
import {Remove, ArrowDownward, AddCircleOutline} from "@mui/icons-material"



function Experimentform() {


	const [inputs, setInputs] = useState({});
	const handleSubmit = (event) => {
		event.preventDefault();
		console.log(inputs)
	}
	const handleChange = (event) => {
		console.log(event.target.name)
		const name = event.target.name;
		const val = event.target.value;
		setInputs(values => ({...values, [name]: val}))
		console.log(inputs)
	}

	const addEffect = () => {     setEffects((prev) => [...prev, prev.length]);   };
	
	const [effects, setEffects] = useState<number[]>([]);


	return (
		<Box sx={{width:"90%", borderLeft: 4, mt:5, pl:3}}>
		
			<Accordion>
				<AccordionSummary
					expandIcon={<ArrowDownward />}
					aria-controls="panel1-content"
					id="panel1-header"
					>
					<Typography>Experiment Data</Typography>
				</AccordionSummary>
				<AccordionDetails>

					<form onSubmit={handleSubmit}>

						{fields.map((field) => (field.type === "option" ? (
							<FormControl sx={{width:"30%", mt: 0, ml:1}} variant="standard">
								<TextField
									id={"form" + field.key}
									label={field.name}
									name={field.key}
									select
									value={inputs[field.key] || ""} 
									onChange={handleChange}
									key={field.key}
									>
									{field.options.map((option) => (
										<MenuItem key={option} value={option}>
										{option}
										</MenuItem>
									))}
								</TextField>
								
							</FormControl>
						)
						: (

							<FormControl sx={{width:"23%", m: 1 }} variant="standard">
								<InputLabel htmlFor="standard-adornment-amount">{field.name}</InputLabel>
								<Input 
									name={field.key}
									onChange={handleChange}
									key={field.key}
									value={inputs[field.key] || ""} 
									endAdornment={field.type === "percent" ? <InputAdornment position="end">%</InputAdornment> : ""}
									id={"form" +field.key}/>
							</FormControl>
						)))}
					</form>


					<Effectform/>
					{effects.map((id, index) => 
						<Effectform key={id}/>
					)}
					<Button onClick={addEffect} variant="outlined" sx={{mt:2}}>Add Effect<AddCircleOutline sx={{ml:1}}/></Button>

				</AccordionDetails>
			</Accordion>
		</Box>
	)}

	export default Experimentform;