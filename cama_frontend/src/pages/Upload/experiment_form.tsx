import React, { useState } from "react";
import { Box, Button, Accordion, AccordionSummary, AccordionDetails, Typography, FormControl, TextField, MenuItem, Input, InputLabel, InputAdornment } from "@mui/material";
import { ArrowDownward, AddCircleOutline, RemoveCircleOutline } from "@mui/icons-material";
import { experimentFields } from "./experimentFields";
import  EffectForm  from "./effect_form";
import { Effect } from '../../api/newTypes'

const ExperimentForm: React.FC = ({inputs, onChange, experimentId, onChangeEffect, removeEffect, addEffect, effects}: any) => {

    return (
        <Box sx={{ width: "90%", borderLeft: 4, mt: 5, pl: 3 }}>
            <Accordion>
                <AccordionSummary expandIcon={<ArrowDownward />} aria-controls="panel1-content" id="panel1-header">
                    <Typography>Experiment Data</Typography>
                </AccordionSummary>
                <AccordionDetails>
                        {experimentFields.map(field => (
                            <FormControl key={field.key} sx={{ width: "30%", mt: 1, ml: 1 }} variant="standard">
								<TextField
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
                            </FormControl>
                        ))}
                    {effects.map((effect: Effect) => (
                        <div key={effect.id}>
                            {effect.experiment_id == experimentId ? (
                            <Box key={effect.id}>
                                <EffectForm 
                                    onChange={onChangeEffect} 
                                    inputs={effect} 
                                    experimentId={experimentId} 
                                    effectId={effect.id}/>

                                <Button onClick={() => removeEffect(effect.id, effect.experiment_id)} variant="outlined" startIcon={<RemoveCircleOutline />}>
                                    Remove Effect
                                </Button>
                            </Box>
                            ): ""}
                        </div>
                    ))}
                    <Button onClick={() => {addEffect(experimentId)}} variant="outlined" sx={{ mt: 2 }}>
                        Add Effect<AddCircleOutline sx={{ ml: 1 }} />
                    </Button>
                </AccordionDetails>
            </Accordion>
        </Box>
    );
};

export default ExperimentForm;
