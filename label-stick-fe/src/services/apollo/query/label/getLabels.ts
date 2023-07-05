import gql from "graphql-tag";
import client from "../../client";

const GET_LABELS = gql`
  query {
    getLabels {
      statusCode
      message
      data {
        id
        name
      }
    }
  }
`;

const fetchGetLabels = async () => {
  const result = await client.query({
    query: GET_LABELS,
  });
  const { data } = result;
  const { getLabels } = data;
  return getLabels;
};

export default fetchGetLabels;
