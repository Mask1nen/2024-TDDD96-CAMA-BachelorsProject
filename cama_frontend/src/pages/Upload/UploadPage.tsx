import React, { useState, useMemo } from "react";
import { Button, Grid,Tab, Box, Typography, Tabs,Input, FilledInput, OutlinedInput, InputLabel, InputAdornment, FormHelperText, FormControl, TextField, MenuItem} from "@mui/material";
import countries from "../../assets/countries.json"
import '@mui/material';
import Studyform from "./study_form"
import Effectform from "./effect_form"
import Experimentform from "./experiment_form"
import {AddCircleOutline} from "@mui/icons-material"
import { v4 as uuidv4 } from 'uuid';

const UploadPage: React.FC = () => {

	const [value, setValue] = React.useState(0);



	  const addExperiment = () => {
		setExperiments(prev => [...prev, uuidv4()]);
	};
	
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
							<Studyform/>
							<Box sx={{width:"90%", borderTop: 1, mx:1, my:3}}></Box>

							<Button onClick={addExperiment} variant="outlined">Add Experiment<AddCircleOutline sx={{ml:1}}/></Button>
							
							{experiments.map((experimentId) => 
								<Experimentform key={experimentId}/>
							)}
							


					</Box>
					<Box sx={{display:"flex", justifyContent: 'flex-end'}}>
						<Button type="submit" variant="contained" className="float-">Send</Button>
					</Box>
				



		</Box>

		
		);
	};
	
	export default UploadPage;
