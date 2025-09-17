import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import Home from "./pages/Home/Home";
import Articles from "./pages/Articles/Articles";
import Savings from "./pages/Savings/Savings";

function App() {
  return (
    <div className="sm:py-5 md:py-10">
      <BrowserRouter>
        <div className="bg-white rounded-xl min-h-9/10 p-7 sm:min-w-160 md:px-10 md:min-w-190">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/articles" element={<Articles />} />
            <Route path="/care-packages" element={<Savings />} />
          </Routes>
        </div>
      </BrowserRouter>
    </div>
  );
}

export default App;
