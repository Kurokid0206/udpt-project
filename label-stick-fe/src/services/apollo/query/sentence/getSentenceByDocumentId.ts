import gql from "graphql-tag";
import client from "../../client";

const GET_SENTENCE_BY_DOCUMENT_ID = gql`
  query getSentencesByDocumentId($documentId: Int!) {
    getSentencesByDocumentId(documentId: $documentId) {
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

const fetchGetSentenceByDocumentId = async (documentId: number) => {
  const result = await client.query({
    query: GET_SENTENCE_BY_DOCUMENT_ID,
    variables: {
      documentId: documentId,
    },
  });
  const { data } = result;
  const { getSentencesByDocumentId } = data;
  return getSentencesByDocumentId;
};

export default fetchGetSentenceByDocumentId;
