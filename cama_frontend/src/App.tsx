import './App.css'
import { Fragment } from 'react/jsx-runtime';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import  Navbar from './components/Navbar.tsx';
import HomePage from './pages/Home/HomePage';
import Footer from './components/Footer.tsx';
import Profile from './pages/Profile/Profile';
import AboutPage from './pages/About/AboutPage.tsx';
import UploadPage from './pages/Upload/UploadPage.tsx';

import { createTheme } from '@mui/material/styles';
import { Box, Container } from '@mui/material';
import { ThemeProvider } from '@emotion/react';
import DatasetsPage from './pages/Datasets/DatasetsPage.tsx';
import { Dataset } from '@mui/icons-material';
import DatasetDetail from './pages/Datasets/DatasetDetail.tsx';



const App: React.FC = () => {

const theme = createTheme({
  
  palette: {
    mode: 'light',
    primary: {
      light: '#757ce8',
      main: '#000000',
      dark: '#002884',
      contrastText: '#fff',
    },
    secondary: {
      light: '#ff7961',
      main: '#f44336',
      dark: '#ba000d',
      contrastText: '#000',
    },
  },
});

  return (
    <Router>
      <ThemeProvider theme={theme}>
      <Navbar />
      <Container sx={{px:4, py:4, minHeight: '60vh'}} className="bg-gray-100">
        <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/Home" element={<HomePage />} />
            <Route path="/Subjects" element={<HomePage />} />
            <Route path="/Profile" element={<Profile />} />
            <Route path="/Database" element={<DatasetsPage />} />
            <Route path="/About" element={<AboutPage />} />
            <Route path="/Upload" element={<UploadPage />} />
            <Route path="/datasets/:titleSlug" element={<DatasetDetail />} />
        </Routes>
      </Container>
      <Footer />
      </ThemeProvider>
    </Router>
  )
};
export default App
