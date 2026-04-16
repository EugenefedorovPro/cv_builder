import { BrowserRouter, Route, Routes } from "react-router-dom";
import Layout from "./pages/Layout";
import User from "./components/User";
import UserForm from "./components/forms/UserForm.tsx";
import { LangProvider } from "./contexts/LangContext";

function App() {
  return (
    <LangProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Layout />} />
          <Route path="/user" element={<User />} />
          <Route path="/user_form" element={<UserForm />} />
        </Routes>
      </BrowserRouter>
    </LangProvider>
  );
}

export default App;
