import { useState } from "react";
import "./App.css";
import Home from "./pages/Home/Home";

function App() {
  return (
    <>
      <div className="bg-white rounded-xl min-h-9/10 p-5 md:p-10">
        <Home />
      </div>
    </>
  );
}

export default App;
