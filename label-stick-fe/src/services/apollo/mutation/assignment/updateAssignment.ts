import gql from "graphql-tag";
import client from "../../client";

const UPDATE_ASSIGNMENT = gql`
  mutation updateAssignment($id: Int!, $input: UpdateAssignmentInputDTO!) {
    updateAssignment(id: $id, input: $input) {
      statusCode
      message
      data {
        userId
      }
    }
  }
`;

const updateAssignment = async (
  id: number,
  name: string,
  sentenceIds: number[],
  userId: number,
  assignType: string,
  fromDate: string,
  toDate: string
) => {
  const result = await client.mutate({
    mutation: UPDATE_ASSIGNMENT,
    variables: {
      id: id,
      input: {
        name: name,
        sentenceIds: sentenceIds,
        userId: userId,
        assignType: assignType,
        fromDate: fromDate,
        toDate: toDate,
      },
    },
  });
  const { data } = result;
  const { updateAssignment } = data;
  return updateAssignment;
};

export default updateAssignment;
