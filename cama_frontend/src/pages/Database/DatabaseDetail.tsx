import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { Box, Typography, TableContainer, Paper } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import data from "../../data/randomized_data.json";
import bild2 from "../../assets/images/bild2.png";
import { fetchStudyById } from "../../api/dataAPI";

const DatabaseDetail = () => {
  const { id: paramId } = useParams();
  const id = paramId ? parseInt(paramId, 10) : null;
  const [study, setStudy] = useState(null);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    console.log("Study ID:", id); // Check what id is being captured

    const fetchStudy = async () => {
      if (!id) {
        console.error("No study ID provided");
        return; // Exit if no id to prevent erroneous API call
      }
      try {
        const response = await fetchStudyById(id);
        setStudy(response);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching study:', error);
        setError(true);
        setLoading(false);
      }
    };

    fetchStudy();
  }, [id]);

  if (!study) {
    return <Typography>Loading...</Typography>;
  }
  const { title, doi, authors, keywords, abstract, rows, columns } = study;

  return (
    <Box sx={{ margin: 4 }}>
      <Typography variant="h4" gutterBottom>
        {title}
      </Typography>
      <Typography variant="subtitle1" gutterBottom>
        DOI: {doi}
      </Typography>
      <Typography variant="subtitle1" gutterBottom>
        Authors: {authors}
      </Typography>
      <Typography variant="subtitle2" gutterBottom>
        Keywords: {keywords}
      </Typography>
      <Typography variant="body1" align="left" gutterBottom>
        Abstract: {abstract}
      </Typography>
      <Box
        component="img"
        sx={{
          height: 233,
          width: 350,
          backgroundSize: "cover",
          backgroundImage: `url(${bild2})`,
        }}
      />
      <TableContainer component={Paper} sx={{ mt: 4, overflowX: "auto" }}>
        <DataGrid
          rows={rows}
          columns={columns}
          autoHeight
          autoPageSize
          sx={{
            "& .MuiDataGrid-virtualScroller": { justifyContent: "flex-start" },
          }}
        />
      </TableContainer>
    </Box>
  );
};

export default DatabaseDetail;
