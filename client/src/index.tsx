import React, { createContext } from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import UserStore from "./store/UserStore";
import GalleryStore from "./store/GalleryStore";



interface ContextProps {
  user: UserStore;
  gallery: GalleryStore;
}

export const Context = createContext<ContextProps>({
  user: new UserStore(),
  gallery: new GalleryStore()
});

ReactDOM.render(
  <Context.Provider value={{
    user: new UserStore(),
    gallery: new GalleryStore()
  }}>
    <App />
  </Context.Provider >,
  document.getElementById("root")
);
