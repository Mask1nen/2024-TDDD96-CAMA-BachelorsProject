import React from "react";
import { useParams } from "react-router-dom";
import { Box, Typography, TableContainer, Paper } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import data from "../../data/randomized_data.json";
import bild2 from "../../assets/images/bild2.png";

const DatasetDetail = () => {
  let { titleSlug } = useParams();
  const title = decodeURIComponent(titleSlug || "");
  const matchingEntries = data.filter((d) => d.title === title);

  if (!matchingEntries.length) {
    return <div>Dataset not found.</div>;
  }

  const { authors, keywords, abstract, doi } = matchingEntries[0];

  const columns = [
    { field: "id", headerName: "ID", width: 90 },
    { field: "category", headerName: "Category", width: 130 },
    { field: "country", headerName: "Country", width: 130 },
    { field: "year", headerName: "Year", width: 100 },
    { field: "peer_reviewed", headerName: "Peer Reviewed", width: 130 },
    { field: "experiment_number", headerName: "Experiment Number", width: 160 },
    {
      field: "effect_size_number",
      headerName: "Effect Size Number",
      width: 170,
    },
    { field: "mean_age", headerName: "Mean Age", width: 100 },
    { field: "grade", headerName: "Grade", width: 100 },
    { field: "ni", headerName: "NI", width: 100 },
    { field: "gender_1", headerName: "Gender 1", width: 130 },
    { field: "gender_2", headerName: "Gender 2", width: 130 },
    { field: "study_design", headerName: "Study Design", width: 130 },
    {
      field: "participant_design",
      headerName: "Participant Design",
      width: 170,
    },
    { field: "implementation", headerName: "Implementation", width: 130 },
    { field: "duration_week", headerName: "Duration Week", width: 130 },
    { field: "frequency_n", headerName: "Frequency N", width: 130 },
    { field: "intensity_n", headerName: "Intensity N", width: 130 },
    { field: "m1i", headerName: "M1I", width: 100 },
    { field: "sd1i", headerName: "SD1I", width: 100 },
    { field: "n1i", headerName: "N1I", width: 100 },
    { field: "m2i", headerName: "M2I", width: 100 },
    { field: "sd2i", headerName: "SD2I", width: 100 },
    { field: "n2i", headerName: "N2I", width: 100 },
    { field: "icc", headerName: "ICC", width: 100 },
    { field: "ai", headerName: "AI", width: 100 },
    { field: "bi", headerName: "BI", width: 100 },
    { field: "ci", headerName: "CI", width: 100 },
    { field: "di", headerName: "DI", width: 100 },
    { field: "ri", headerName: "RI", width: 100 },
    { field: "ni__1", headerName: "NI_1", width: 100 },
    { field: "t", headerName: "T", width: 100 },
    { field: "f_stat", headerName: "F Stat", width: 100 },
    { field: "d", headerName: "D", width: 100 },
    { field: "d_var", headerName: "D Var", width: 100 },
    { field: "rob", headerName: "ROB", width: 100 },
    { field: "robins", headerName: "ROBINS", width: 100 },
    { field: "outcome", headerName: "Outcome", width: 130 },
    { field: "outcome_full", headerName: "Outcome Full", width: 130 },
  ];

  const rows = matchingEntries.map((entry, index) => ({
    id: index,
    title: entry.title,
    authors: entry.authors,
    keywords: entry.keywords,
    abstract: entry.abstract,
    category: entry.category,
    country: entry.country,
    year: entry.year,
    doi: entry.doi,
    peer_reviewed: entry.peer_reviewed,
    experiment_number: entry.experiment_number,
    effect_size_number: entry.effect_size_number,
    mean_age: entry.mean_age,
    grade: entry.grade,
    ni: entry.ni,
    gender_1: entry.gender_1,
    gender_2: entry.gender_2,
    study_design: entry.study_design,
    participant_design: entry.participant_design,
    implementation: entry.implementation,
    duration_week: entry.duration_week,
    frequency_n: entry.frequency_n,
    intensity_n: entry.intensity_n,
    m1i: entry.m1i,
    sd1i: entry.sd1i,
    n1i: entry.n1i,
    m2i: entry.m2i,
    sd2i: entry.sd2i,
    n2i: entry.n2i,
    icc: entry.icc,
    ai: entry.ai,
    bi: entry.bi,
    ci: entry.ci,
    di: entry.di,
    ri: entry.ri,
    ni__1: entry.ni__1,
    t: entry.t,
    f_stat: entry.f_stat,
    d: entry.d,
    d_var: entry.d_var,
    rob: entry.rob,
    robins: entry.robins,
    outcome: entry.outcome,
    outcome_full: entry.outcome_full,
    // Add other fields as necessary.
  }));

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

export default DatasetDetail;
