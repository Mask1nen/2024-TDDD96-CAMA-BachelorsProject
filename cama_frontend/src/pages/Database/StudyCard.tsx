import React from "react";
import {
  Card,
  CardContent,
  CardMedia,
  Typography,
  Box,
  Tooltip
} from "@mui/material";
import { Study } from "../../api/newTypes";
import { useNavigate } from "react-router-dom";
import getImage from "./GetImage";

interface StudyCardProps {
  studyData: Study;
}
const StudyCard: React.FC<StudyCardProps> = ({ studyData }) => {
  let navigate = useNavigate();



  const handleCardClick = () => {
    navigate(`/Database/${studyData.study_id}`);
};
const image1 = getImage(studyData.study_id);



  return (
    <Box
      sx={{
        width: "100%",
        marginBottom: 2,
        transition: "transform 0.3s",
        "&:hover": { transform: "scale(1.05)" },
      }}
    >
        <Tooltip title={studyData.title} placement="top">
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
            image={studyData.image || image1}
            alt={studyData.title}
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
              {studyData.title}
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
              {studyData.authors}
            </Typography>
          </CardContent>
        </Card>
        </Tooltip>
    </Box>
  );
};

export default StudyCard;
