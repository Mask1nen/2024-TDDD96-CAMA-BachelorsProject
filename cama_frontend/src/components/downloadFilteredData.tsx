import React, { useState } from 'react';
import { Box, Button, TextField, MenuItem, FormControl, InputLabel, Select, Checkbox, FormControlLabel, FormGroup } from '@mui/material';
import { downloadFilteredData } from '../api/dataAPI';
import countries from '../assets/countries.json';

const categories = [
    { id: 1, name: 'STEM' },
    { id: 2, name: 'Language' },
    { id: 3, name: 'Mathematics' }
  ];
  const studyDesigns = [
    { id: 1, name: 'RCT' },
    { id: 2, name: 'QES' }
  ];
  const participantDesigns = [
    { id: 1, name: 'within' },
    { id: 2, name: 'between' },
    { id: 3, name: 'mixed' }
  ];
  const testTimes = [
    { id: 1, name: 'baseline(pre-test)' },
    { id: 2, name: 'post-test' },
    { id: 3, name: 'follow-up' }
  ];
  const effectSizeTypes = [
    { id: 1, name: 'SMD' },
    { id: 2, name: 'RR/OR' }
  ];
  
  const FilterAndDownload = () => {
      const [filters, setFilters] = useState({
          category: '',
          study_design: '',
          participant_design: '',
          test_time: '',
          effect_size_type: '',
      });
  
      const handleChange = (e: React.ChangeEvent<HTMLInputElement | { name?: string; value: unknown }>) => {
          setFilters({
              ...filters,
              [e.target.name]: e.target.value
          });
      };
  
      const handleCheckboxChange = (e: React.ChangeEvent<HTMLInputElement>) => {
          setFilters({
              ...filters,
              [e.target.name]: e.target.checked
          });
      };
  
      const handleDownload = async () => {
          await downloadFilteredData(filters);
      };
  
      return (
          <Box sx={{ padding: 4 }}>
              <FormControl fullWidth margin="normal">
                  <InputLabel>Category</InputLabel>
                  <Select
                      name="category"
                      value={filters.category}
                      onChange={handleChange}
                  >
                      {categories.map(category => (
                          <MenuItem key={category.id} value={category.id}>{category.name}</MenuItem>
                      ))}
                  </Select>
              </FormControl>
  
  
              <FormControl fullWidth margin="normal">
                  <InputLabel>Study Design</InputLabel>
                  <Select
                      name="study_design"
                      value={filters.study_design}
                      onChange={handleChange}
                  >
                      {studyDesigns.map(studyDesign => (
                          <MenuItem key={studyDesign.id} value={studyDesign.id}>{studyDesign.name}</MenuItem>
                      ))}
                  </Select>
              </FormControl>
  
              <FormControl fullWidth margin="normal">
                  <InputLabel>Participant Design</InputLabel>
                  <Select
                      name="participant_design"
                      value={filters.participant_design}
                      onChange={handleChange}
                  >
                      {participantDesigns.map(participantDesign => (
                          <MenuItem key={participantDesign.id} value={participantDesign.id}>{participantDesign.name}</MenuItem>
                      ))}
                  </Select>
              </FormControl>
  
              <FormControl fullWidth margin="normal">
                  <InputLabel>Test Time</InputLabel>
                  <Select
                      name="test_time"
                      value={filters.test_time}
                      onChange={handleChange}
                  >
                      {testTimes.map(testTime => (
                          <MenuItem key={testTime.id} value={testTime.id}>{testTime.name}</MenuItem>
                      ))}
                  </Select>
              </FormControl>
  
              <FormControl fullWidth margin="normal">
                  <InputLabel>Effect Size Type</InputLabel>
                  <Select
                      name="effect_size_type"
                      value={filters.effect_size_type}
                      onChange={handleChange}
                  >
                      {effectSizeTypes.map(effectSizeType => (
                          <MenuItem key={effectSizeType.id} value={effectSizeType.id}>{effectSizeType.name}</MenuItem>
                      ))}
                  </Select>
              </FormControl>
              <Button variant="contained" color="primary" onClick={handleDownload}>
                  Download CSV
              </Button>
          </Box>
      );
  };
  
  export default FilterAndDownload;