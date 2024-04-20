{/*This file conatins the code responible for controlling the content and function of the login page*/}

import React, { useState } from "react";
import {Box, Button} from "@mui/material";
import Logo  from "../../assets/images/orcid_logo_icon.png";
import { loginUser } from "../../api/loginAPI";
const loginUrl = "https://orcid.org/oauth/authorize?client_id=APP-IZWWE416AT5JC4N6&response_type=token&scope=openid&redirect_uri=http://192.168.0.34:3000/Login"



const LoginPage: React.FC = () => {
    const [isLoggedIn, setIsLoggedIn] = useState(false);

    const handleLogin = () => {
        window.location.href = loginUrl;
    };

    // Function to extract token from URL after ORCID callback
    const extractTokenFromURL = () => {
        alert("extractTokenFromURL");
        const urlParams = new URLSearchParams(window.location.search);
        const access_token = urlParams.get('access_token');
        const id_token = urlParams.get('id_token');
        const tokenId = urlParams.get('tokenId');
        alert(access_token);
        if (access_token) {
            // Handle the code (token) received from ORCID
            console.log('Received code from ORCID:', access_token);
            setIsLoggedIn(true);
        }
    };

    // Check for token in URL on component mount
    React.useEffect(() => {
        extractTokenFromURL();
    }, []);

    return (
        <Box display="flex" flexDirection="column" justifyContent="center" alignItems="center">
            
            <Box display="flex" justifyContent="center" alignItems="center" sx={{ fontSize: "2rem", margin: "0.5rem" }}>
                Login to contribute
            </Box>

            <Box display="flex" justifyContent="center" alignItems="center" sx={{ fontSize: "1.2rem", margin: "1rem" }}>
                To contribute you need to be loged in.
                <br />
                Login with your ORCID account by pressing the button below.
            </Box>
            
            <Box display="flex" sx={{ justifyContent: "flex-start" }}>
                <Button variant="contained" color="primary"  sx={{ marginTop: 10, fontSize: "1.5rem" }} onClick={() => {handleLogin()}}>
                    Login with ORCID
                    <img src={Logo} alt="ORCID logo" style={{ width: "20px", height: "20px", marginLeft: "5px" }} />
                </Button>
            </Box>
        </Box>
    );
	};
	
export default LoginPage;