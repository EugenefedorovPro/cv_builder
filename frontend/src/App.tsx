import { BrowserRouter, Route, Routes } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import Layout from "./pages/Layout";
import LayoutBuilder from "./pages/LayoutBuilder";
import User from "./components/User";
import UserForm from "./builder/UserForm";
import { Login } from "./builder/Login";
import { LangProvider } from "./contexts/LangContext";
import { AuthProvider } from "./contexts/AuthContext";

function App() {
  return (
    <AuthProvider>
      <LangProvider>
        <BrowserRouter>
          <Routes>
            // public layout
            <Route path="/" element={<Layout />} />
            <Route path="/user" element={<User />} />
            <Route path="/user_form" element={<UserForm />} />
            // Builder layout
            <Route path="/builder" element={<LayoutBuilder/>} />
            <Route path="/login" element={<Login />} />
          </Routes>
        </BrowserRouter>
      </LangProvider>
    </AuthProvider>
  );
}

export default App;
