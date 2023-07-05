import gql from "graphql-tag";
import client from "../../client";

const GET_DOCUMENTS = gql`
  query getDocuments {
    getDocuments {
      statusCode
      message
      data {
        id
        name
        documentUrl
        documentType
        projectId
      }
    }
  }
`;

const fetchDocuments = async () => {
  const result = await client.query({
    query: GET_DOCUMENTS,
  });
  const { data } = result;
  const { getDocuments } = data;
  return getDocuments;
};

export default fetchDocuments;
