import { BrowserRouter, Route, Routes } from "react-router-dom";
import Layout from "./pages/Layout";
import User from "./components/User";
import UserForm from "./components/forms/UserForm";
import { Login } from "./pages/Login";
import { LangProvider } from "./contexts/LangContext";
import { AuthProvider } from "./contexts/AuthContext";

function App() {
  return (
    <AuthProvider>
      <LangProvider>
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Layout />} />
            <Route path="/user" element={<User />} />
            <Route path="/user_form" element={<UserForm />} />
            <Route path="/login" element={<Login />} />
          </Routes>
        </BrowserRouter>
      </LangProvider>
    </AuthProvider>
  );
}

export default App;
