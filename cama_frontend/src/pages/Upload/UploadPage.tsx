import React, { useState, useMemo } from "react";
import { Button, Grid,Tab, Box, Typography, Tabs,Input, FilledInput, OutlinedInput, InputLabel, InputAdornment, FormHelperText, FormControl, TextField, MenuItem} from "@mui/material";
import countries from "../../assets/countries.json"
import '@mui/material';
import fields from "./fields.json"

const UploadPage: React.FC = () => {

	const [value, setValue] = React.useState(0);

	const handleChange = (event: React.SyntheticEvent, newValue: number) => {
	  setValue(newValue);
	};

	interface TabPanelProps {
		children?: React.ReactNode;
		index: number;
		value: number;
	  }

	function CustomTabPanel(props: TabPanelProps) {
		const { children, value, index, ...other } = props;
	  
		return (
		  <div
			role="tabpanel"
			hidden={value !== index}
			id={`simple-tabpanel-${index}`}
			aria-labelledby={`simple-tab-${index}`}
			{...other}
		  >
			{value === index && (
			  <Box sx={{ p: 3 }}>
				<Typography>{children}</Typography>
			  </Box>
			)}
		  </div>
		);
	  }

	  function a11yProps(index: number) {
		return {
		  id: `simple-tab-${index}`,
		  'aria-controls': `simple-tabpanel-${index}`,
		};
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
					<Tabs value={value} onChange={handleChange} aria-label="basic tabs example">
						<Tab label="Upload to existing dataset" {...a11yProps(0)} />
						<Tab label="Add meta analysis" {...a11yProps(1)} />
					</Tabs>
				</Box>
				<CustomTabPanel value={value} index={0}>
					<Typography variant="h5">
						Metadata
					</Typography>
					<Box sx={{display:"flex", flexWrap: 'wrap'}}>	

						<FormControl sx={{width:"45%", m: 1 }} variant="standard">
							<InputLabel htmlFor="standard-adornment-amount">Authors</InputLabel>
							<Input id="formAuthors"/>
						</FormControl>
						<FormControl sx={{width:"45%", m: 1 }} variant="standard">
							<InputLabel htmlFor="standard-adornment-amount">Year</InputLabel>
							<Input id="formYear"/>
						</FormControl>
						<FormControl sx={{width:"45%", m: 1 }} variant="standard">
							<InputLabel htmlFor="standard-adornment-amount">Abstract</InputLabel>
							<Input id="formAbstract"/>
						</FormControl>

						<FormControl sx={{width:"45%", m: 1 }} variant="standard">
							<InputLabel htmlFor="standard-adornment-amount">Keywords</InputLabel>
							<Input id="formKeywords"/>
						</FormControl>
						<FormControl sx={{width:"45%", m: 1 }} variant="standard">
							<InputLabel htmlFor="standard-adornment-amount">Category</InputLabel>
							<Input id="formCategory"/>
						</FormControl>
						<FormControl sx={{width:"45%", m: 1 }} variant="standard">
							<InputLabel htmlFor="standard-adornment-amount">DOI</InputLabel>
							<Input id="formDOI"/>
						</FormControl>

						<FormControl sx={{width:"45%", mt: 2, ml:1}} variant="standard">
							<TextField
								id="formCountry"
								label="country"
								select
								defaultValue="SE"
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
								select
								defaultValue="yes"
								>
								
									<MenuItem key="yes" value="yes">
									Yes
									</MenuItem>
									<MenuItem key="no" value="no">
									No
									</MenuItem>
							</TextField>
							
						</FormControl>
					</Box>
				<Box sx={{width:"90%", borderTop: 1, m:2}}></Box>
				<Typography variant="h5">
					Data for meta-analysis
				</Typography>
				{fields.map((field) => (field.type === "option" ? (
					<FormControl sx={{width:"30%", mt: 2, ml:1}} variant="standard">
					<TextField
						id={"form" + field.key}
						label={field.name}
						select
						defaultValue={field.options[0]} 
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
						<Input id={"form" +field.key}/>
					</FormControl>
				)))}

				<Box sx={{display:"flex", justifyContent: 'flex-end'}}>
					<Button variant="contained" className="float-">Send</Button>
				</Box>


				</CustomTabPanel>
				<CustomTabPanel value={value} index={1}>
					Item Two
				</CustomTabPanel>
				<CustomTabPanel value={value} index={2}>
					Item Three
				</CustomTabPanel>

			
		</Box>

		
		);
	};
	
	export default UploadPage;