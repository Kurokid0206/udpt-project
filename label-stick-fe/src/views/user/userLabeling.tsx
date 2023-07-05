import { useParams } from "react-router-dom";

const UserLabeling: React.FC = () => {
  let { assignmentId } = useParams();
  return (
    <div>
      <h1>This is UserLabeling for assignment id {assignmentId}</h1>
    </div>
  );
};
export default UserLabeling;
