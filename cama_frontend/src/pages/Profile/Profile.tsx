import React from "react";
import { Button, Grid, Paper, Avatar, Box, Typography} from "@mui/material";

import '@mui/material';

const ProfilePage: React.FC = () => {
	return (
		<Box sx={{py:4}}>
			<Grid container spacing={2}>
				<Box display="flex">
					<Grid item xs={6}>
						<Paper sx={{p:3, height:'100%', mr:2}}>
							<Box display="flex" sx={{justifyContent:"flex-start"}}>
								<Avatar  sx={{width:200, height:200}} alt="Remy Sharp" src="/static/images/avatar/1.jpg" />
								<Box >
									<Box><b>Marcus Wandt</b></Box>
									<Box sx={{mt:2}}>Hedersdoktor vid Linköpings universitet, Astronaut, Chefstestare för JAS Gripen vid SAAB </Box>
									<Box sx={{mt:2}}>Lorem ipsum dolor sit amet</Box>
								</Box>
							</Box>
						</Paper>
					</Grid>
					<Grid item xs={6}>
							<Paper sx={{p:3, height:'100%'}}><b>About: </b>LLorem ipsum dolor sit ametLorem ipsum dolor sit ametLorem ipsum dolor sit ametLorem ipsum dolor sit ametLorem ipsum dolor sit ametorem ipsum dolor sit amet</Paper>
					</Grid>
				</Box>
			</Grid>
			<Grid container spacing={2} sx={{mt:2}}>
				<Box display="flex">
					<Grid item xs={6}>
						<Paper sx={{p:3, height:'100%', mr:2}}>
							<Grid container spacing={1}>
								<Typography variant="h5">
									Most viewed studies
								</Typography>
								<Typography variant="h5">
									Most viewed studies
								</Typography>

							</Grid>
						</Paper>
					</Grid>
					<Grid item xs={6}>
							<Paper sx={{p:3, height:'100%'}}><b>About:</b>LLorem ipsum dolor sit ametLorem ipsum dolor sit ametLorem ipsum dolor sit ametLorem ipsum dolor sit ametLorem ipsum dolor sit ametorem ipsum dolor sit amet</Paper>
					</Grid>
				</Box>
			</Grid>
		</Box>

		);
	};
	
	export default ProfilePage;