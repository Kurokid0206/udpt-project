import gql from "graphql-tag";
import client from "../../client";

const CREATE_LABEL = gql`
  mutation createLabel($input: LabelInputDTO!) {
    createLabel(input: $input) {
      statusCode
      message
      data {
        id
        name
      }
    }
  }
`;

const createLabel = async (name: string) => {
  const result = await client.mutate({
    mutation: CREATE_LABEL,
    variables: {
      input: {
        name: name,
      },
    },
  });
  const { data } = result;
  const { createLabel } = data;
  return createLabel;
};

export default createLabel;
