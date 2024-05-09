import React, { useState } from 'react';
import { 
  Box, Button, Accordion, AccordionSummary, AccordionDetails, Typography, 
  FormControl, TextField, MenuItem, Input, InputLabel, InputAdornment 
} from '@mui/material';
import { ArrowDownward } from '@mui/icons-material';
import { blueGrey } from '@mui/material/colors';
import { effectFields } from './effectFields'; // Make sure the import path is correct

const EffectForm: React.FC = ({inputs, experiment_nr, effect_size_number, readOnly}: any) => {
  
  const disabledStyling = {
		"& .MuiInputBase-input.Mui-disabled": {
			  WebkitTextFillColor: "#010101",
		  },
	  };

  return (
    <Box sx={{ mt: 3 }}>
      <Accordion sx={{ backgroundColor: blueGrey['A100'] }}>
        <AccordionSummary expandIcon={<ArrowDownward />} aria-controls="panel1-content" id="panel1-header">
          <Typography>Effect Data</Typography>
        </AccordionSummary>
        <AccordionDetails>
            {effectFields.map(field => (
                  <TextField
                    disabled={(readOnly||false)}
                    key={field.key} 
                    sx={{ width: '23%', mt: 1, ml: 1, ...disabledStyling}}
                    variant="standard"
                    id={"form" + field.key}
                    label={field.name}
                    name={experiment_nr +"_"+ effect_size_number +"_"+ field.key}
                    select={!!field.options}
                    defaultValue={inputs[field.key]||""}
                    fullWidth
                  >
                    {field.options?.map(option => (
                      <MenuItem key={`${field.key}-${option}`} value={option}>
                        {option}
                      </MenuItem>
                    ))}
                  </TextField>
            ))}
        </AccordionDetails>
      </Accordion>
    </Box>
  );
};

export default EffectForm;
