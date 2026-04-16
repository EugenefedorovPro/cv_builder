import { urlUser } from "../../urls";
import { usePostData } from "../../api/UsePostData";
import { Form, Button } from "react-bootstrap";
import { useState } from "react";

export interface CreateUserPayload {
  username: string;
  email: string;
  password: string;
}

export interface CustomUserType {
  id?: number | string;
  username: string;
  email: string;
  password?: string | null;
}

export interface UserResponseType {
  user_data: CustomUserType;
}

const UserForm = () => {
  const [inputData, setInputData] = useState<CreateUserPayload>({
    username: "",
    email: "",
    password: "",
  });

  const { data, loading, error, postData } = usePostData<
    UserResponseType,
    CreateUserPayload
  >(urlUser);

  const handleChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    setInputData({
      ...inputData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e: React.ChangeEvent<HTMLFormElement>) => {
    e.preventDefault();
    const result = await postData(inputData);

    if (result) {
      setInputData({
        username: "",
        email: "",
        password: "",
      });
    }
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group className="mb-3" controlId="username">
        <Form.Label>Username</Form.Label>
        <Form.Control
          name="username"
          type="text"
          value={inputData.username}
          onChange={handleChange}
          placeholder="Enter username"
          required
        />
      </Form.Group>
      <Form.Group className="mb-3" controlId="password">
        <Form.Label>Password</Form.Label>
        <Form.Control
          name="password"
          type="password"
          value={inputData.password}
          onChange={handleChange}
          placeholder="Enter password"
          required
        />
      </Form.Group>
      <Form.Group>
        <Form.Label>Email</Form.Label>
        <Form.Control
          name="email"
          type="email"
          value={inputData.email}
          onChange={handleChange}
          placeholder="Enter email"
          required
        />
      </Form.Group>
      <Button type="submit" disabled={loading} className="me-2">
        {loading ? "Saving..." : "Create user"}
      </Button>

      {error && <div className="mt-3">Error: {error}</div>}
      {data && (
        <div>
          Created User: {data.user_data.username} ({data.user_data.email})
        </div>
      )}
    </Form>
  );
};

export default UserForm;
