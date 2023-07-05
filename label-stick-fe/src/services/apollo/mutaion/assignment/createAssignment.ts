import gql from "graphql-tag";
import client from "../../client";

const CREATE_ASSIGNMENT = gql`
  mutation createAssignment($input: CreateAssignmentInputDTO!) {
    createAssignment(input: $input) {
      statusCode
      message
      data {
        id
        name
        sentenceIds
        userId
        assignType
        fromDate
        toDate
      }
    }
  }
`;

const createAssignment = async (
  name: string,
  sentenceIds: number[],
  userId: number,
  assignType: string,
  fromDate: string,
  toDate: string
) => {
  const result = await client.mutate({
    mutation: CREATE_ASSIGNMENT,
    variables: {
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
  const { getAssignments } = data;
  return getAssignments;
};

export default createAssignment;
