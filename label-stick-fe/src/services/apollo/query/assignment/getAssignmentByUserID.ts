import gql from "graphql-tag";
import client from "../../client";

const GET_ASSIGNMENTS = gql`
  query getAssignments($filter: AssignmentFilterInputDTO!) {
    getAssignments(filter: $filter) {
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

const fetchGetAssignmentByUserId = async (
  userId: number,
  page: number = 0,
  limit: number = 100
) => {
  const result = await client.query({
    query: GET_ASSIGNMENTS,
    variables: {
      filter: {
        userId: userId,
        page: page,
        limit: limit,
      },
    },
    fetchPolicy: "network-only",
  });
  const { data } = result;
  const { getAssignments } = data;
  return getAssignments;
};

export default fetchGetAssignmentByUserId;
