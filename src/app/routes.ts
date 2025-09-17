import {
  type RouteConfig,
  route,
  index,
  layout,
  prefix,
} from "@react-router/dev/routes";

export default [
  index("./pages/Home.tsx"),
  route("articles", "./pages/Articles.tsx"),
  route("care-packages", "./pages/Articles.tsx"),

  //** LOGIN **//
  //    layout("./auth/layout.tsx", [
  //     route("login", "./auth/login.tsx"),
  //     route("register", "./auth/register.tsx"),
  //   ]),

  //** POPUP - CHECK-IN? */
  //   ...prefix("concerts", [
  //     index("./concerts/home.tsx"),
  //     route(":city", "./concerts/city.tsx"),
  //     route("trending", "./concerts/trending.tsx"),
  //   ]),
] satisfies RouteConfig;
