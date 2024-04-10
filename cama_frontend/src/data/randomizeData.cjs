const fs = require("fs");
const dataset = require("./data_copy.json"); // Ensure the path is correct

const mockTitles = [
  "Analysis of Time Series Data in Climate Change Studies",
  "Machine Learning Approaches for Predicting Stock Market Trends",
  "Big Data Analytics in Healthcare: Case Studies and Applications",
  "The Impact of Social Media Data on Consumer Behavior",
  "Data-Driven Strategies in Digital Marketing: A Comprehensive Review",
  "Advancements in Natural Language Processing for Textual Data Analysis",
  "Blockchain Technology: A Dataset Analysis of Its Adoption and Challenges",
  "Predictive Modeling for Real-Time Traffic Data",
  "Genomic Data Analysis: Techniques and Applications",
  "Environmental Data Science: Monitoring Biodiversity through Big Data",
  "Deep Learning for Image Recognition: Datasets and Achievements",
  "Statistical Methods for Fraud Detection in Financial Datasets",
  "The Role of Open Data in Enhancing Public Governance",
  "Comparative Study of Election Data Analytics Techniques",
  "Understanding Urban Mobility Patterns through Data Visualization",
  "Data Integrity in IoT Devices: Challenges and Solutions",
  "Using Dataset Correlations to Improve Renewable Energy Forecasts",
  "COVID-19 Data Analysis: Insights into the Pandemic's Spread",
];

const mockAuthors = [
     "Jordan Ellis, Ph.D.",
     "Alexa Simmonds, M.Sc.",
     "Raj Patel, Data Scientist",
     "Dr. Liu Yang, Statistician",
     "Isabella Chen, Machine Learning Expert",
     "Prof. Miguel Santos, Environmental Data Analyst",
     "Dr. Nora Q. Abrams, Epidemiologist",
     "Samuel Clarkson, Blockchain Researcher",
     "Anika Bhatnagar, Ph.D. in Genomics",
     "Carlos Mendez, Public Policy Analyst",
     "Fatima Zahra, M.Sc. in Urban Planning",
     "Elijah Martin, Cybersecurity Specialist",
     "Sophia Park, M.Sc. in Renewable Energy",
     "Mohammad Al Farsi, Healthcare Data Analyst",
     "Lena Schmidt, Social Media Analyst",
     "Hiro Tanaka, Ph.D. in Natural Language Processing",
     "Emily Watson, Ph.D. in Financial Mathematics",
];

function getRandomElement(arr) {
  const randomIndex = Math.floor(Math.random() * arr.length);
  return arr[randomIndex];
}

function randomizeTitlesAndAuthors(dataset) {
  return dataset.map((item) => ({
    ...item,
    title: getRandomElement(mockTitles),
    authors: getRandomElement(mockAuthors),
  }));
}

const randomizedDataset = randomizeTitlesAndAuthors(dataset);

// Write the randomized dataset to a new JSON file
fs.writeFile(
  "./randomized_data.json",
  JSON.stringify(randomizedDataset, null, 2),
  "utf8",
  (err) => {
    if (err) throw err;
    console.log("Data has been randomized and saved.");
  }
);
