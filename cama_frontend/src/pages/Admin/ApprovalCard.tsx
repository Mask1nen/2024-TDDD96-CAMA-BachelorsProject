import React from "react";
import { Card, CardContent, CardActions, Button, Typography, Box, Accordion, AccordionSummary, AccordionDetails } from "@mui/material";
import { useNavigate } from "react-router-dom";
import { DataEntry } from "../../api/types";
import { ArrowDownward, AddCircleOutline, RemoveCircleOutline } from "@mui/icons-material";
import Studyform from "../Upload/study_form";
import Experimentform from "../Upload/experiment_form";
import { approveStudy } from "../../api/dataAPI"

interface ApprovalCardProps {
  data: DataEntry;
}

const ApprovalCard: React.FC<ApprovalCardProps> = ({ data }) => {
  let navigate = useNavigate();

  const handleEdit = () => {
    navigate(`/edit/${data.id}`);
  };

  const handleApprove = () => {
    console.log("Approve", data.study_id);
    let response = approveStudy(data.study_id);
  };

  const handleReject = () => {
    console.log("Reject", data.id);
  };

  return (
    <Card sx={{ minWidth: 275, margin: 2, boxShadow: 3 }}>
      <CardContent>
        <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
          {data.title}
        </Typography>
        <Typography variant="h5" component="div">
          {data.authors}
        </Typography>
        <Typography sx={{ mb: 1.5 }} color="text.secondary">
          {data.year}
        </Typography>
        <Typography variant="body2">
          {data.abstract.substring(0, 100)}...
        </Typography>
		<Accordion>
                <AccordionSummary expandIcon={<ArrowDownward />} aria-controls="panel1-content" id="panel1-header">
                    <Typography>Show details</Typography>
                </AccordionSummary>
                <AccordionDetails>
					<Studyform onChange={() => {}} inputs={data} readOnly={true}/>
          {data.experiments.map(experiment => 

            							
								<Box key={experiment['id']}>
									<Experimentform 
										key={experiment['id']} 
                    readOnly={true}
										onChangeEffect={() => {}} 
										onChange={() => {}} 
										inputs={experiment} 
										effects={experiment.effects}
										addEffect={() => {}}
										removeEffect={() => {}}
										experimentId={experiment['id']}/>
								
								</Box>
            
            )}


                </AccordionDetails>
            </Accordion>


      </CardContent>
      <CardActions>
        <Button size="small" onClick={handleEdit}>Edit</Button>
        <Button size="small" onClick={handleApprove}>Approve</Button>
        <Button size="small" onClick={handleReject}>Reject</Button>
      </CardActions>
    </Card>
  );
};

export default ApprovalCard;
