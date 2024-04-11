import React from "react";
import {
  Card,
  CardActions,
  CardContent,
  CardMedia,
  Button,
  Typography,
  Box,
  Tooltip
} from "@mui/material";
import { Link } from "react-router-dom";
import { DataEntry } from "../api/types";
import rawData from "../data/data.json";
import bild2 from "../assets/images/bild2.png";
import { useNavigate } from "react-router-dom";

const data: DataEntry[] = rawData as unknown as DataEntry[];
interface DatasetCardProps {
  data: DataEntry;
}

const DatasetCard: React.FC<DatasetCardProps> = ({ data }) => {
  let navigate = useNavigate();

  const handleCardClick = () => {
    // Use a slug or encoded title for URL-safe navigation
    const titleSlug = encodeURIComponent(data.title);
    navigate(`/datasets/${titleSlug}`);
  };

  return (
    <Box
      sx={{
        width: "100%",
        marginBottom: 2,
        transition: "transform 0.3s",
        "&:hover": { transform: "scale(1.05)" },
      }}
    >
        <Tooltip title={data.title} placement="top">
        <Card
          sx={{
            minWidth: 240,
            maxWidth: 320,
            margin: "auto",
            maxHeight: "100%",
            boxShadow:
              "0 2px 4px -2px rgba(0,0,0,0.24), 0 4px 24px -2px rgba(0, 0, 0, 0.2)",
            
          }}
          onClick={handleCardClick}
        >
          <CardMedia
            component="img"
            image={data.image || bild2}
            alt={data.title}
            sx={{ width: "100%", height: "auto" }}
          />
          <CardContent>

            <Typography
              variant="h6"
              component="h2"
              noWrap
              sx={{
                width: "100%",
                overflow: "hidden",
                textOverflow: "ellipsis",
                whiteSpace: "nowrap",
              }}
            >
              {data.title}
            </Typography>
            <Typography
              variant="body2"
              color="text.secondary"
              sx={{
                width: "100%",
                overflow: "hidden",
                textOverflow: "ellipsis",
                whiteSpace: "nowrap",
              }}
            >
              {data.authors}
            </Typography>
          </CardContent>
          {/* <CardActions sx={{ justifyContent: "center" }}>
            <Button size="small" variant="contained" color="primary">
              Learn More
            </Button>
          </CardActions> */}
        </Card>
        </Tooltip>
    </Box>
  );
};

export default DatasetCard;
