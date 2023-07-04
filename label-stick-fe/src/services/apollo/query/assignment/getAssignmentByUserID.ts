import gql from "graphql-tag";
import client from "../../client";

const GET_ASSIGNMEMTS = gql`
  query getDocuments($filter: AssignmentResponseDTOListResponseDTO!!) {
    getDocuments(filter: $filter) {
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
  page = 1 as number,
  limit = null as null | number
) => {
  const result = await client.query({
    query: GET_ASSIGNMEMTS,
    variables: {
      filter: {
        userId: userId,
        page: page,
        limit: limit,
      },
    },
  });
  const { data } = result;
  const { getAssignments } = data;
  return getAssignments;
};

export default fetchGetAssignmentByUserId;
