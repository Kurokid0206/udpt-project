import gql from "graphql-tag";
import client from "../../client";

const GET_LABELS_BY_SENTENCE_ID = gql`
  query getSentenceLabels($sentenceId: Int!) {
    getSentenceLabels(sentenceId: $sentenceId) {
      statusCode
      message
      data {
        sentenceId
        labelId
        status
        labeledBy
        label
      }
    }
  }
`;

const fetchGetSentenceLabels = async (sentenceId: number) => {
  const result = await client.query({
    query: GET_LABELS_BY_SENTENCE_ID,
    variables: {
      sentenceId: sentenceId,
    },
  });
  const { data } = result;
  const { getSentenceLabels } = data;
  return getSentenceLabels;
};

export default fetchGetSentenceLabels;
