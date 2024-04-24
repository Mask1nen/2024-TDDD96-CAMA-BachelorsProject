import { createAuthProvider } from 'react-token-auth';

const loginUrl = "https://orcid.org/oauth/authorize?client_id=APP-IZWWE416AT5JC4N6&response_type=token&scope=openid&redirect_uri=http://192.168.0.34:3000/Login"

// Define the session type
type Session = { accessToken: string; 
                 refreshToken: string;
                 orcid: string;
                 name: string; };

// Create an authProvider instance
export const { useAuth, authFetch, login, logout } = createAuthProvider<Session>({
    getAccessToken: session => session.accessToken,
    storage: localStorage,
    expirationThresholdMillisec: 24 * 60 * 60 * 1000 // 24 hours
    
});
