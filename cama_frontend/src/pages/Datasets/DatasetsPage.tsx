import React, { useState } from "react";
import { Grid, Box, Typography, Button, Pagination } from "@mui/material";
import DatasetCard from "../../components/DatasetCard";
import ListViewCard from "../../components/ListViewCard";
import bild2 from "../../assets/images/bild2.png";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import TrendingUpIcon from "@mui/icons-material/TrendingUp";
import NewReleasesIcon from "@mui/icons-material/NewReleases";
import data from "../../data/randomized_data.json";
import { DataEntry } from "../../types/dataType";
import { useNavigate } from "react-router-dom";

const sliderSettings = {
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

const DatasetsPage = () => {
  const [displayMode, setDisplayMode] = useState("default"); // Toggle between 'default' and 'all'
  const [viewMode, setViewMode] = useState("grid"); // Toggle between 'grid' and 'list'
  const [currentPage, setCurrentPage] = useState(1);

  const itemsPerPage = viewMode === "grid" ? 24 : 25;
  const totalPages = Math.ceil(data.length / itemsPerPage);
  const handleSeeAllClick = () => setDisplayMode("all");
  const toggleViewMode = () =>
    setViewMode(viewMode === "grid" ? "list" : "grid");
  const trendingDatasets = data.slice(0, 8);
  const latestDatasets = data.slice(-8);

  return (
    <Box sx={{ px:4 }}>
      {displayMode === "default" && (
        <>
          {/* Trending Datasets Section */}
          <Grid
            container
            justifyContent="space-between"
            alignItems="center"
            marginBottom={4}
          >
            <Typography variant="h5" color="primary" component="h1">
              Trending Datasets <TrendingUpIcon color="primary" />
            </Typography>
            <Button variant="text" onClick={() => handleSeeAllClick()}>
              See All
            </Button>
          </Grid>

          <Slider {...sliderSettings}>
            {trendingDatasets.map((entry, index) => (
              <Box key={index} padding={1}>
                <DatasetCard data={entry} />
              </Box>
            ))}
          </Slider>

          {/* Latest Datasets Section */}
          <Grid
            container
            justifyContent="space-between"
            alignItems="center"
            marginTop={4}
          >
            <Typography variant="h5" color="primary" component="h1">
              Latest Datasets <NewReleasesIcon color="primary" />
            </Typography>
            <Button variant="text" onClick={() => handleSeeAllClick()}>
              See All
            </Button>
          </Grid>
          <Slider {...sliderSettings}>
          {latestDatasets.map((entry, index) => (
            <Box key={index} padding={1}>
              <DatasetCard data={entry} />
            </Box>
          ))}
        </Slider>
        </>
      )}

      {displayMode === "all" && (
        // "All" view with Grid or List toggle and Pagination
        <>
          <Button variant="text" onClick={toggleViewMode}>
            {viewMode === "grid"
              ? "Switch to List View"
              : "Switch to Grid View"}
          </Button>

          {viewMode === "grid" ? (
            <Box
              sx={{
                display: "grid",
                gridTemplateColumns: "repeat(4, 1fr)",
                gap: 2,
              }}
            >
              {data
                .slice(
                  (currentPage - 1) * itemsPerPage,
                  currentPage * itemsPerPage
                )
                .map((entry, index) => (
                  <DatasetCard key={index} data={entry} />
                ))}
            </Box>
          ) : (
            <Box sx={{ display: "flex", flexDirection: "column" }}>
              {data
                .slice(
                  (currentPage - 1) * itemsPerPage,
                  currentPage * itemsPerPage
                )
                .map((entry, index) => (
                  <ListViewCard key={index} data={entry} />
                ))}
            </Box>
          )}

          <Pagination
            count={totalPages}
            page={currentPage}
            onChange={(event, newPage) => setCurrentPage(newPage)}
            sx={{ display: "flex", justifyContent: "center", marginTop: 2 }}
            color="primary"
          />
        </>
      )}
    </Box>
  );
};

export default DatasetsPage;
