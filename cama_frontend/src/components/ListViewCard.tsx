import React from "react";
import {
  Card,
  CardContent,
  CardMedia,
  Typography,
  Box,
} from "@mui/material";
import { Link } from "react-router-dom";
import { DataEntry } from "../api/types"; // Adjust the import path as necessary
import defaultImage from "../assets/images/bild2.png"; // Import the default image

interface ListViewCardProps {
  data: DataEntry;
}

const ListViewCard: React.FC<ListViewCardProps> = ({ data }) => {
  return (
    <Link to={data.to || "#!"} style={{ textDecoration: "none" }}>
      <Card sx={{ display: 'flex', width: '100%', mb: 2, transition: 'transform .3s', '&:hover': { transform: 'scale(1.05)' }, boxShadow: '0 2px 4px -2px rgba(0,0,0,.24), 0 4px 24px -2px rgba(0, 0, 0, .2)' }}>
        <CardMedia
          component="img"
          sx={{ width: 151, height: 'auto' }} // Adjust size to fit your design
          image={data.image || defaultImage}
          alt={data.title}
        />
        <Box sx={{ display: 'flex', flexDirection: 'column', flexGrow: 1 }}>
          <CardContent sx={{ flex: '1 0 auto' }}>
            <Typography variant="h6">{data.title}</Typography>
            <Typography variant="subtitle1" color="text.secondary">
              {data.authors}
            </Typography>
            {/* You can include more data fields here as needed */}
          </CardContent>
          {/* Optionally, include actions like buttons in CardActions if needed */}
        </Box>
      </Card>
    </Link>
  );
};

export default ListViewCard;
