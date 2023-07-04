import fetchGetProjectsByUserId from "@apolloClient/query/project/getProjectByUserId";
import { AccountCircle } from "@mui/icons-material";
import LockIcon from "@mui/icons-material/Lock";
import { Box, Button, InputAdornment, TextField } from "@mui/material";
import { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";

const LoginPage: React.FC = () => {
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");

  //event handlers
  const handleLogin = () => {
    console.log({ username, password });
  };

  return (
    <div
      style={{
        width: "100%",
        height: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        flexDirection: "column",
        backgroundColor: "#ebebeb",
      }}
    >
      <Box
        sx={{
          display: "flex",
          justifyContent: "center",
          flexDirection: "column",
          alignItems: "center",
          gap: "16px",
          width: "560px",
          backgroundColor: "#fff",
          borderRadius: "16px",
          padding: "68px 16px",
        }}
      >
        <h3>US CODINGO</h3>

        <TextField
          id="username"
          label="User name"
          fullWidth
          value={username}
          onChange={(e) => {
            setUsername(e.target.value);
          }}
          InputProps={{
            startAdornment: (
              <InputAdornment position="start">
                <AccountCircle />
              </InputAdornment>
            ),
          }}
        />
        <TextField
          id="password"
          label="Password"
          type="password"
          value={password}
          onChange={(e) => {
            setPassword(e.target.value);
          }}
          fullWidth
          InputProps={{
            startAdornment: (
              <InputAdornment position="start">
                <LockIcon />
              </InputAdornment>
            ),
          }}
        />
        <NavLink to="/manager">
          <Button variant="outlined" onClick={handleLogin}>
            Login
          </Button>
        </NavLink>
      </Box>
    </div>
  );
};
export default LoginPage;
