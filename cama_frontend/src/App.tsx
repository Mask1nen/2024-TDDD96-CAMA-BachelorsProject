import './App.css'
import { Fragment } from 'react/jsx-runtime';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import  Navbar from './components/Navbar.tsx';
import HomePage from './pages/Home/HomePage';
import Footer from './components/Footer.tsx';

import { createTheme } from '@mui/material/styles';
import { ThemeProvider } from '@emotion/react';



const App: React.FC = () => {

const theme = createTheme({
  palette: {
    primary: {
      light: '#757ce8',
      main: '#3f50b5',
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
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/Home" element={<HomePage />} />
        <Route path="/Subjects" element={<HomePage />} />
      </Routes>
      <Footer /></ThemeProvider>
    </Router>
  )
};
export default App
