import { Routes, Route } from "react-router-dom";
import { useEffect } from "react";
import { ConfigProvider } from "antd";
import ruRU from "antd/locale/ru_RU";

function App() {
    useEffect(() => {
        const userId = localStorage.getItem("userId");
        const userRoleId = localStorage.getItem("userRoleId");

        //   if (userId && userRoleId) {
        //     appState.setUserId(+userId);
        //     appState.setUserRoleId(+userRoleId);
        //   }
    }, []);

    return (
        <div className="app">
            <ConfigProvider locale={ruRU}>
                <Routes>
                    {/* <Route path="/" element={<Home />}></Route>
                    <Route path="/auth" element={<Auth />}></Route> */}
                </Routes>
            </ConfigProvider>
        </div>
    );
}


export default App;
