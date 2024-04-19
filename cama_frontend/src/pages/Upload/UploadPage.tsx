import React, { useState, useMemo } from "react";
import { Button, Grid,Tab, Box, Typography, Tabs,Input, FilledInput, OutlinedInput, InputLabel, InputAdornment, FormHelperText, FormControl, TextField, MenuItem} from "@mui/material";
import countries from "../../assets/countries.json"
import '@mui/material';
import Studyform from "./study_form"
import Effectform from "./effect_form"
import Experimentform from "./experiment_form"
import {AddCircleOutline} from "@mui/icons-material"
import { v4 as uuidv4 } from 'uuid';
import {Experiment } from '../../api/newTypes'

const UploadPage: React.FC = () => {

	const [value, setValue] = React.useState(0);


	
	const emptyExperiment = (id): Experiment => ({
		id: id,
		source: "",
		experiment_number: "",
		intervention: "",
		intervention_op: "",
		target_population: "",
		mean_age: "",
		grade: "",
		ni: "",
		study_design: "",
		participant_design: "",
		implementation: "",
		duration_week: "",
		frequency_n: "",
		intensity_n: "",
		robins: "",
		rob: "",
		effects: [],
	});

	const addExperiment = () => {
		console.log("click")

		setExperimentValues(function(prev) {
			let id = uuidv4();
			return [...prev, emptyExperiment(id)];
		});
		console.log(experimentValues)
	};
	const [experimentValues, setExperimentValues] = React.useState([]);	

	const handleExperimentChange = (event, experimentId) => {
		const { name, value } = event.target;

		setExperimentValues(function(prev) {
			console.log([prev,experimentId])
			const res = [...prev];
			const index = prev.findIndex(e => e.id == experimentId)
			res[index][name] = value;

			return res;
		})
		console.log(experimentValues);
	}
	React.useEffect(() => {
		console.log('experimentValues efter uppdatering:', experimentValues);
	  }, [experimentValues]);
	
	
	const handleSubmit = (event) => {
		event.preventDefault();
		console.log(inputs);
		let exps = inputs["experiments"] || {};
		exps = Object.values(exps);
		console.log(exps)
		inputs["experiments"] = exps;
		console.log(inputs)
	};

	const [inputs, setInputs] = useState({experiments:{}});
	
	const handleChange = (event) => {
		console.log(event)
		const { name, value } = event.target;
		setInputs(prev => ({...prev, [name]: value }));
	};


	const handleEffectChange = (event, experimentId, effectId) => {

		const { name, value } = event.target;
		
		setInputs(function(prev) {
			let exps = prev["experiments"] || {};
			exps[experimentId] = exps[experimentId] || {"experiment_id":experimentId/*Unpack interface here*/};
			exps[experimentId][name] = value;
			prev["experiments"] = exps;
			
			return {...prev}
		})
	}


	return (
		<Box sx={{py:2, pl:2, textAlign:"left"}}>
			<Typography variant="h3" gutterBottom>
        		Upload
      		</Typography>
			<Typography gutterBottom>
				Are you adding a new study to an existing dataset or a whole new meta-analysis?
			</Typography>
			
				<Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
				</Box>
				
					<Typography variant="h5">
						Study information
					</Typography>
					<Box sx={{display:"flex", flexWrap: 'wrap'}}>
						<form onSubmit={handleSubmit}>
							<Studyform onChange={handleChange} inputs={inputs}/>
							<Box sx={{width:"90%", borderTop: 1, mx:1, my:3}}></Box>

							<Button onClick={addExperiment} variant="outlined">Add Experiment<AddCircleOutline sx={{ml:1}}/></Button>
							
							{experimentValues.map((experiment, index) =>  
								<Experimentform 
									key={experiment['id']} 
									onChangeEffect={handleEffectChange} 
									onChange={handleExperimentChange} 
									inputs={experimentValues} 
									index={index}
									experimentId={experiment['id']}/>
							)}
							<Box sx={{display:"flex", justifyContent: 'flex-end'}}>
								<Button type="submit" variant="contained" className="float-">Send</Button>
							</Box>
						</form>
					</Box>
				



		</Box>

		
		);
	};
	
	export default UploadPage;
