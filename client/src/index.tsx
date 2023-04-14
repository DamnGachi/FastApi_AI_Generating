import React, { createContext } from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import UserStore from "./store/UserStore";


interface ContextProps {
  user: UserStore;
}

export const Context = createContext<ContextProps>({
  user: new UserStore(),
});

ReactDOM.render(
  <Context.Provider value={{
    user: new UserStore()
  }}>
    <App />
  </Context.Provider >,
  document.getElementById("root")
);
