import React, { useState, useMemo } from "react";
import {
  Grid,
  Box,
  Typography,
  Button,
  Pagination,
  TextField,
  InputAdornment,
  Tooltip,
} from "@mui/material";
import DatasetCard from "../../components/DatasetCard";
import ListViewCard from "../../components/ListViewCard";
import bild2 from "../../assets/images/bild2.png";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import TrendingUpIcon from "@mui/icons-material/TrendingUp";
import NewReleasesIcon from "@mui/icons-material/NewReleases";
import SearchIcon from "@mui/icons-material/Search";
import data from "../../data/randomized_data.json";
import { DataEntry } from "../../api/types";
import { useNavigate } from "react-router-dom";
import ViewListIcon from "@mui/icons-material/ViewList";
import ViewModuleIcon from "@mui/icons-material/ViewModule";

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
  const [searchQuery, setSearchQuery] = useState("");

  const itemsPerPage = viewMode === "grid" ? 23 : 25;
  const handleSeeAllClick = () => setDisplayMode("all");
  const toggleViewMode = () =>
    setViewMode(viewMode === "grid" ? "list" : "grid");

  const handleSearch = (query: string) => {
    setSearchQuery(query);
  };
  const filteredData = data.filter((item) =>
    item.title.toLowerCase().includes(searchQuery.toLowerCase())
  );

  // Use useMemo to efficiently compute filtered titles based on the search query
  const filteredTitles = useMemo(() => {
    const titles = data
      .filter((item) =>
        item.title.toLowerCase().includes(searchQuery.toLowerCase())
      )
      .map((item) => item.title);
    return [...new Set(titles)];
  }, [searchQuery]);

  // Use useMemo to compute the total pages based on filtered titles
  const totalPages = useMemo(() => {
    return Math.ceil(filteredTitles.length / itemsPerPage);
  }, [filteredTitles, itemsPerPage]);

  const trendingDatasets = filteredTitles.slice(0, 8);
  const latestDatasets = filteredTitles.slice(-8);

  return (
    <Box sx={{ px: 4 }}>
      {displayMode === "default" && (
        <>
          <Grid
            container
            justifyContent="space-between"
            alignItems="center"
            marginBottom={4}
          >
            <Typography variant="h5" color="primary" component="h1">
              Trending Datasets <TrendingUpIcon color="primary" />
            </Typography>
            <Button variant="text" onClick={handleSeeAllClick}>
              See All
            </Button>
          </Grid>
          <Slider {...sliderSettings}>
            {trendingDatasets.map((title, index) => {
             
                const datasetEntry = data.find(item => item.title === title);
              return datasetEntry ? (
                <Box key={index} padding={1}>
                  <DatasetCard data={datasetEntry} />
                </Box>
              ) : null;
            })}
          </Slider>

          <Grid
            container
            justifyContent="space-between"
            alignItems="center"
            marginTop={4}
          >
            <Typography variant="h5" color="primary" component="h1">
              Latest Datasets <NewReleasesIcon color="primary" />
            </Typography>
            <Button variant="text" onClick={handleSeeAllClick}>
              See All
            </Button>
          </Grid>
          <Slider {...sliderSettings}>
            {latestDatasets.map((title, index) => {
              
             
                const datasetEntry = data.find(item => item.title === title);
              return datasetEntry ? (
                <Box key={index} padding={1}>
                  <DatasetCard data={datasetEntry} />
                </Box>
              ) : null;
            })}
          </Slider>
        </>
      )}

      {displayMode === "all" && (
        <>
          <TextField
            fullWidth
            style={{
              marginBottom: 40,
              maxWidth: 800,
              backgroundColor: "white",
            }}
            onChange={(e) => handleSearch(e.target.value)}
            placeholder="Search datasets..."
            InputProps={{
              endAdornment: (
                <InputAdornment position="end">
                  <SearchIcon />
                </InputAdornment>
              ),
            }}
          />
          <Tooltip
            title={
              viewMode === "grid"
                ? "Switch to List View"
                : "Switch to Grid View"
            }
          >
            <Button
              variant="text"
              onClick={toggleViewMode}
              sx={{ minWidth: "auto", marginLeft: 12 }}
            >
              {viewMode === "grid" ? <ViewListIcon /> : <ViewModuleIcon />}
            </Button>
          </Tooltip>

          {viewMode === "grid" ? (
            <Box
              sx={{
                display: "grid",
                gridTemplateColumns: "repeat(3, 1fr)",
                gap: 2,
              }}
            >
              {filteredTitles
                .slice(
                  (currentPage - 1) * itemsPerPage,
                  currentPage * itemsPerPage
                )
                .map((title, index) => {
                  const entry = data.find((item) => item.title === title);
                  return entry && <DatasetCard key={index} data={entry} />;
                })}
            </Box>
          ) : (
            <Box sx={{ display: "flex", flexDirection: "column" }}>
              {filteredTitles
                .slice(
                  (currentPage - 1) * itemsPerPage,
                  currentPage * itemsPerPage
                )
                .map((title, index) => {
                  const entry = data.find((item) => item.title === title);
                  return entry && <ListViewCard key={index} data={entry} />;
                })}
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
