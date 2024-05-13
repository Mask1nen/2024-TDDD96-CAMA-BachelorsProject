{/*This file conatins the code responible for controlling the content and cunction of the about page*/}

import React from "react";
import {Grid, Paper, Box, Typography} from "@mui/material";
import CAMA_test_icon from "../../assets/images/CAMA_test_icon.png";
import teamHeading from "../../../src/assets/pageText/teamPage/teamPageHeading.json";
import teamText1 from "../../../src/assets/pageText/teamPage/teamPageMain1.json";
import teamText2 from "../../../src/assets/pageText/teamPage/teamPageMain2.json";
import teamText3 from "../../../src/assets/pageText/teamPage/teamPageMain3.json";
import teamText4 from "../../../src/assets/pageText/teamPage/teamPageMain4.json";
import teamText5 from "../../../src/assets/pageText/teamPage/teamPageMain5.json";
import teamText6 from "../../../src/assets/pageText/teamPage/teamPageMain6.json";
import teamDevelopers from "../../../src/assets/pageText/teamPage/teamDevelopers.json";



import { useContext } from 'react';
import {Context} from "../../../src/App";
import multiLanguage from "../../components/multiLanguage";

import '@mui/material';

const TeamPage: React.FC = () => {
    const [isSWE, setIsSWE] = useContext(Context); //uses the chared context for global language

	return (
        <Box>
            {/*Creats a centered title wich the icon on both sides*/}
            <Box display="flex"  justifyContent="center"  alignItems="center">
                <Box display="flex" sx={{justifyContent:"flex-start"}}>
                    <img src={CAMA_test_icon} alt="Description of the image" width="250" height="250" style={{ top: '-50px', position: 'relative' }}/>  
                    <Typography variant="h1" style={{ color: 'black' , textShadow: '2px 2px 4px rgba(0, 0, 0, 0.5)' }}> {multiLanguage(isSWE, teamHeading)} </Typography>
                    <img src={CAMA_test_icon} alt="Description of the image" width="250" height="250" style={{ top: '-50px', position: 'relative' }}/>                        
                </Box>
            </Box>
        

        {/*Creats the two blocks for about text and a timeline report, with headline for the timeline*/}
        <Grid container rowSpacing={8}>
            <Grid item xs={12}>
                <Paper sx={{p:3, height:'100%'}}>
                    {multiLanguage(isSWE, teamText1)}
                    <br />
                    {multiLanguage(isSWE, teamText2)}
                    <br />
                    {multiLanguage(isSWE, teamText3)}
                    <br />
                    {multiLanguage(isSWE, teamText4)}
                    <br />
                    {multiLanguage(isSWE, teamText5)}
                    <br />
                    {multiLanguage(isSWE, teamText6)}
                </Paper>
            </Grid>
            
            <Grid item xs={12} >
                <Typography variant="h3" style={{ color: 'black' , textShadow: '2px 2px 4px rgba(0, 0, 0, 0.5)' }}> Developers </Typography>
                <Paper sx={{p:3, height:'70%'}}> 
                    {multiLanguage(isSWE, teamDevelopers)}
                </Paper>
            </Grid>

        </Grid>

        </Box>
		);
	};
	
	export default TeamPage;