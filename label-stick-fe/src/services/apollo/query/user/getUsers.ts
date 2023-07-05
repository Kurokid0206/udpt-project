import gql from "graphql-tag";
import client from "../../client";

const GET_USERS = gql`
  query {
    getLabelers {
      statusCode
      message
      data {
        userId
        username
        email
      }
    }
  }
`;

const fetchGetLabelers = async () => {
  const result = await client.query({
    query: GET_USERS,
  });
  const { data } = result;
  const { getLabelers } = data;
  return getLabelers;
};

export default fetchGetLabelers;
