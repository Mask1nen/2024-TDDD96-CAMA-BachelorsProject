import React, { useState, useEffect, useMemo } from 'react';
import { Box, Grid, Typography, Button, TextField, InputAdornment, Tooltip, Pagination, CircularProgress } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import ViewListIcon from '@mui/icons-material/ViewList';
import ViewModuleIcon from '@mui/icons-material/ViewModule';
import NewReleasesIcon from '@mui/icons-material/NewReleases';
import StudyCard from './StudyCard';
import Slider from 'react-slick';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import { fetchStudies } from '../../api/dataAPI';
import FilterAndDownload from '../../components/downloadFilteredData';

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
  const [loading, setLoading] = useState(true); // Loading state
  const [displayMode, setDisplayMode] = useState("default"); // Toggle between 'default' and 'all'
  const [viewMode, setViewMode] = useState("grid"); // Toggle between 'grid' and 'list'
  const [currentPage, setCurrentPage] = useState(1);
  const [searchQuery, setSearchQuery] = useState("");

  const itemsPerPage = viewMode === "grid" ? 12 : 25;

  useEffect(() => {
    const loadStudies = async () => {
      setLoading(true);
      const fetchedStudies = await fetchStudies();
      if (fetchedStudies) {
        setStudies(fetchedStudies);
      } else {
        console.error('Error fetching studies or no data returned');
      }
      setLoading(false);
    };
    loadStudies();
  }, []);

  const handleSeeAllClick = () => setDisplayMode("all");
  const toggleViewMode = () => setViewMode(viewMode === "grid" ? "list" : "grid");

  const handleSearch = (query: string) => {
    setSearchQuery(query);
  };

  const filteredData = studies.filter((item) =>
    item.title.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const totalPages = useMemo(() => {
    return Math.ceil(filteredData.length / itemsPerPage);
  }, [filteredData, itemsPerPage]);

  const latestDatasets = filteredData.slice(-8);

  return (
    <Box sx={{ px: 4 }}>
      <Typography variant="h4" gutterBottom>
        Download Filtered Data
      </Typography>
      <FilterAndDownload />
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

      {loading ? (
        <Box display="flex" justifyContent="center" alignItems="center" minHeight="80vh">
          <CircularProgress />
        </Box>
      ) : (
        <>
          {displayMode === "default" && (
            <>
              <Grid
                container
                justifyContent="space-between"
                alignItems="center"
                marginBottom={4}
              >
                
                
              </Grid>
            

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
                {latestDatasets.map((study, index) => (
                  <Box key={index} padding={1}>
                    <StudyCard studyData={study} />
                  </Box>
                ))}
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
                  {filteredData
                    .slice(
                      (currentPage - 1) * itemsPerPage,
                      currentPage * itemsPerPage
                    )
                    .map((study, index) => (
                      <StudyCard key={index} studyData={study} />
                    ))}
                </Box>
              ) : (
                <Box sx={{ display: "flex", flexDirection: "column" }}>
                  {filteredData
                    .slice(
                      (currentPage - 1) * itemsPerPage,
                      currentPage * itemsPerPage
                    )
                    .map((study, index) => (
                      <StudyCard key={index} studyData={study} />
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
        </>
      )}
    </Box>
  );
};

export default DatabasePage;
