import React from "react";
import mainImage from "../../assets/images/falcon.png";
import { MinusCircleIcon } from "@heroicons/react/16/solid";
import { DataGrid, GridToolbar } from "@mui/x-data-grid";
import { useDemoData } from "@mui/x-data-grid-generator";
import { Link } from "react-router-dom";
import { Luggage } from "@mui/icons-material";
import { Button, Grid,Tab, Box, Typography, Tabs,Input, FilledInput, OutlinedInput, InputLabel, InputAdornment, FormHelperText, FormControl, TextField, MenuItem} from "@mui/material";
import  ApprovalCard  from "./ApprovalCard";

const AdminPage: React.FC = () => {

	const studies = [
			{
				"uploader":"0000-0002-1825-0097",
				"nr_downloads":"",
				"id":"8351152b-d7ba-4b2b-b911-9578ac465dfb",
				"title":"bästa rapporten",
				"authors":"J.k rowling",
				"keywords":"sdf",
				"abstract":"Den här studyn lorem ipsum",
				"category":"ha",
				"country":"ES",
				"study_year":"9",
				"doi":"ha",
				"peer_reviewed":false,
				"experiments":[
				   {
					  "risks":{
						 "rob":"low",
						 "robins":""
					  },
					  "implemented":"teacher",
					  "study_id":"8351152b-d7ba-4b2b-b911-9578ac465dfb",
					  "id":"8803e22e-b332-4d34-b4fe-50366091461c",
					  "source":"",
					  "experiment_number":"2",
					  "intervention":"js",
					  "intervention_op":"js",
					  "target_population":"js",
					  "mean_age":"9",
					  "grade":"hs",
					  "ni":"8",
					  "study_design":"RCT",
					  "participant_design":"within",
					  "implementation":"teacher",
					  "duration_week":"7",
					  "frequency_n":"7",
					  "intensity_n":"7",
					  "robins":"low",
					  "rob":"gs",
					  "effects":[
						 {
							"id":"1",
							"study_id":"8351152b-d7ba-4b2b-b911-9578ac465dfb",
							"experiment_id":"8803e22e-b332-4d34-b4fe-50366091461c",
							"test_time":"baseline",
							"gender_1":"3",
							"gender_2":"3",
							"gender_3":"3",
							"effect_size_type":"RR",
							"mean_age_1i":"7",
							"m1i":"7",
							"sd1i":"7",
							"n1i":"9",
							"mean_age_2i":"9",
							"m2i":"9",
							"sd2i":"9",
							"n2i":"9",
							"icc":"9",
							"ai":"9",
							"bi":"9",
							"ci":"9",
							"di":"9",
							"ri":"9",
							"t":"4",
							"f_stat":"8",
							"d":"8",
							"d_var":"8",
							"outcome":"j",
							"test_name":"j",
							"outcome_full":"j",
							"outcome_op":"j"
						 }
					  ]
				   }
				]
			 }
		]
 

	return (
		<Box sx={{py:2, pl:2, textAlign:"left"}}>
			<Typography variant="h3" gutterBottom>
				Upload control
			</Typography>
				<Box sx={{ borderBottom: 1, borderColor: 'divider', my:1}}>
				</Box>
				
					<Typography variant="h5">
						Pending studies
					</Typography>
					{studies.map(study => 
						<ApprovalCard data={study}/>
						
					)}


		</Box>

	);
};

export default AdminPage;