import React, { useState, useMemo } from "react";
import { Button, Grid,Tab, Box, Typography, Tabs,Input, FilledInput, OutlinedInput, InputLabel, InputAdornment, FormHelperText, FormControl, TextField, MenuItem} from "@mui/material";
import countries from "../../assets/countries.json"
import '@mui/material';
import Metaform from "./metadataForm"

const UploadPage: React.FC = () => {

	const [value, setValue] = React.useState(0);

	const handleTabChange = (event: React.SyntheticEvent, newValue: number) => {
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
				{children}
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
					<Tabs value={value} onChange={handleTabChange} aria-label="basic tabs example">
						<Tab label="Upload to existing dataset" {...a11yProps(0)} />
						<Tab label="Add meta analysis" {...a11yProps(1)} />
					</Tabs>
				</Box>
				<CustomTabPanel value={value} index={0}>
					<Typography variant="h5">
						Metadata
					</Typography>
					<Box sx={{display:"flex", flexWrap: 'wrap'}}>
							<Metaform/>



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