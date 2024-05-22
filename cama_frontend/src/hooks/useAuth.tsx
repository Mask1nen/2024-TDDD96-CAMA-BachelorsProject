import { createAuthProvider } from 'react-token-auth';


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
