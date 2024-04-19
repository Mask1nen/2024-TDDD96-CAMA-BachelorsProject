{/*This file conatins the code responible for controlling the content and function of the login page*/}

import React from "react";
import {Box, Button} from "@mui/material";
import Logo  from "../../assets/images/orcid_logo_icon.png";
import { loginUser } from "../../api/loginAPI";



const LoginPage: React.FC = () => {
    const handleLogin = async () => {
        
        const token = await loginUser();
    }

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
                <Button variant="contained" color="primary"  href="/login" sx={{ marginTop: 10, fontSize: "1.5rem" }} onClick={() => {handleLogin()}}>
                    Login with ORCID
                    <img src={Logo} alt="ORCID logo" style={{ width: "20px", height: "20px", marginLeft: "5px" }} />
                </Button>
            </Box>
        </Box>
    );
	};
	
export default LoginPage;