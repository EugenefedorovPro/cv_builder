import { Form, Button } from "react-bootstrap";
import { useState } from "react";
import { useAuth } from "../contexts/AuthContext";
import type { LoginResponseInterface } from "../contexts/AuthContext";

export const Login = () => {
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const { login } = useAuth();
  const [responseData, setResponseData] =
    useState<LoginResponseInterface | null>(null);

  const handleSubmit = async (event: React.ChangeEvent<HTMLFormElement>) => {
    event.preventDefault();
    const data = await login({ username, password });
    setResponseData(data);
  };

  return (
    <>
      <Form onSubmit={handleSubmit}>
        <Form.Group className="mb-3" controlId="formUsername">
          <Form.Label>Username</Form.Label>
          <Form.Control
            type="text"
            placeholder="enter username"
            value={username}
            onChange={(event) => setUsername(event.target.value)}
          />
        </Form.Group>
        <Form.Group className="mt-3" controlId="formPassword">
          <Form.Label>Password</Form.Label>
          <Form.Control
            type="password"
            placeholder="enter password"
            value={password}
            onChange={(event) => setPassword(event.target.value)}
          />
        </Form.Group>
        <Button type="submit">Login</Button>
      </Form>
      {responseData && (
        <div>
          <div>{responseData.detail}</div>
          <div>{responseData.user.username}</div>
          <div>{responseData.user.email}</div>
        </div>
      )}
    </>
  );
};
