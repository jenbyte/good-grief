import { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import Home from "./pages/Home/Home";
import Articles from "./pages/Articles/Articles";
import Savings from "./pages/Savings/Savings";

function App() {
  return (
    <BrowserRouter>
      <div className="bg-white rounded-xl min-h-9/10 min-w-svh p-7 md:px-10 md:min-w-100">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/articles" element={<Articles />} />
          <Route path="/care-packages" element={<Savings />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
