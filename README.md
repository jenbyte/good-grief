# Vite + FastAPI + Neon Starter

A minimal, safe pattern to connect a React (Vite) frontend to a Neon (Postgres) database via a Python (FastAPI) backend.

## Technologies Used & Pre-requisites

### Frontend

- **React**
- **Vite**
- **TypeScript**

### Backend

- **FastAPI** - A high-performance Python web framework for building APIs quickly and efficiently
- Uvicorn: An ASGI server to run FastAPI application
- SQLAlchemy: An ORM for database interactions
- psycopg2-binary: PostgreSQL adapter for Python
- Pydantic: For data validation and settings management
- python-dotenv: To load environment variables from a .env file

### Database

- **NeonDB** - serverless postgres platform

## Run Frontend (Client)

Navigate to the frontend directory and start the local development server:

```bash
cd client

npm run dev
```

## Run Backend (Server)

1. Navigate to the backend

```bash
cd server
```

2. Activate the virtual environment

```bash
source .venv/bin/activate
```

3. Start the API server

```bash
uvicorn app.main:app --reload

uvicorn app.main:app --reload --port 8000
```

4. Exit the virtual environment

```bash
deactivate
```

# React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type-aware lint rules:

```js
export default tseslint.config([
  globalIgnores(["dist"]),
  {
    files: ["**/*.{ts,tsx}"],
    extends: [
      // Other configs...

      // Remove tseslint.configs.recommended and replace with this
      ...tseslint.configs.recommendedTypeChecked,
      // Alternatively, use this for stricter rules
      ...tseslint.configs.strictTypeChecked,
      // Optionally, add this for stylistic rules
      ...tseslint.configs.stylisticTypeChecked,

      // Other configs...
    ],
    languageOptions: {
      parserOptions: {
        project: ["./tsconfig.node.json", "./tsconfig.app.json"],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
]);
```

You can also install [eslint-plugin-react-x](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-x) and [eslint-plugin-react-dom](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-dom) for React-specific lint rules:

```js
// eslint.config.js
import reactX from "eslint-plugin-react-x";
import reactDom from "eslint-plugin-react-dom";

export default tseslint.config([
  globalIgnores(["dist"]),
  {
    files: ["**/*.{ts,tsx}"],
    extends: [
      // Other configs...
      // Enable lint rules for React
      reactX.configs["recommended-typescript"],
      // Enable lint rules for React DOM
      reactDom.configs.recommended,
    ],
    languageOptions: {
      parserOptions: {
        project: ["./tsconfig.node.json", "./tsconfig.app.json"],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
]);
```
