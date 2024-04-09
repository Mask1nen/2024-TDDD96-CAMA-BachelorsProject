import React from 'react';
import { Card, CardActions, CardContent, CardMedia, Button, Typography } from '@mui/material';
import { Link } from 'react-router-dom';

interface DatasetCardProps {
  to: string;
  image: string;
  heading: string;
  description: string;
  content: string;
}

const DatasetCard: React.FC<DatasetCardProps> = ({ to, image, heading, description, content }) => {
  return (
    <div className="w-full sm:w-1/2 md:w-1/3 px-4 mb-4 transition-transform transform hover:scale-105 duration-300">
      <Link to={to}>
        <Card
          sx={{
            minWidth: 240,
            maxWidth: 320,
            m: 4,
            maxHeight: "100%",
            boxShadow: "0 2px 4px -2px rgba(0,0,0,0.24), 0 4px 24px -2px rgba(0, 0, 0, 0.2)",
          }}
        >
          <CardMedia
            image={image}
            sx={{
              width: "100%",
              height: 0,
              paddingBottom: "min(60%, 200px)",
              bgcolor: "rgba(0, 0, 0, 0.08)",
            }}
          />
          <CardContent>
            <Typography variant="h4" component="div">
              {heading}
            </Typography>
            <Typography sx={{ mb: 1.5 }} color="text.secondary">
              {description}
            </Typography>
            <Typography variant="body1">
              {content}
            </Typography>
          </CardContent>
          <CardActions style={{ justifyContent: "center" }}>
            <Button size="small" variant="contained" color="primary">Learn More</Button>
          </CardActions>
        </Card>
      </Link>
    </div>
  );
};

export default DatasetCard;