import React, { useState } from 'react';
import { 
  Box, Button, Accordion, AccordionSummary, AccordionDetails, Typography, 
  FormControl, TextField, MenuItem, Input, InputLabel, InputAdornment 
} from '@mui/material';
import { ArrowDownward } from '@mui/icons-material';
import { blueGrey } from '@mui/material/colors';
import { effectFields } from './effectFields'; // Make sure the import path is correct

const EffectForm: React.FC = () => {
  const [inputs, setInputs] = useState<Record<string, string>>({});

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setInputs(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    console.log(inputs);
  };

  return (
    <Box sx={{ mt: 3 }}>
      <Accordion sx={{ backgroundColor: blueGrey['A100'] }}>
        <AccordionSummary expandIcon={<ArrowDownward />} aria-controls="panel1-content" id="panel1-header">
          <Typography>Effect Data</Typography>
        </AccordionSummary>
        <AccordionDetails>
          <form onSubmit={handleSubmit}>
            {effectFields.map(field => (
              <FormControl key={field.key} sx={{ width: field.type === 'option' ? '30%' : '23%', mt: 2, ml: 1 }} variant="standard">
                {field.type === 'option' ? (
                  <TextField
                    id={"form" + field.key}
                    label={field.name}
                    name={field.key}
                    select
                    value={inputs[field.key] || ""}
                    onChange={handleChange}
                    fullWidth
                  >
                    {field.options?.map(option => (
                      <MenuItem key={`${field.key}-${option}`} value={option}>
                        {option}
                      </MenuItem>
                    ))}
                  </TextField>
                ) : (
                  <TextField
                    id={"form" + field.key}
                    label={field.name}
                    name={field.key}
                    value={inputs[field.key] || ""}
                    onChange={handleChange}
                    fullWidth
                    InputProps={{
                      endAdornment: field.type === 'percent' ? <InputAdornment position="end">%</InputAdornment> : null
                    }}
                  />
                )}
              </FormControl>
            ))}
          </form>
        </AccordionDetails>
      </Accordion>
    </Box>
  );
};

export default EffectForm;
