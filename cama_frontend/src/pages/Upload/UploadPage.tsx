import React, { useState, useMemo } from "react";
import { Button, Grid,Tab, Box, Typography, Tabs,Input, FilledInput, OutlinedInput, InputLabel, InputAdornment, FormHelperText, FormControl, TextField, MenuItem} from "@mui/material";
import countries from "../../assets/countries.json"
import '@mui/material';

const UploadPage: React.FC = () => {

	const [value, setValue] = React.useState(1);

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
						<Tab label="Item One" {...a11yProps(0)} />
						<Tab label="Item Two" {...a11yProps(1)} />
						<Tab label="Item Three" {...a11yProps(2)} />
					</Tabs>
				</Box>
				<CustomTabPanel value={value} index={0}>
					<FormControl sx={{width:"50%", m: 1 }} variant="standard">
						<InputLabel htmlFor="standard-adornment-amount">Year</InputLabel>
						<Input id="formYear"/>
					</FormControl>

					<FormControl sx={{width:"50%", m: 1 }} variant="standard">
						<InputLabel htmlFor="standard-adornment-amount">Authors</InputLabel>
						<Input id="formAuthors"/>
					</FormControl>

					<FormControl sx={{width:"50%", mt: 2 }} variant="standard">
						<TextField
							id="outlined-select-currency"
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