import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import {
  Box,
  Typography,
  Card,
  CardContent,
  CardActions,
  Collapse,
  IconButton,
  Divider
} from "@mui/material";
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { styled } from '@mui/material/styles';
import { fetchStudyById } from "../../api/dataAPI";

const ExpandMore = styled((props) => {
  const { expand, ...other } = props;
  return <IconButton {...other} />;
})(({ theme, expand }) => ({
  transform: !expand ? 'rotate(0deg)' : 'rotate(180deg)',
  marginLeft: 'auto',
  transition: theme.transitions.create('transform', {
    duration: theme.transitions.duration.shortest,
  }),
}));

const DatabaseDetail = () => {
  const { id: paramId } = useParams();
  const id = paramId ? parseInt(paramId, 10) : null;
  const [study, setStudy] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);
  const [expanded, setExpanded] = useState({});

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

  const handleExpandClick = (index) => {
    setExpanded(prevExpanded => ({
      ...prevExpanded,
      [index]: !prevExpanded[index]
    }));
  };

  if (loading) return <Typography>Loading...</Typography>;
  if (error) return <Typography>Error loading study details.</Typography>;
  if (!study) return <Typography>No study data.</Typography>;

  const { title, doi, authors, keywords, abstract, experiments } = study;

  return (
    <Box sx={{ margin: 4, textAlign: "left" }}>
      <Card raised>
        <CardContent sx={{ borderLeft: 4 }}>
          <Typography variant="h4" gutterBottom>{title}</Typography>
          <Typography variant="subtitle1" gutterBottom>DOI: {doi}</Typography>
          <Typography variant="subtitle1" gutterBottom>Authors: {authors}</Typography>
          <Typography variant="subtitle2" gutterBottom>Keywords: {keywords}</Typography>
          <Typography variant="body1" align="left" gutterBottom>Abstract: {abstract}</Typography>
        </CardContent>
      </Card>
      {experiments.map((experiment, index) => (
        <Card key={index} sx={{ mt: 2 }}>
          <CardContent sx={{ borderLeft: 4 }}>
            <Typography variant="h6">Experiment Details:</Typography>
            {Object.keys(experiment).filter(key => key !== 'effects').map(key => (
              <Typography key={key}>{`${key}: ${experiment[key]}`}</Typography>
            ))}
          </CardContent>
          <CardActions>
            <ExpandMore
              expand={expanded[index]}
              onClick={() => handleExpandClick(index)}
              aria-expanded={expanded[index]}
              aria-label="show more"
            >
              <ExpandMoreIcon />
            </ExpandMore>
          </CardActions>
          <Collapse in={expanded[index]} timeout="auto" unmountOnExit>
            <CardContent sx={{ ml: 4, mb: 4, borderLeft: 4 }}>
              {experiment.effects.map((effect, effIndex) => (
                <Box key={effIndex} sx={{ ml: 4 }}>
                  <Typography variant="h6">Effect {effIndex + 1} Details:</Typography>
                  {Object.keys(effect).map(key => (
                    <Typography key={key}>{`${key}: ${effect[key]}`}</Typography>
                  ))}
                  {effIndex < experiment.effects.length - 1 && <Divider sx={{ my: 2 }} />}
                </Box>
              ))}
            </CardContent>
          </Collapse>
        </Card>
      ))}
    </Box>
  );
};

export default DatabaseDetail;
