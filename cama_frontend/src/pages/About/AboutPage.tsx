{/*This file conatins the code responible for controlling the content and cunction of the about page*/}

import React from "react";
import {Grid, Paper, Box, Typography, Button} from "@mui/material";
import CAMA_test_icon from "../../assets/images/CAMA_test_icon.png";
import InfoPopUps from "../../components/infoPopUps";
import {useState} from "react";
import multiLanguage from "../../components/multiLanguage";
import aboutHeading from "../../../src/assets/pageText/aboutPage/aboutPageHeading.json";
import aboutText1 from "../../../src/assets/pageText/aboutPage/aboutPageMain1.json";
import aboutText2 from "../../../src/assets/pageText/aboutPage/aboutPageMain2.json";
import aboutText3 from "../../../src/assets/pageText/aboutPage/aboutPageMain3.json";
import { useContext } from 'react';
import SharedStateContext from "../../components/languageVariable";

import {Context} from "../../../src/App";

import '@mui/material';


const AboutPage: React.FC = () => {
    //const { valueS, setValue } = useContext(SharedStateContext);
    const [buttonPopup, setBottonPopup] = useState(false);
    const [isSWE, setIsSWE] = useContext(Context);
    //const valueS = useContext(SharedStateContext);

	return (
        <SharedStateContext.Provider value={isSWE}>
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
                {/*
                {/*
                    <p>Welcome to our website, dedicated to the pursuit of knowledge and understanding surrounding 
                        learning disabilities.  We are fervently committed to fostering an inclusive and supportive environment for individuals, especially children, 
                        who navigate the challenges posed by learning differences. </p> <br />
                    <p> Our platform serves as a comprehensive repository, meticulously curated with public
                        studies, research, and resources related to various learning disabilities. We recognize the importance of accessibility to credible information, 
                        which is why we strive to provide a user-friendly interface that facilitates seamless exploration and learning. </p> <br />
                    <p> Driven by our unwavering passion for 
                        children's futures, we endeavor to empower parents, educators, and professionals with the tools and insights necessary to support those with learning 
                        disabilities effectively. Through the dissemination of evidence-based studies and best practices, we aim to promote awareness, understanding, and advocacy 
                        for inclusive education. </p> <br />
                    <p> Join us in our mission to create a more compassionate and equitable society where every individual, 
                        regardless of their learning differences, is afforded the opportunity to thrive. Together, let's build a brighter future for all children, 
                        ensuring that no obstacle stands in the way of their potential and success. </p> <br />
                */}
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
        </SharedStateContext.Provider>
		);
	};
	
	export default AboutPage;