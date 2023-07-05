import gql from "graphql-tag";
import client from "../../client";

const GET_PROJECT_BY_USER_ID = gql`
  query getProjectsByUserId($filter: ProjectUserFilterDTO!) {
    getProjectsByUserId(filter: $filter) {
      statusCode
      message
      data {
        id
        name
        description
        maxUser
      }
    }
  }
`;

const fetchGetProjectsByUserId = async (userId: number) => {
  const result = await client.query({
    query: GET_PROJECT_BY_USER_ID,
    variables: {
      filter: {
        userId: userId,
      },
    },
  });
  const { data } = result;
  const { getProjectsByUserId } = data;
  return getProjectsByUserId;
};

export default fetchGetProjectsByUserId;
