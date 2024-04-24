{/*This file conatins the code responible for controlling the content and function of the login page*/}

import React from "react";
import {Box, Button} from "@mui/material";
import Logo  from "../../assets/images/orcid_logo_icon.png";
import { apiUrl } from "../../api/apiConfig";
import { login, useAuth } from "../../hooks/useAuth";
const loginUrl = "https://orcid.org/oauth/authorize?client_id=APP-IZWWE416AT5JC4N6&response_type=code&scope=/authenticate&redirect_uri=http://192.168.0.34:3000/Login"


const LoginPage: React.FC = () => {
    const [isLoggedIn, session] = useAuth();
    if (isLoggedIn) {
        window.location.href = "/Upload";
    }

    const handleLogin = () => {
        console.log("Logging in...");
        window.location.href = loginUrl;
    };

    // Function to extract token from URL after ORCID callback
    const extractTokenFromURL = async () => {
        const urlParams = new URLSearchParams(window.location.search);
        const code = urlParams.get('code');
        console.log("Code from ORCID:", code);
    if (code) {
        try {
            const response = await fetch(`${apiUrl}/get-orcid-info/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ code }),
            });

            const data = await response.json();
            const accessToken = data.access_token;
            const refreshToken = data.refresh_token;
            const orcid = data.orcid;
            const name = data.name;
            const userSession = { accessToken, refreshToken, orcid, name };
            login(userSession);
            window.location.href = "/Upload";

        }
        catch (error) {
            alert("Failed to login with ORCID");
        }
    }
    
    }

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