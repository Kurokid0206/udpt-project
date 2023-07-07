import login from "@apolloClient/mutation/user/login";
import fetchGetProjectsByUserId from "@apolloClient/query/project/getProjectByUserId";
import { AccountCircle } from "@mui/icons-material";
import LockIcon from "@mui/icons-material/Lock";
import { Box, Button, InputAdornment, TextField } from "@mui/material";
import { useEffect, useState } from "react";
import { NavLink, useNavigate } from "react-router-dom";
import { setUser } from "@redux/slices/userSlice";
import { useAppDispatch } from "@redux/store";
import { useAppSelector } from "@redux/hooks";
import png from "@assets/png";

const LoginPage: React.FC = () => {
  const dispatch = useAppDispatch();
  const userState = useAppSelector((store) => store.user);
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const navigate = useNavigate();

  //event handlers
  const handleLogin = () => {
    if (username !== "" && password !== "") {
      login(username, password).then((res) => {
        if (res.statusCode === 200) {
          const user = {
            userId: Number(res.data.userId),
            userName: res.data.username,
            email: res.data.email,
            role: res.data.role,
          };
          dispatch(setUser(user));
          // navigate("/");
        }
      });
    }
  };

  useEffect(() => {
    console.log(userState);
  }, [userState]);

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
        <Box sx={{ height: 100 }}>
          <img src={png.logo} alt="" style={{ height: "100%" }} />
        </Box>
        <Box
          sx={{ fontSize: "26px", fontFamily: "Roboto", fontWeight: "bold" }}
        >
          <h3>Label Sticke - US Codingo</h3>
        </Box>

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
        <Button variant="outlined" onClick={handleLogin}>
          Login
        </Button>
      </Box>
    </div>
  );
};
export default LoginPage;
