import './App.css'
import { Fragment } from 'react/jsx-runtime';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import  Navbar from './components/Navbar.tsx';
import HomePage from './pages/Home/HomePage';
import Footer from './components/Footer.tsx';
import Profile from './pages/Profile/Profile';
import AboutPage from './pages/About/AboutPage.tsx';
import TeamPage from './pages/Team/TeamPage.tsx';
import ContactInfoPage from './pages/ContactInfo/ContactInfoPage.tsx';
import AppPage from './pages/App/AppPage.tsx';
import FbFPage from './pages/FbF/FbFPage.tsx';


import { createTheme } from '@mui/material/styles';
import { Box, Container } from '@mui/material';
import { ThemeProvider } from '@emotion/react';
import DatasetsPage from './pages/Datasets/DatasetsPage.tsx';



const App: React.FC = () => {

const theme = createTheme({
  palette: {
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
      <Container sx={{px:4, py:0}} className="bg-gray-100">
        <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/Home" element={<HomePage />} />
            <Route path="/Subjects" element={<HomePage />} />
            <Route path="/Profile" element={<Profile />} />
            <Route path="/Database" element={<DatasetsPage />} />
            <Route path="/About" element={<AboutPage />} />
            <Route path="/Team" element={<TeamPage />} />
            <Route path="/ContactInfo" element={<ContactInfoPage />} />  
            <Route path="/App" element={<AppPage />} />  
            <Route path="/FbF" element={<FbFPage />} />  
        </Routes>
      </Container>
      <Footer /></ThemeProvider>
    </Router>
  )
};
export default App
