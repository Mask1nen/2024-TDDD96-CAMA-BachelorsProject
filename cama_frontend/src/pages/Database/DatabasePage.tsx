import React, { useState, useEffect } from 'react';
import { Box, Grid, Typography } from '@mui/material';
import StudyCard from './StudyCard';
import Slider from 'react-slick';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import { fetchStudies } from '../../api/dataAPI';

const sliderSettings = {
  dots: true,
  infinite: true,
  speed: 500,
  slidesToShow: 4,
  slidesToScroll: 4,
  responsive: [
    {
      breakpoint: 1280,
      settings: { slidesToShow: 3, slidesToScroll: 3 },
    },
    {
      breakpoint: 1024,
      settings: { slidesToShow: 2, slidesToScroll: 2 },
    },
    {
      breakpoint: 768,
      settings: { slidesToShow: 2, slidesToScroll: 2 },
    },
    {
      breakpoint: 640,
      settings: { slidesToShow: 1, slidesToScroll: 1 },
    },
  ],
};

const DatabasePage = () => {
  const [studies, setStudies] = useState([]);

  useEffect(() => {
    const loadStudies = async () => {
        const fetchedStudies = await fetchStudies();
        if (fetchedStudies) {
            setStudies(fetchedStudies);
        } else {
            console.error('Error fetching studies or no data returned');
        }
    };
    loadStudies();
}, []);

  return (
    <Box sx={{ px: 4 }}>
      <Grid
        container
        justifyContent="space-between"
        alignItems="center"
        marginBottom={4}
      >
        <Typography variant="h5" color="primary" component="h1">
          Fetched studies
        </Typography>
      </Grid>
      <Slider {...sliderSettings}>
        {studies.map((study, index) => (
          <Box key={index} padding={1}>
            <StudyCard studyData={study} />
          </Box>
        ))}
      </Slider>
    </Box>
  );
};

export default DatabasePage;