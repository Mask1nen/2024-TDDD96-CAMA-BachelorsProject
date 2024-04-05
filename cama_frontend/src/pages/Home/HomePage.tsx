import React from "react";
import { Button } from "@mui/material";
import mainImage from "../../assets/images/falcon.png";
import bild2 from "../../assets/images/bild2.png";
import {
  Card,
  CardMedia,
  CardContent,
  CardActions,
  Typography,
} from "@mui/material";
import { MinusCircleIcon } from "@heroicons/react/16/solid";
import { DataGrid, GridToolbar } from '@mui/x-data-grid';
import { useDemoData } from '@mui/x-data-grid-generator';

const VISIBLE_FIELDS = ['name', 'rating', 'country', 'dateCreated', 'isAdmin'];

const HomePage: React.FC = () => {

  const rows = [
    { id: 1, name: 'John Doe', age: 30, country: 'USA' },
    { id: 2, name: 'Jane Doe', age: 25, country: 'Canada' },
    // Add more rows as needed
  ];

  const columns = [
    { field: 'id', headerName: 'ID', width: 90 },
    { field: 'name', headerName: 'Name', width: 150 },
    { field: 'age', headerName: 'Age', width: 110 },
    { field: 'country', headerName: 'Country', width: 150 },
  ];
  
  

  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto">
        {/* Section 1 */}
        <div className="flex flex-wrap items-center justify-center py-12">
          <div className="w-full md:w-1/2 lg:w-2/5 px-4 mb-8 md:mb-0">
            <h1 className="text-4xl font-bold text-gray-800 mb-4">
              Welcome to Our Site!
            </h1>
            <p className="text-lg text-gray-600 mb-6">
              Discover our projects and learn more about us.
            </p>
            <Button variant="contained" color="primary">
              Learn More
            </Button>
          </div>
          <div className="w-full md:w-1/2 lg:w-3/5 px-4">
            <img src={mainImage} alt="Main" className="rounded-lg shadow-lg" />
          </div>
        </div>
        {/* Section 2 */}
        

        {/* Section 3 */}
        <section className="flex flex-wrap justify-center py-8">
          <h2 className="text-2xl font-semibold text-gray-700 mb-6">
            Choose Between These Subjects
          </h2>
          <div className="flex flex-wrap items-center justify-between mx-10">
            {/* Repeat for each card */}
            <div className="w-full sm:w-1/2 md:w-1/3 px-4 mb-4">
              <Card
                sx={{
                  width: 320,
                  maxWidth: "100%",
                  boxShadow:
                    "0 2px 4px -2px rgba(0,0,0,0.24), 0 4px 24px -2px rgba(0, 0, 0, 0.2)",
                }}
              >
                <CardMedia
                  image={bild2}
                  sx={{
                    width: "100%",
                    height: 0,
                    paddingBottom: "min(56.25%, 200px)",
                    bgcolor: "rgba(, 0, 0, 0.08)",
                  }}
                />
                <CardContent>
                  
                  <Typography variant="h4" component="div">
                    Heading
                  </Typography>
                  <Typography sx={{ mb: 1.5 }} color="text.secondary">
                    describes the heading
                  </Typography>
                  <Typography variant="body1">
                    Card content
                    <br />
                    {'"describes the content"'}
                  </Typography>
                </CardContent>
                <CardActions>
                  <Button size="small" >Learn More</Button>
                </CardActions>
              </Card>
            </div>
            {/* End of card */}
            <div className="w-full sm:w-1/2 md:w-1/3 px-4 mb-4">
              <Card
                sx={{
                  width: 320,
                  maxWidth: "100%",
                  boxShadow:
                    "0 2px 4px -2px rgba(0,0,0,0.24), 0 4px 24px -2px rgba(0, 0, 0, 0.2)",
                }}
              >
                <CardMedia
                  image={bild2}
                  sx={{
                    width: "100%",
                    height: 0,
                    paddingBottom: "min(56.25%, 200px)",
                    bgcolor: "rgba(, 0, 0, 0.08)",
                  }}
                />
                <CardContent>
                  
                  <Typography variant="h4" component="div">
                    Heading
                  </Typography>
                  <Typography sx={{ mb: 1.5 }} color="text.secondary">
                    describes the heading
                  </Typography>
                  <Typography variant="body1">
                    Card content
                    <br />
                    {'"describes the content"'}
                  </Typography>
                </CardContent>
                <CardActions>
                  <Button size="small" >Learn More</Button>
                </CardActions>
              </Card>
            </div>
            <div className="w-full sm:w-1/2 md:w-1/3 px-4 mb-4">
              <Card
                sx={{
                  width: 320,
                  maxWidth: "100%",
                  boxShadow:
                    "0 2px 4px -2px rgba(0,0,0,0.24), 0 4px 24px -2px rgba(0, 0, 0, 0.2)",
                }}
              >
                <CardMedia
                  image={bild2}
                  sx={{
                    width: "100%",
                    height: 0,
                    paddingBottom: "min(56.25%, 200px)",
                    bgcolor: "rgba(, 0, 0, 0.08)",
                  }}
                />
                <CardContent>
                  
                  <Typography variant="h4" component="div">
                    Heading
                  </Typography>
                  <Typography sx={{ mb: 1.5 }} color="text.secondary">
                    describes the heading
                  </Typography>
                  <Typography variant="body1">
                    Card content
                    <br />
                    {'"describes the content"'}
                  </Typography>
                </CardContent>
                <CardActions>
                  <Button size="small" >Learn More</Button>
                </CardActions>
              </Card>
            </div>
          </div>
        </section>

        {/* Section 4 */}

        {/* Section 5 */}
        <section className="py-8 mx-4">
      <h2 className="text-2xl font-semibold text-gray-700 py-4 text-left mx-4 ">
        Display Studies
      </h2>
      <div style={{ height: 400, width: '100%' }}>
      <DataGrid
        rows={rows}
        columns={columns}
        checkboxSelection
        // For demo data
         //{...data}
      />
    </div>
    </section>
      </div>
    </div>
  );
};

export default HomePage;
