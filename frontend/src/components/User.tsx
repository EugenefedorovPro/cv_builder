import { urlSignup } from "../urls";
import { useFetchData } from "../api/UseFetchData";
import { ListGroup, ListGroupItem } from "react-bootstrap";

export interface CustomUserType {
  id?: number | string;
  username: string;
  email: string;
  password?: string | null;
}

export interface UserResponseType {
  user_data: CustomUserType;
}

const User = () => {
  const name = "User";
  const { data, loading, error } = useFetchData<UserResponseType>(urlSignup);

  if (loading) {
    return <div>Loading data for {name}...</div>;
  }

  if (error) {
    return (
      <div>
        Error on fetching {name}: {error}
      </div>
    );
  }

  if (!data) {
    return <div>No data on {name}</div>;
  }

  const user_data = data.user_data;

  if (!user_data) {
    return <div>No data on {name}</div>;
  }

  console.log(data);

  return (
    <ListGroup>
      <ListGroupItem>{user_data.username}</ListGroupItem>
      <ListGroupItem>{user_data.email}</ListGroupItem>
    </ListGroup>
  );
};

export default User;
