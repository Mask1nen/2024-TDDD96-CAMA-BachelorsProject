import React, { useState } from "react";
import { FormLabel, FormControlLabel, Checkbox, Tooltip, Box, Button, Accordion, AccordionSummary, AccordionDetails, Typography, FormControl, TextField, MenuItem, Input, InputLabel, InputAdornment } from "@mui/material";
import { ArrowDownward, AddCircleOutline, RemoveCircleOutline } from "@mui/icons-material";
import { experimentFields } from "./experimentFields";
import  EffectForm  from "./effect_form";
import { Effect, schoolGradesOptions } from '../../api/newTypes'
import AddEffectDialog from "./addEffectDialog"


const ExperimentForm: React.FC = ({experiment_nr, removeEffect, addEffect, effects, readOnly = false, inputs = {}, expanded = false, study_id = -1, fetchExistingStudy=() => {}}: any) => {

    const disabledStyling = {
		"& .MuiInputBase-input.Mui-disabled": {
			WebkitTextFillColor: "#010101",
		  },
	  };

    const insertEffect = (effect:any) => {
        return (
        <div key={experiment_nr +'_'+ effect.effect_size_number}>
            {effect.experiment_nr == experiment_nr ? (
            <Box >
                <EffectForm 
                    readOnly={readOnly}
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

    //addEffectDialog
    const [addEffectDialogOpen, setAddEffectDialogOpen] = React.useState(false);
	const handleAddEffectDialogOpen = () => setAddEffectDialogOpen(true);
	const handleAddEffectDialogClose = () => {
        fetchExistingStudy();
		setAddEffectDialogOpen(false);
	}
    const schoolGradesOptions = [
    {label:"K", val:"K",},
    {label:"1", val: "first"},
    {label:"2", val: "second"},
    {label:"3", val: "third"},
    {label:"4", val: "fourth"},
    {label:"5", val: "fifth"},
    {label:"6", val: "sixth"},
    {label:"7", val: "seventh"},
    {label:"8", val: "eight"},
    {label:"9", val: "ninth"},
    {label:"10", val: "tenth"},
    {label:"11", val: "eleventh"},
    {label:"12", val: "twelfth"}];

    return (
        <Box sx={{ width: "90%", borderLeft: 4, mt: 5, pl: 3 }}>
            <AddEffectDialog dialogOpen={addEffectDialogOpen} handleDialogClose={handleAddEffectDialogClose} experiment_nr={experiment_nr} study_id={study_id || 0}/>
            <Accordion defaultExpanded={expanded}>
                <AccordionSummary expandIcon={<ArrowDownward />} aria-controls="panel1-content" id="panel1-header">
                    <Typography>Experiment Data</Typography>
                </AccordionSummary>
                <AccordionDetails>
                    <FormLabel component="legend">School grade</FormLabel>
                    {schoolGradesOptions.map(grade => (

                        <FormControlLabel
                        key={"grade_" + grade.val}
                        sx={{mx:0}}
                        name={experiment_nr+"_grade_"+grade.val}
                        control={<Checkbox name={experiment_nr+"_grade_"+grade.val}/>}
                        label={grade.label}
                        labelPlacement="top"
                        />
                    ))}
                    <br/>
                        {experimentFields.map(field => (
                            <TextField
                                key={field.key}
                                disabled={(readOnly||false||field.type=="disabled")}
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

                        

                        {/*existing effects (only when addToExisting)*/}
                        {inputs.effects?.map((effect: {effect_size_number: number, experiment_nr:number}) => (
                            <div key={experiment_nr +'_'+ effect.effect_size_number}>
                                {insertEffect(effect)}
                            </div>
                        ))}

                        {/*new effects*/}
                        {effects.map((effect: {effect_size_number: number, experiment_nr:number}) => (
                             <div key={experiment_nr +'_'+ effect.effect_size_number}>
                                {insertEffect(effect)}
                            </div>
                        ))}
                    {(!readOnly) ?(
                        <div>
                            <Button onClick={() => {addEffect(experiment_nr)}} variant="outlined" sx={{ mt: 2 }}>
                                Add Effect<AddCircleOutline sx={{ ml: 1 }} />
                            </Button>
                        </div>
                    ):(
                        <div>
                            <Button onClick={handleAddEffectDialogOpen} variant="outlined" sx={{ mt: 2 }}>
                                Add Effect To Experiment<AddCircleOutline sx={{ ml: 1 }} />
                            </Button>
                        </div>
                    ) }
                </AccordionDetails>
            </Accordion>
        </Box>
    );
};

export default ExperimentForm;
