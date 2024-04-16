import React, { useState, useMemo } from "react";
import {Link} from "react-router-dom";
import { Button, Grid,Tab, Box, Typography, Tabs,Input, FilledInput, OutlinedInput, InputLabel, InputAdornment, FormHelperText, FormControl, TextField, MenuItem, Accordion, AccordionDetails, AccordionSummary} from "@mui/material";
import countries from "../../assets/countries.json"
import fields from "./fields_effect.json"
import {Remove, ArrowDownward} from "@mui/icons-material"
import { grey, blueGrey} from '@mui/material/colors';


function Effectform() {


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


	return (
		<Box sx={{mt:3}}>
			<Accordion sx={{backgroundColor: blueGrey['A100']}}>
				<AccordionSummary
					expandIcon={<ArrowDownward />}
					aria-controls="panel1-content"
					id="panel1-header"
					>
					<Typography>Effect Data</Typography>
				</AccordionSummary>
				<AccordionDetails>
					
					<form onSubmit={handleSubmit}>
						<Box sx={{width:"100%", borderTop: 0, my:0}}></Box>

							{fields.map((field) => (field.type === "option" ? (
								<FormControl sx={{width:"30%", mt: 2, ml:1}} variant="standard">
									<TextField
										id={"form" + field.key}
										label={field.name}
										name={field.key}
										select
										value={inputs[field.key] || ""} 
										onChange={handleChange}
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
										value={inputs[field.key] || ""} 
										endAdornment={field.type === "percent" ? <InputAdornment position="end">%</InputAdornment> : ""}
										id={"form" +field.key}/>
								</FormControl>
							)))}

					</form>


				</AccordionDetails>
			</Accordion>
		</Box>

	)}

	export default Effectform;