import gql from "graphql-tag";
import client from "../../client";

const UPDATE_PROJECT = gql`
  mutation updateProject($id: Int!, $input: UpdateProjectDTO!) {
    updateProject(id: $id, input: $input) {
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

const fetchUpdateProject = async (
  id: number,
  name: string,
  description: string,
  maxUser: number
) => {
  const result = await client.mutate({
    mutation: UPDATE_PROJECT,
    variables: {
      id: id,
      input: {
        name: name,
        description: description,
        maxUser: maxUser,
      },
    },
  });
  const { data } = result;
  const { updateProject } = data;
  return updateProject;
};

export default fetchUpdateProject;
