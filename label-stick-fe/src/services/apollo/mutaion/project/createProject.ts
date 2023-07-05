import gql from "graphql-tag";
import client from "../../client";

const CREATE_PROJECT = gql`
  mutation createProject($input: CreateProjectDTO!) {
    createProject(input: $input) {
      statusCode
      message
      data {
        id
        name
        description
        maxUser
      }
    }
  }
`;

const fetchCreateProject = async (
  name: string,
  description: string,
  maxUser: number
) => {
  const result = await client.mutate({
    mutation: CREATE_PROJECT,
    variables: {
      input: {
        name: name,
        description: description,
        maxUser: maxUser,
      },
    },
  });
  const { data } = result;
  const { createProject } = data;
  return createProject;
};

export default fetchCreateProject;
