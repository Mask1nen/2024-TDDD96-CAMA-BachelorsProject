import React from "react";
import { Grid, Paper, Box } from "@mui/material";

const DatabasePage: React.FC = () => {
  return (
    <Box sx={{py:4}}>
      <Grid container spacing={2}>
        <Grid item xs={6} md={8}>
          <Paper>xs=6 md=8</Paper>
        </Grid>
        <Grid item xs={6} md={4}>
          <Paper>xs=6 md=4</Paper>
        </Grid>
        <Grid item xs={6} md={4}>
          <Paper>xs=6 md=4</Paper>
        </Grid>
        <Grid item xs={6} md={8}>
          <Paper>xs=6 md=8</Paper>
        </Grid>
      </Grid>
    </Box>
  );
};
export default DatabasePage;
