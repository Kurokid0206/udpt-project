import gql from "graphql-tag";
import client from "../../client";

const LOGIN = gql`
  mutation login($input: LoginDTO!) {
    login(input: $input) {
      statusCode
      message
      data {
        userId
        username
        email
        role
      }
    }
  }
`;

const login = async (username: string, password: string) => {
  const result = await client.mutate({
    mutation: LOGIN,
    variables: {
      input: {
        username: username,
        password: password,
      },
    },
  });
  const { data } = result;
  const { login } = data;
  return login;
};

export default login;
