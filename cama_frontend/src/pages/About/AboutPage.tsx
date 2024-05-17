{/*This file conatins the code responible for controlling the content and cunction of the about page*/}

import React from "react";
import {Grid, Paper, Box, Typography} from "@mui/material";
import CAMA_test_icon from "../../assets/images/CAMA_test_icon.png";
import InfoPopUps from "../../components/infoPopUps";
import {useState} from "react";
import multiLanguage from "../../components/multiLanguage";
import aboutHeading from "../../../src/assets/pageText/aboutPage/aboutPageHeading.json";
import aboutText1 from "../../../src/assets/pageText/aboutPage/aboutPageMain1.json";
import aboutText2 from "../../../src/assets/pageText/aboutPage/aboutPageMain2.json";
import aboutText3 from "../../../src/assets/pageText/aboutPage/aboutPageMain3.json";

import { useContext } from 'react';
import {Context} from "../../../src/App";

import '@mui/material';


const AboutPage: React.FC = () => {
    const [buttonPopup, setBottonPopup] = useState(false);
    const [isSWE, setIsSWE] = useContext(Context);    //uses the chared context for global language

	return (
        <Context.Provider value={isSWE}>
        <Box>
            {/*Creats a centered title wich the icon on both sides*/} 
            <Box display="flex"  justifyContent="center"  alignItems="center">
                <Box display="flex" sx={{justifyContent:"flex-start"}}>
                    <img src={CAMA_test_icon} alt="Description of the image" width="250" height="250" style={{ top: '-50px', position: 'relative' }}/> 
                    <Typography variant="h1" style={{ color: 'black' , textShadow: '2px 2px 4px rgba(0, 0, 0, 0.5)' }}> {multiLanguage(isSWE, aboutHeading)} </Typography>
                    <img src={CAMA_test_icon} alt="Description of the image" width="250" height="250" style={{ top: '-50px', position: 'relative' }}/>                        
                </Box>
                <Box>
                    <button onClick={() => setBottonPopup(true)} style={{ color: 'white' }}> INFO</button>
                    <InfoPopUps trigger={buttonPopup} setTrigger={setBottonPopup} >
                        <h3 >xxTestxxZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ</h3>
                        
                    </InfoPopUps>
                </Box>
            </Box>
        

        {/*Creats the two blocks for about text and a timeline report, with headline for the timeline*/}
        
        <Grid container rowSpacing={8}>
            <Grid item >
                <Paper sx={{p:3, height:'100%'}}>                
                    {multiLanguage(isSWE, aboutText1)}
                    <br />
                    {multiLanguage(isSWE, aboutText2)}
                    <br />
                    {multiLanguage(isSWE, aboutText3)}
                </Paper>
            </Grid>

            <Grid item xs={12} >
                <Typography variant="h3" style={{ color: 'black' , textShadow: '2px 2px 4px rgba(0, 0, 0, 0.5)' }}> CAMA through the years </Typography>
                <Paper sx={{p:3, height:'70%'}}> 
                <p>2020: The begining </p> <br />
                <p>2022: Cool stuff </p> <br />
                <p>2024: This website </p> <br />
                </Paper>
            </Grid>
            

        </Grid>

        </Box>
        </Context.Provider>
		);
	};
	
	export default AboutPage;