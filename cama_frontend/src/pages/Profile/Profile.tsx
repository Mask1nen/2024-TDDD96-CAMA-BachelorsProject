import React, { useEffect, useState } from "react";
import {Grid, Paper, Avatar, Box, Typography} from "@mui/material";

import '@mui/material';
import { useAuth } from "../../hooks/useAuth";

const ProfilePage: React.FC = () => {
	const [loading, setLoading] = useState(true);
  // Change to const in production
	let [isLoggedIn, session] = useAuth();
  isLoggedIn = true; // Remove this line in production

	// Handle to not have redirection on refresh
	useEffect(() => {
		setLoading(false);
	}, [isLoggedIn]);

	if (loading) {
		return (
			<div>
				Loading...
			</div>
		);
		}
  
  if (!isLoggedIn) {
    window.location.href = "/Home";
  }

  const orcid = session?.orcid || "Your ORCID";
  const name = session?.name || "Your Name";
  return (
    <Grid container justifyContent="center">
      <Grid item xs={12} sm={6} md={4}>
        <Paper elevation={3} sx={{ padding: "2rem" }}>
          <Avatar sx={{ width: "100px", height: "100px", margin: "0 auto" }} />
          <Box textAlign="center" mt={2}>
            <Typography variant="h5">{name}</Typography>
            <Typography variant="subtitle1">{orcid}</Typography>
          </Box>
          <Box textAlign="center" mt={2}>
          </Box>
        </Paper>
      </Grid>
    </Grid>
  );
};

export default ProfilePage;