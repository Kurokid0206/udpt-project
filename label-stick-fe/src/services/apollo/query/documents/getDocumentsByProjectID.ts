import gql from "graphql-tag";
import client from "../../client";

const GET_DOCUMENTS = gql`
  query getDocuments($filter: DocumentFilterInputDTO!) {
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

const fetchGetDocumentsByProjectID = async (
  projectId: number,
  page = 1 as number,
  limit = null as null | number
) => {
  const result = await client.query({
    query: GET_DOCUMENTS,
    variables: {
      filter: {
        projectId: projectId,
        page: page,
        limit: limit,
      },
    },
  });
  const { data } = result;
  const { getDocuments } = data;
  return getDocuments;
};

export default fetchGetDocumentsByProjectID;
