import gql from "graphql-tag";
import client from "../../client";

const GET_SENTENCE_BY_ID = gql`
  query getSentencesByIds($ids: [Int!]!) {
    getSentencesByIds(ids: $ids) {
      statusCode
      message
      data {
        id
        name
        sentence
        documentId
      }
    }
  }
`;

const fetchGetSentenceByIds = async (ids: number[]) => {
  const result = await client.query({
    query: GET_SENTENCE_BY_ID,
    variables: {
      ids: ids,
    },
    fetchPolicy: "network-only",
  });
  const { data } = result;
  const { getSentencesByIds } = data;
  return getSentencesByIds;
};

export default fetchGetSentenceByIds;
