import gql from "graphql-tag";
import client from "../client";

const GET_CHECK = gql`
  query healthCheck {
    healthCheck {
      status
      message
    }
  }
`;

const fetchHealthCheck = async () => {
  const result = await client.query({
    query: GET_CHECK,
  });
  const { data } = result;
  const { healthCheck } = data;
  return healthCheck;
};

export default fetchHealthCheck;
