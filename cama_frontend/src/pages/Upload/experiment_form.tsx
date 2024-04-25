import React, { useState } from "react";
import { Tooltip, Box, Button, Accordion, AccordionSummary, AccordionDetails, Typography, FormControl, TextField, MenuItem, Input, InputLabel, InputAdornment } from "@mui/material";
import { ArrowDownward, AddCircleOutline, RemoveCircleOutline } from "@mui/icons-material";
import { experimentFields } from "./experimentFields";
import  EffectForm  from "./effect_form";
import { Effect } from '../../api/newTypes'

const ExperimentForm: React.FC = ({inputs, onChange, experimentId, onChangeEffect, removeEffect, addEffect, effects, readOnly}: any) => {

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
                                    name={field.key}
                                    select={!!field.options}
                                    value={inputs[field.key] || ""}
                                    onChange={(e) => {onChange(e, experimentId)}}
                                >
                                    {field.options?.map(option => (
                                        <MenuItem key={`${field.key}-${option}`} value={option}>
                                            {option}
                                        </MenuItem>
                                    ))}
                                </TextField>
                            </Tooltip>
                        ))}
                    {effects.map((effect: Effect) => (
                        <div key={effect.id}>
                            {effect.experiment_id == experimentId ? (
                            <Box key={effect.id} >
                                <EffectForm 
                                    readOnly={readOnly}
                                    onChange={onChangeEffect} 
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
