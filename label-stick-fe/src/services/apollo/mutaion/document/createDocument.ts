import gql from "graphql-tag";
import client from "../../client";

const CREATE_PROJECT = gql`
  mutation createDocument($input: CreateDocumentInputDTO!) {
    createDocument(input: $input) {
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

const fetchCreateDocument = async (
  name: string,
  documentType: string,
  projectId: number,
  documentUrl: string
) => {
  const result = await client.mutate({
    mutation: CREATE_PROJECT,
    variables: {
      input: {
        name: name,
        documentType: documentType,
        projectId: projectId,
        documentUrl: documentUrl,
      },
    },
  });
  const { data } = result;
  const { createDocument } = data;
  return createDocument;
};

export default fetchCreateDocument;
