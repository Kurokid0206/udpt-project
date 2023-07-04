import gql from "graphql-tag";
import client from "../../client";

const CREATE_ASSIGNMENTS = gql`
  mutation createAssignments($input: CreateAssignmentInputDTO!) {
    createAssignments(input: $input) {
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

const createAssignments = async (
  name: string,
  sentenceIds: [number],
  userId: number,
  assignType: string,
  fromDate: Date,
  toDate: Date
) => {
  const result = await client.mutate({
    mutation: CREATE_ASSIGNMENTS,
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

export default createAssignments;
