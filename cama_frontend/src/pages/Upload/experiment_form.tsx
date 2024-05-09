import React, { useState } from "react";
import { Tooltip, Box, Button, Accordion, AccordionSummary, AccordionDetails, Typography, FormControl, TextField, MenuItem, Input, InputLabel, InputAdornment } from "@mui/material";
import { ArrowDownward, AddCircleOutline, RemoveCircleOutline } from "@mui/icons-material";
import { experimentFields } from "./experimentFields";
import  EffectForm  from "./effect_form";
import { Effect } from '../../api/newTypes'

const ExperimentForm: React.FC = ({experiment_nr, removeEffect, addEffect, effects, readOnly, inputs, addToExisting = false}: any) => {

    const disabledStyling = {
		"& .MuiInputBase-input.Mui-disabled": {
			WebkitTextFillColor: "#010101",
		  },
	  };

    const insertEffect = (effect) => {
        return (
        <div key={experiment_nr +'_'+ effect.effect_size_number}>
            {effect.experiment_nr == experiment_nr ? (
            <Box >
                <EffectForm 
                    readOnly={readOnly && !addToExisting}
                    inputs={effect} 
                    experiment_nr={experiment_nr} 
                    effect_size_number={effect.effect_size_number}/>
                {(!readOnly) ?(
                    <Button sx={{mt:1}} size='small' onClick={() => removeEffect(effect.effect_size_number, effect.experiment_nr)} variant="outlined" startIcon={<RemoveCircleOutline />}>
                        Remove Effect
                    </Button>
                ):""
                }
            </Box>
            ): ""}
        </div>
        )
    }

    return (
        <Box sx={{ width: "90%", borderLeft: 4, mt: 5, pl: 3 }}>
            <Accordion>
                <AccordionSummary expandIcon={<ArrowDownward />} aria-controls="panel1-content" id="panel1-header">
                    <Typography>Experiment Data</Typography>
                </AccordionSummary>
                <AccordionDetails>
                        {experimentFields.map(field => (
                            <TextField
                                disabled={(readOnly||false)}
                                sx={{ width: "30%", mt: 1, ml: 1, ...disabledStyling}}
                                variant="standard"
                                id={"form" + field.key}
                                label={field.name}
                                name={experiment_nr +"_"+ field.key}
                                select={!!field.options}
                                defaultValue={inputs[field.key]||""}
                            >
                                {field.options?.map(option => (
                                    <MenuItem key={`${field.key}-${option}`} value={option}>
                                        {option}
                                    </MenuItem>
                                ))}
                            </TextField>
                        ))}

                        {/*existing (only when addToExisting)*/}
                        {inputs.effects?.map((effect: {effect_size_number: number, experiment_nr:number}) => (
                            <div>
                                {insertEffect(effect)}
                            </div>
                        ))}

                        {/*new*/}
                        {effects.map((effect: {effect_size_number: number, experiment_nr:number}) => (
                            <div>
                                {insertEffect(effect)}
                            </div>
                        ))}
                    {(!readOnly || addToExisting) ?(
                        <div>
                            <Button onClick={() => {addEffect(experiment_nr)}} variant="outlined" sx={{ mt: 2 }}>
                            Add Effect<AddCircleOutline sx={{ ml: 1 }} />
                            </Button>
                        </div>
                    ):""
                    }
                </AccordionDetails>
            </Accordion>
        </Box>
    );
};

export default ExperimentForm;
