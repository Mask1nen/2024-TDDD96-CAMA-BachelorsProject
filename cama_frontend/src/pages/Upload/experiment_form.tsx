import React, { useState } from "react";
import { Tooltip, Box, Button, Accordion, AccordionSummary, AccordionDetails, Typography, FormControl, TextField, MenuItem, Input, InputLabel, InputAdornment } from "@mui/material";
import { ArrowDownward, AddCircleOutline, RemoveCircleOutline } from "@mui/icons-material";
import { experimentFields } from "./experimentFields";
import  EffectForm  from "./effect_form";
import { Effect } from '../../api/newTypes'

const ExperimentForm: React.FC = ({experimentId, onChangeEffect, removeEffect, addEffect, effects, readOnly, inputs}: any) => {

    const disabledStyling = {
		"& .MuiInputBase-input.Mui-disabled": {
			WebkitTextFillColor: "#010101",
		  },
	  };

    return (
        <Box sx={{ width: "90%", borderLeft: 4, mt: 5, pl: 3 }}>
            <Accordion>
                <AccordionSummary expandIcon={<ArrowDownward />} aria-controls="panel1-content" id="panel1-header">
                    <Typography>Experiment Data</Typography>
                </AccordionSummary>
                <AccordionDetails>
                        {experimentFields.map(field => (
                            <Tooltip title={field.desc} key={field.key}>
                                <TextField
                                    disabled={(readOnly||false)}
                                    sx={{ width: "30%", mt: 1, ml: 1, ...disabledStyling}}
                                    variant="standard"
                                    id={"form" + field.key}
                                    label={field.name}
                                    name={experimentId +"_"+ field.key}
                                    select={!!field.options}
                                    defaultValue={inputs[field.key]||""}
                                >
                                    {field.options?.map(option => (
                                        <MenuItem key={`${field.key}-${option}`} value={option}>
                                            {option}
                                        </MenuItem>
                                    ))}
                                </TextField>
                            </Tooltip>
                        ))}
                    {effects.map((effect: {id: string, experiment_id:string}) => (
                        <div key={effect.id}>
                            {effect.experiment_id == experimentId ? (
                            <Box key={effect.id} >
                                <EffectForm 
                                    readOnly={readOnly}
                                    inputs={effect} 
                                    experimentId={experimentId} 
                                    effectId={effect.id}/>
                                {(!readOnly) ?(
                                    <Button sx={{mt:1}} size='small' onClick={() => removeEffect(effect.id, effect.experiment_id)} variant="outlined" startIcon={<RemoveCircleOutline />}>
                                        Remove Effect
                                    </Button>
                                ):""
                                }
                            </Box>
                            ): ""}
                        </div>
                    ))}
                    {(!readOnly) ?(

                        <Button onClick={() => {addEffect(experimentId)}} variant="outlined" sx={{ mt: 2 }}>
                          Add Effect<AddCircleOutline sx={{ ml: 1 }} />
                        </Button>
                    ):""
                    }
                </AccordionDetails>
            </Accordion>
        </Box>
    );
};

export default ExperimentForm;
