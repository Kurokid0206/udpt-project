import gql from "graphql-tag";
import client from "../../client";

const GET_ASSIGNMENTS = gql`
  query {
    getAssignments {
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

const fetchGetAssignments = async () => {
  const result = await client.query({
    query: GET_ASSIGNMENTS,
    fetchPolicy: "network-only",
  });
  const { data } = result;
  const { getAssignments } = data;
  return getAssignments;
};

export default fetchGetAssignments;
