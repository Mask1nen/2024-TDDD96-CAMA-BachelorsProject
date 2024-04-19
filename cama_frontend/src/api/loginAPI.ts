

const loginUrl = "https://orcid.org/oauth/authorize?client_id=APP-IZWWE416AT5JC4N6&response_type=token&scope=openid&redirect_uri=http://192.168.0.34:3000/"
import axios from 'axios';


export const loginUser = async (): Promise<string | null> => {
    alert("login");
    try {
        const response = await axios.post(loginUrl);
        alert(response.data);
        // Process the response here
        return "yay"
    } catch (error) {
        alert(error);
        console.error("Error occurred while making the login request:", error);
        return null;
    }
} 