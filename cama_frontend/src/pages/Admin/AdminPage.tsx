import React, { useEffect, useState } from "react";
import {
  Box,
  Typography,
  Snackbar,
  Alert
} from "@mui/material";
import ApprovalCard from "./ApprovalCard";
import { fetchStudies, fetchFieldDefinitions, approveStudy } from "../../api/dataAPI";
import { Study } from "../../api/newTypes";

const AdminPage: React.FC = () => {
  const [studies, setStudies] = useState<Study[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);
  const [fieldData, setFieldData] = useState(null);
  const [successMessage, setSuccessMessage] = useState("");
  const [showSnackbar, setShowSnackbar] = useState(false);

  useEffect(() => {
    const loadStudies = async () => {
      const fetchedStudies = await fetchStudies();
      if (!fetchedStudies) {
        setLoading(false);
        setError(true);
        return;
      } else {
        const unapprovedStudies = fetchedStudies.filter(study => !study.approved);
        setStudies(unapprovedStudies);
        setLoading(false);
      }
    };
    loadStudies();

    const fetchStudyFields = async () => {
      const fieldData = await fetchFieldDefinitions();
      if (fieldData) {
        console.log("field data: ", fieldData);
        setFieldData(fieldData);
      } else {
        console.log("field data not found");
      }
    };
    fetchStudyFields();
  }, []);

  const handleApproval = async (studyId: number, studyTitle: string) => {
    try {
      const response = await approveStudy(studyId);
      if (response) {
        setStudies(prevStudies => prevStudies.filter(study => study.study_id !== studyId));
        setSuccessMessage(`Study "${studyTitle}" has been approved!`);
        setShowSnackbar(true);
      }
    } catch (error) {
      console.error("Error approving study:", error);
    }
  };

  const handleCloseSnackbar = () => {
    setShowSnackbar(false);
  };

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
        <ApprovalCard key={study.study_id} data={study} onApprove={handleApproval} />
      ))}

      <Snackbar open={showSnackbar} autoHideDuration={6000} onClose={handleCloseSnackbar}>
        <Alert onClose={handleCloseSnackbar} severity="success" sx={{ width: '100%' }}>
          {successMessage}
        </Alert>
      </Snackbar>
    </Box>
  );
};

export default AdminPage;
