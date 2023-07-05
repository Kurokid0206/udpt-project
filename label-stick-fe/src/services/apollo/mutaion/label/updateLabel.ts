import gql from "graphql-tag";
import client from "../../client";

const UPDATE_LABEL = gql`
  mutation updateLabel($id: Int!, $input: LabelInputDTO!) {
    updateLabel(id: $id, input: $input) {
      statusCode
      message
      data {
        statusCode
        message
      }
    }
  }
`;

const updateLabel = async (id: number, name: string) => {
  const result = await client.mutate({
    mutation: UPDATE_LABEL,
    variables: {
      id: id,
      input: {
        name: name,
      },
    },
  });
  const { data } = result;
  const { updateLabel } = data;
  return updateLabel;
};

export default updateLabel;
