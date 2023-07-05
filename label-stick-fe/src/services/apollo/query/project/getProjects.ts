import gql from "graphql-tag";
import client from "../../client";

const GET_PROJECTS = gql`
  query {
    getProjects {
      statusCode
      message
      data {
        id
        name
        maxUser
        description
      }
    }
  }
`;

const fetchGetProjects = async () => {
  const result = await client.query({
    query: GET_PROJECTS,
  });
  const { data } = result;
  const { getProjects } = data;
  return getProjects;
};

export default fetchGetProjects;
