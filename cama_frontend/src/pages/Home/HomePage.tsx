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

const HomePage: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto px-4">
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
        <section className="flex flex-wrap items-center justify-center py-8">
          <h2 className="text-2xl font-semibold text-gray-700 mb-6">
            Most Viewed
          </h2>
          <div className="grid grid-cols-2 gap-4">
            <a href="#" className="block">
              <img
                src={bild2}
                alt="Description"
                className="rounded-lg"
              />
            </a>
            <a href="#" className="block">
              <img
                src={bild2}
                alt="Description"
                className="rounded-lg"
              />
            </a>
            <a href="#" className="block">
              <img
                src={bild2}
                alt="Description"
                className="rounded-lg"
              />
            </a>
            <a href="#" className="block">
              <img
                src={bild2}
                alt="Description"
                className="rounded-lg"
              />
            </a>
          </div>
        </section>

        {/* Section 3 */}
        <section className="flex flex-wrap items-center justify-center py-8">
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
        {/* Similar to Section 3 but with only 2 cards */}

        {/* Section 5 */}
        <section className="py-8">
          <h2 className="text-2xl font-semibold text-gray-700">
            Display Studies Placeholder Section
          </h2>
          {/* Placeholder content */}
        </section>

        <footer className="text-center py-6 text-gray-600">
          © 2024 Our Site. All rights reserved.
        </footer>
      </div>
    </div>
  );
};

export default HomePage;
