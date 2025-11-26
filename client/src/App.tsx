import { BrowserRouter, Routes, Route, useLocation } from "react-router-dom";
import { Suspense } from "react";
import { StackHandler, StackProvider, StackTheme } from "@stackframe/react";
import { stackClientApp } from "./stack";
import "./App.css";
import Home from "./pages/Home/Home";
import Articles from "./pages/Articles/Articles";
import Offers from "./pages/Offers/Offers";

function HandlerRoutes() {
  const location = useLocation();
  return (
    <StackHandler app={stackClientApp} location={location.pathname} fullPage />
  );
}

export default function App() {
  return (
    <Suspense fallback={"Loading..."}>
      <StackProvider app={stackClientApp}>
        <StackTheme>
          <BrowserRouter>
            <div className="sm:py-5 md:py-10">
              <div className="bg-white rounded-xl min-h-9/10 p-7 sm:min-w-160 md:px-10 md:min-w-190">
                <Routes>
                  <Route path="/handler/*" element={<HandlerRoutes />} />
                  <Route path="/" element={<Home />} />
                  <Route path="/articles" element={<Articles />} />
                  <Route path="/care-packages" element={<Offers />} />
                </Routes>
              </div>
            </div>
          </BrowserRouter>
        </StackTheme>
      </StackProvider>
    </Suspense>
  );
}
