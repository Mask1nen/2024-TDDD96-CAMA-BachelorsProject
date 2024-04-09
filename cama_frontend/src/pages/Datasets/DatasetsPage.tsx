import React from "react";
import { Grid, Paper, Box, Typography, Button, colors } from "@mui/material";
import DatasetCard from "../../components/DatasetCard";
import bild2 from "../../assets/images/bild2.png";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import TrendingUpIcon from "@mui/icons-material/TrendingUp";
import data from "../../data/data.json";
import { DataEntry } from "../../types/dataType";
import { useNavigate } from "react-router-dom";

const settings = {
  dots: true,
  infinite: false,
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
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2,
        infinite: true,
        dots: true,
      },
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


const DatasetsPage: React.FC = () => {
  let navigate = useNavigate(); // Initialize useHistory hook

    // Handler for the "See All" button click
    const handleSeeAllClick = () => {
      // Placeholder for navigation logic
      // For example, navigate to the route showing all datasets in list view
      // history.push('/datasets/all');
      console.log("See All clicked. Implement navigation to the list view.");
    };
    return (
      <Box sx={{ padding: "2rem", bgcolor: "#f0f0f0" }}>
        <Grid container justifyContent="space-between" alignItems="center">
          <Grid item>
            <Typography variant="h5" color="primary" component="h1" sx={{ display: "inline", mr: 1 }}>
              Trending Datasets
            </Typography>
            <TrendingUpIcon color="primary" fontSize="large" sx={{ verticalAlign: "bottom", ml: 1 }} />
          </Grid>
          <Grid item>
            <Button variant="text" onClick={handleSeeAllClick}>See All</Button>
          </Grid>
        </Grid>
        <Slider {...settings}>
          {data.slice(0, 8).map((entry: DataEntry, index: number) => ( // Only map through the first 8 items
            <Box key={index} sx={{ padding: 1 }}>
              <DatasetCard data={entry} />
            </Box>
          ))}
        </Slider>
      </Box>
    );
  };

export default DatasetsPage;
