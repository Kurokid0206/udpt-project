import gql from "graphql-tag";
import client from "../../client";

const GET_DOCUMENTS = gql`
  query getDocuments($filter: DocumentFilterInputDTO) {
    getDocuments(filter: $filter) {
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

const fetchDocuments = async (projectId: number) => {
  const result = await client.query({
    query: GET_DOCUMENTS,
    variables: {
      filter: {
        projectId: projectId,
      },
    },
  });
  const { data } = result;
  const { getDocuments } = data;
  return getDocuments;
};

export default fetchDocuments;
