import gql from "graphql-tag";
import client from "../../client";

const CREATE_SENTENCES = gql`
  mutation createSentences($input: [SentenceInputDTO!]!) {
    createSentences(input: $input) {
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

const fetchCreateSentences = async (
  sentencesInput: {
    name: string;
    sentence: string;
    documentId: number;
  }[]
) => {
  const result = await client.mutate({
    mutation: CREATE_SENTENCES,
    variables: {
      input: sentencesInput,
    },
  });
  const { data } = result;
  const { createSentences } = data;
  return createSentences;
};

export default fetchCreateSentences;
