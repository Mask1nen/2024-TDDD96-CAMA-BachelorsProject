import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { Box, Typography, Paper } from "@mui/material";
import { fetchStudyById } from "../../api/dataAPI";

const DatabaseDetail = () => {
  const { id: paramId } = useParams();
  const id = paramId ? parseInt(paramId, 10) : null;
  const [study, setStudy] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    const fetchStudy = async () => {
      if (!id) {
        console.error("No study ID provided");
        return;
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

  if (loading) return <Typography>Loading...</Typography>;
  if (error) return <Typography>Error loading study details.</Typography>;
  if (!study) return <Typography>No study data.</Typography>;

  const { title, doi, authors, keywords, abstract, experiments } = study;

  const renderExperimentDetails = (experiment) => (
    <Box sx={{ mb: 2, p: 2, border: '1px dashed grey' }}>
      <Typography variant="h6">Experiment Details:</Typography>
      {Object.keys(experiment).map(key => {
        if (key !== 'effects') { 
          return <Typography key={key}>{`${key}: ${experiment[key]}`}</Typography>;
        }
        return null;
      })}
      {experiment.effects && experiment.effects.map((effect, id) => renderEffectDetails(effect, id))}
    </Box>
  );

  const renderEffectDetails = (effect, index) => (
    <Box sx={{ mt: 2, ml: 4, p: 2, border: '1px solid lightgray' }} key={index}>
      <Typography variant="subtitle1">Effect {index + 1} Details:</Typography>
      {Object.keys(effect).map(key => (
        <Typography key={key}>{`${key}: ${effect[key]}`}</Typography>
      ))}
    </Box>
  );

  return (
    <Box sx={{ margin: 4 }}>
      <Typography variant="h4" gutterBottom>{title}</Typography>
      <Typography variant="subtitle1" gutterBottom>DOI: {doi}</Typography>
      <Typography variant="subtitle1" gutterBottom>Authors: {authors}</Typography>
      <Typography variant="subtitle2" gutterBottom>Keywords: {keywords}</Typography>
      <Typography variant="body1" align="left" gutterBottom>Abstract: {abstract}</Typography>
      {experiments && experiments.map(renderExperimentDetails)}
    </Box>
  );
};

export default DatabaseDetail;
