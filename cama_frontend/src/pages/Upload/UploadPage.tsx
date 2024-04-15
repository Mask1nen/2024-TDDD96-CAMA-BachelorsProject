import React from "react";
import { Button, Grid, Paper, Avatar, Box, Typography} from "@mui/material";

import '@mui/material';

const UploadPage: React.FC = () => {
	return (
		<Box sx={{py:2, pl:2, textAlign:"left"}}>
			<Typography variant="h3" gutterBottom>
        		Upload
      		</Typography>
			<Typography gutterBottom>
				Are you adding a new study to an existing dataset or a whole new meta-analysis?
			</Typography>
			<Box sx={{display: 'flex', justifyContent:"space-around"}}>

				<Button variant="contained">
					Add study
				</Button>
				<Button variant="contained">
					Edit study
				</Button>
				<Button variant="contained">
					Add meta-analysis
				</Button>
				<Button variant="contained">
					Edit meta-analysis
				</Button>
			</Box>
		</Box>

		);
	};
	
	export default UploadPage;