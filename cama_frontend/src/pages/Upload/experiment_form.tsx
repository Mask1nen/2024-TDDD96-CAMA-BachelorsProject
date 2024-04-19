import React, { useState } from "react";
import { Box, Button, Accordion, AccordionSummary, AccordionDetails, Typography, FormControl, TextField, MenuItem, Input, InputLabel, InputAdornment } from "@mui/material";
import { ArrowDownward, AddCircleOutline, RemoveCircleOutline } from "@mui/icons-material";
import { experimentFields } from "./experimentFields";
import  EffectForm  from "./effect_form";

const ExperimentForm: React.FC = (props) => {
    const [inputs, setInputs] = useState<Record<string, string>>({});
    const [effects, setEffects] = useState<number[]>([]);

    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        console.log(inputs);
    };

    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = event.target;
        setInputs(prev => ({ ...prev, [name]: value }));
    };

    const addEffect = () => {

        setEffects(function(prev) {
            let id = prev.length + 1;
            setInputs(function(pre){
                pre["experiments"][props.experimentId][""] = {"experiment_id": id}
                return pre;
            }); 
            return [...prev, id]
        });  // Ensure you are adding unique identifiers
    };
	const removeEffect = (index: number) => {
        if(window.confirm('Are you sure you want to remove this effect?')) {
            setEffects(prev => prev.filter((_, idx) => idx !== index));
        }
    };

    console.log(props)

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
                                    value={props.inputs[props.index][field.key] || ""}
                                    onChange={(e) => {props.onChange(e, props.experimentId)}}
                                >
                                    {field.options?.map(option => (
                                        <MenuItem key={`${field.key}-${option}`} value={option}>
                                            {option}
                                        </MenuItem>
                                    ))}
                                </TextField>
                            </FormControl>
                        ))}
                    {effects.map((effectId, index) => (
                        <Box key={effectId}>
                            <EffectForm onChange={props.onChangeEffect} inputs={props.inputs} experimentId={props.experimentId} effectId={effectId}/>
                            <Button onClick={() => removeEffect(index)} variant="outlined" startIcon={<RemoveCircleOutline />}>
                                Remove Effect
                            </Button>
                        </Box>
                    ))}
                    <Button onClick={addEffect} variant="outlined" sx={{ mt: 2 }}>
                        Add Effect<AddCircleOutline sx={{ ml: 1 }} />
                    </Button>
                </AccordionDetails>
            </Accordion>
        </Box>
    );
};

export default ExperimentForm;
