import React, { useState, useMemo } from "react";
import { Button, Grid,Tab, Box, Typography, Tabs,Input, FilledInput, OutlinedInput, InputLabel, InputAdornment, FormHelperText, FormControl, TextField, MenuItem} from "@mui/material";
import countries from "../../assets/countries.json"
import '@mui/material';
import Studyform from "./study_form"
import Effectform from "./effect_form"
import Experimentform from "./experiment_form"
import {AddCircleOutline} from "@mui/icons-material"
import { v4 as uuidv4 } from 'uuid';

import {Study, Experiment, Effect  } from  "../../api/newTypes"

const UploadPage: React.FC = () => {

	const [study, setStudy] = React.useState<Study>({
		title: "",
		authors: "",
		abstract: "",
		keywords: "",
		category: "",
		country: "",
		year: 0,
		doi: "",
		peer_reviewed: false,
		experiments: {}
	});
	

	const [value, setValue] = React.useState(0);



	  const addExperiment = () => {
		let id = uuidv4();
		setInputs(function(prev){
			prev["experiments"][id] = {
				"id": id,
				"title": "",
				"design": "",
				"duration": "",
				"frequency": "",
				"intensity": "",
				"grade": "",
				"ni": "",
			}
			return prev;
		}); 
		setExperiments(prev => [...prev, id]);
	};
	
	
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

	const handleExperimentChange = (event, experimentId) => {
		const { name, value } = event.target;
		
		setInputs(function(prev) {
			let exps = prev["experiments"] || {};
			exps[experimentId] = exps[experimentId] || {"experiment_id":experimentId/*Unpack interface here*/};
			exps[experimentId][name] = value;
			prev["experiments"] = exps;
			
			return {...prev}
		})
	}

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

	const [experiments, setExperiments] = useState<string[]>([]);

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
							
							{experiments.map((experimentId) => 
								<Experimentform key={experimentId} onChange={handleExperimentChange} inputs={inputs} experimentId={experimentId}/>
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
