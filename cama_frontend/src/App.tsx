import './App.css'
import { Fragment } from 'react/jsx-runtime';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import  Navbar from './components/Navbar.tsx';
import HomePage from './pages/Home/HomePage';

const App: React.FC = () => {
  return (
    <Router>
      <div className='sticky'>
      <Navbar />
      </div>
      <Routes>
        <Route path="/" element={<HomePage />} />
        </Routes>
    </Router>
  )
};
export default App
