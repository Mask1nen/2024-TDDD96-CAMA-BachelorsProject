import React from "react";
import {
  Card,
  CardActions,
  CardContent,
  CardMedia,
  Button,
  Typography,
  Box,
} from "@mui/material";
import { Link } from "react-router-dom";
import { DataEntry } from "../types/dataType"; // Adjust the import path as necessary
import rawData from "../data/data.json";
import bild2 from "../assets/images/bild2.png";

const data: DataEntry[] = rawData as unknown as DataEntry[];
interface DatasetCardProps {
  data: DataEntry;
}

const DatasetCard: React.FC<DatasetCardProps> = ({ data }) => {
  return (
    <Box
      sx={{
        width: "100%",
        marginBottom: 2,
        transition: "transform 0.3s",
        "&:hover": { transform: "scale(1.05)" },
      }}
    >
      <Link to={data.to || "#!"}  style={{ textDecoration: "none" }}>
        <Card
          sx={{
            minWidth: 240,
            maxWidth: 320,
            margin: "auto",
            maxHeight: "100%",
            boxShadow:
              "0 2px 4px -2px rgba(0,0,0,0.24), 0 4px 24px -2px rgba(0, 0, 0, 0.2)",
          }}
        >
          <CardMedia
            component="img"
            image={data.image || bild2} // Provide a default or a placeholder
            alt={data.title}
            sx={{ width: "100%", height: "auto" }}
          />
          <CardContent>
            <Typography variant="h6" component="div" gutterBottom>
              {data.title}
            </Typography>
            <Typography variant="body2" color="text.secondary" gutterBottom>
              {data.authors}
            </Typography>
          </CardContent>
          <CardActions sx={{ justifyContent: "center" }}>
            <Button size="small" variant="contained" color="primary">
              Learn More
            </Button>
          </CardActions>
        </Card>
      </Link>
    </Box>
  );
};

export default DatasetCard;
