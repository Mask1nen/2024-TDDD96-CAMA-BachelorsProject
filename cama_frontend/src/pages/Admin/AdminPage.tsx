import React, { useEffect, useState } from "react";
import {
  Box,
  Typography,
} from "@mui/material";
import ApprovalCard from "./ApprovalCard";
import { fetchStudies } from "../../api/dataAPI";
import { Study } from "../../api/newTypes";

const AdminPage: React.FC = () => {
  const [studies, setStudies] = useState<Study[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  


  useEffect(() => {
    const loadStudies = async () => {
        const fetchedStudies = await fetchStudies();
		if (!fetchedStudies) {
			setLoading(false);
			setError(true);
			return;
		} else{
		console.log(fetchedStudies);
		const unapprovedStudies = fetchedStudies?.filter(study=>!study.approved);
		setStudies(unapprovedStudies);
		setLoading(false);
		} 
    };
    loadStudies();
}, []);


  if (loading) return <Typography>Loading...</Typography>;
  if (error) return <Typography>Error loading studies.</Typography>;

  return (
    <Box sx={{ py: 2, pl: 2, textAlign: "left" }}>
      <Typography variant="h3" gutterBottom>
        Upload control
      </Typography>
      <Box sx={{ borderBottom: 1, borderColor: "divider", my: 1 }}></Box>

      <Typography variant="h5">Pending studies</Typography>
      {studies.map((study) => (
        <ApprovalCard key={study.study_id} data={study} />
      ))}
    </Box>
  );
};

export default AdminPage;
