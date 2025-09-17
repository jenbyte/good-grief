import { Outlet, Scripts } from "react-router";

import "./global-styles.css";

export default function App() {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="/favicon.ico" />
      </head>
      <body>
        <Outlet />
        <Scripts />
      </body>
    </html>
  );
}
