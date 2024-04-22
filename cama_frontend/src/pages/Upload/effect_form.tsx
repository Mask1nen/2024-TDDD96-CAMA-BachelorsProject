import React, { useState } from 'react';
import { 
  Box, Button, Accordion, AccordionSummary, AccordionDetails, Typography, 
  FormControl, TextField, MenuItem, Input, InputLabel, InputAdornment 
} from '@mui/material';
import { ArrowDownward } from '@mui/icons-material';
import { blueGrey } from '@mui/material/colors';
import { effectFields } from './effectFields'; // Make sure the import path is correct

const EffectForm: React.FC = (props) => {
  const [inputs, setInputs] = useState<Record<string, string>>({});


  return (
    <Box sx={{ mt: 3 }}>
      <Accordion sx={{ backgroundColor: blueGrey['A100'] }}>
        <AccordionSummary expandIcon={<ArrowDownward />} aria-controls="panel1-content" id="panel1-header">
          <Typography>Effect Data</Typography>
        </AccordionSummary>
        <AccordionDetails>
            {effectFields.map(field => (
              <FormControl key={field.key} sx={{ width: field.type === 'option' ? '30%' : '23%', mt: 1, ml: 1 }} variant="standard">
                {field.type === 'option' ? (
                  <TextField
                    id={"form" + field.key}
                    label={field.name}
                    name={field.key}
                    select
                    value={props.inputs[field.key] ?? ""}
                    onChange={(e) => {props.onChange(e, props.experimentId, props.effectId)}}
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
                    value={props.inputs[field.key] ?? ""}
                    onChange={(e) => {props.onChange(e, props.experimentId, props.effectId)}}
                    fullWidth
                    InputProps={{
                      endAdornment: field.type === 'percent' ? <InputAdornment position="end">%</InputAdornment> : null
                    }}
                  />
                )}
              </FormControl>
            ))}
        </AccordionDetails>
      </Accordion>
    </Box>
  );
};

export default EffectForm;
