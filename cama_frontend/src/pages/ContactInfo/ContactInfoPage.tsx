{/*This file conatins the code responible for controlling the content and cunction of the about page*/}

import React from "react";
import {Grid, Paper, Box, Typography} from "@mui/material";
import CAMA_test_icon from "../../assets/images/CAMA_test_icon.png";


import '@mui/material';

const ContactInfoPage: React.FC = () => {
	return (
        <Box>
            {/*Creats a centered title wich the icon on both sides*/}
            <Box display="flex"  justifyContent="center"  alignItems="center">
                <Box display="flex" sx={{justifyContent:"flex-start"}}>
                    <img src={CAMA_test_icon} alt="Description of the image" width="250" height="250" style={{ top: '-50px', position: 'relative' }}/>  
                    <Typography variant="h1" style={{ color: 'black' , textShadow: '2px 2px 4px rgba(0, 0, 0, 0.5)' }}>   Contact info</Typography>
                    <img src={CAMA_test_icon} alt="Description of the image" width="250" height="250" style={{ top: '-50px', position: 'relative' }}/>                        
                </Box>
            </Box>
        

        {/*Creats the two blocks for about text and a timeline report, with headline for the timeline*/}
        <Grid container rowSpacing={8}>
            <Grid item xs={12}>
                <Paper sx={{p:3, height:'100%'}}> 
                    You can reach Lucija Batinovic at name@email.se
                </Paper>
            </Grid>
            
            <Grid item xs={12} >
                <Typography variant="h3" style={{ color: 'black' , textShadow: '2px 2px 4px rgba(0, 0, 0, 0.5)' }}> Developers </Typography>
                <Paper sx={{p:3, height:'70%'}}> 
                    <p>Grabbarna </p> <br />
                    <p>Grus </p> <br />
                </Paper>
            </Grid>

        </Grid>

        </Box>
		);
	};
	
	export default ContactInfoPage;