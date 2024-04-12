import React from "react";
import { Grid, Paper, Box, Typography, Button, colors } from "@mui/material";
import DatasetCard from "../../components/DatasetCard";
import bild2 from "../../assets/images/bild2.png";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import TrendingUpIcon from "@mui/icons-material/TrendingUp";

interface Dataset {
  to: string;
  image: string;
  heading: string;
  description: string;
  content: string;
}

interface TrendingDatasetsProps {
  datasets: Dataset[];
}

const datasets: Dataset[] = [
  {
    to: "/dataset/1",
    image: bild2,
    heading: "Dataset 1",
    description: "This is a description",
    content: "This is the content",
  },
  {
    to: "/dataset/2",
    image: bild2,
    heading: "Dataset 2",
    description: "This is a description",
    content: "This is the content",
  },
  {
    to: "/dataset/3",
    image: bild2,
    heading: "Dataset 3",
    description: "This is a description",
    content: "This is the content",
  },
  {
    to: "/dataset/3",
    image: bild2,
    heading: "Dataset 3",
    description: "This is a description",
    content: "This is the content",
  },
  {
    to: "/dataset/3",
    image: bild2,
    heading: "Dataset 3",
    description: "This is a description",
    content: "This is the content",
  },
  {
    to: "/dataset/3",
    image: bild2,
    heading: "Dataset 3",
    description: "This is a description",
    content: "This is the content",
  },
];

const settings = {
  dots: true,
  infinite: false,
  speed: 500,
  slidesToShow: 4, // Default for large screens
  slidesToScroll: 4,
  responsive: [
    {
      breakpoint: 1280, // Considered as 'lg' in Tailwind
      settings: {
        slidesToShow: 3,
        slidesToScroll: 3,
      },
    },
    {
      breakpoint: 1024, // Considered as 'md' in Tailwind
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2,
        infinite: true,
        dots: true,
      },
    },
    {
      breakpoint: 768, // Considered as 'sm' in Tailwind
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2,
      },
    },
    {
      breakpoint: 640, // Considered as 'xs' in Tailwind
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
      },
    },
  ],
};

const DatasetsPage: React.FC = () => {
  return (
    <Box sx={{ padding: "2rem", bgcolor: "#f0f0f0" }}>
      <Grid container justifyContent="space-between" alignItems="center" >
        <Grid item >
          <Typography
            variant="h5"
            color="primary"
            component="h1"
            sx={{ display: "inline", mr:1}}
            
          >
            Trending Datasets
          </Typography>
          <TrendingUpIcon
            color="primary"
            fontSize="large"
            sx={{ verticalAlign: "bottom", ml:1}}
          />
        </Grid>
        <Grid item>
          <Button variant="text">See All</Button>
        </Grid>
      </Grid>
      <Slider {...settings}>
        {datasets.map((dataset: Dataset, index: number) => (
          <div key={index}>
            <DatasetCard
              to={dataset.to}
              image={dataset.image}
              heading={dataset.heading}
              description={dataset.description}
              content={dataset.content}
            />
          </div>
        ))}
      </Slider>
    </Box>
  );
};
export default DatasetsPage;
