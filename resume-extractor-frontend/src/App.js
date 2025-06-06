import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home';
import Resumes from './pages/Resumes';

function App() {
  return (
    <Router>
      <div className="bg-gray-50 min-h-screen p-4">
        <nav className="mb-6 flex justify-between items-center bg-white p-4 rounded-lg shadow">
          <h1 className="text-2xl font-bold text-blue-700">Resume Extractor</h1>
          <div className="space-x-4">
            <Link to="/" className="text-blue-600 hover:underline">Upload</Link>
            <Link to="/resumes" className="text-blue-600 hover:underline">All Resumes</Link>
          </div>
        </nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/resumes" element={<Resumes />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
