import ReactDOM from "react-dom/client";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { authRoutes, publicRoutes } from '../routes';
import { Context } from '..';
import { useContext } from "react";

const AppRouter = () => {
  const { user } = useContext(Context)

  console.log(user)
  return (
    // <Router>
      <Routes>
        {user._isAuth &&
          authRoutes.map(({ path, Component }) => (
            <Route key={path} path={path} element={<Component />} />
          ))}
        {publicRoutes.map(({ path, Component }) => (
          <Route key={path} path={path} element={<Component />} />
        ))}
      </Routes>
    // </Router>
  );
};

export default AppRouter;
