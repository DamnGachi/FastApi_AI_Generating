import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import MainPage from './pages/MainPage';
import Gallery from './pages/Gallery';
import Admin from './pages/Admin';
import NavBar from './Components/NavBar';

const App = () => {
    return (
        <Router>
            <NavBar />
            <Routes>
                <Route path="/" element={<Gallery />} />
                <Route path="/admin" element={<Admin />} />
                <Route path="/about" element={<MainPage />} />
            </Routes>
        </Router>
    );
};

export default App;
