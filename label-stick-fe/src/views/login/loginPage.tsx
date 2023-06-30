import { Button } from "@mui/material";
import { NavLink } from "react-router-dom";

const LoginPage: React.FC = () => {
  return (
    <div
      style={{
        width: "100%",
        height: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <NavLink to="/manager">
        <Button variant="outlined">Login</Button>
      </NavLink>
    </div>
  );
};
export default LoginPage;
