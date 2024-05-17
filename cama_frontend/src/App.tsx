import './App.css'
import { Fragment } from 'react/jsx-runtime';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import  Navbar from './components/Navbar.tsx';
import HomePage from './pages/Home/HomePage';
import Footer from './components/Footer.tsx';
import Profile from './pages/Profile/Profile';
import AboutPage from './pages/FooterPages/AboutPage.tsx';
import TeamPage from './pages/FooterPages/TeamPage.tsx';
import ContactInfoPage from './pages/FooterPages/ContactInfoPage.tsx';
import AppPage from './pages/FooterPages/AppPage.tsx';
import FbFPage from './pages/FooterPages/FbFPage.tsx';
import AdminPage from './pages/Admin/AdminPage.tsx';
import UploadPage from './pages/Upload/UploadPage.tsx';
import LoginPage from './pages/Login/LoginPage.tsx';
import { createTheme } from '@mui/material/styles';
import { Box, Container } from '@mui/material';
import { ThemeProvider } from '@emotion/react';
import DatabasePage from './pages/Database/DatabasePage.tsx';
import { Dataset } from '@mui/icons-material';
import DatabaseDetail from './pages/Database/DatabaseDetail.tsx';
import SubjectsPage from './pages/Subjects/SubjectsPage.tsx';


import React, {useState} from "react";
export const Context = React.createContext();  //creates the chared context for global language

const App: React.FC = () => {

  const [isSWE, setIsSWE] = useState(false);  //creates the chared context for global language

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
        <Context.Provider value = {[isSWE, setIsSWE]}>
      <Navbar />
      <Container sx={{px:4, py:4, minHeight: '60vh'}} className="bg-gray-100">
        <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/Home" element={<HomePage />} />
            <Route path="/Subjects" element={<SubjectsPage />} />
            <Route path="/Profile" element={<Profile />} />
            <Route path="/Database" element={<DatabasePage />} />
            <Route path="/Database/:id" element={<DatabaseDetail />} />
            <Route path="/Admin" element={<AdminPage />} />
            <Route path="/About" element={<AboutPage />} />
            <Route path="/Team" element={<TeamPage />} />
            <Route path="/ContactInfo" element={<ContactInfoPage />} />  
            <Route path="/App" element={<AppPage />} />  
            <Route path="/FbF" element={<FbFPage />} />  
            <Route path="/Upload" element={<UploadPage />} />
            <Route path="/login" element={<LoginPage />} />
        </Routes>
      </Container>
      <Footer />
      </Context.Provider>
      </ThemeProvider>
    </Router>
  )
};
export default App
