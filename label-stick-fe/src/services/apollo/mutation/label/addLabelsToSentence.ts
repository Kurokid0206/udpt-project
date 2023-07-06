import gql from "graphql-tag";
import client from "../../client";

const ADD_LABELS_TO_SENTENCE = gql`
  mutation addLabelsToSentence($input: LabelSentenceInputDTO!) {
    addLabelsToSentence(input: $input) {
      statusCode
      message
      data {
        id
        sentenceId
        labelId
        labeledBy
        status
      }
    }
  }
`;

const fetchAddLabelsToSentence = async (
  id: number,
  labelIds: number[],
  userId: number
) => {
  const result = await client.mutate({
    mutation: ADD_LABELS_TO_SENTENCE,
    variables: {
      input: {
        id: id,
        labelIds: labelIds,
        userId: userId,
        status: "IN_PROGRESS",
      },
    },
  });
  const { data } = result;
  const { addLabelsToSentence } = data;
  return addLabelsToSentence;
};

export default fetchAddLabelsToSentence;
