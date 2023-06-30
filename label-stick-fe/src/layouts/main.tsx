import * as React from "react";
import Box from "@mui/material/Box";
import CssBaseline from "@mui/material/CssBaseline";
import { Outlet } from "react-router-dom";
import ResponsiveAppBar from "./appbar";
import SideBar from "./sideBar";

const MainLayout: React.FC<{}> = (): JSX.Element => {
  return (
    <Box sx={{ display: "flex", height: "100vh" }}>
      <CssBaseline />
      <ResponsiveAppBar></ResponsiveAppBar>
      <SideBar></SideBar>
      <Box
        component="main"
        sx={{
          flexGrow: 1,
          bgcolor: "background.default",
          p: "64px 24px 24px 24px",
          width: "100%",
          height: "100%",
        }}
      >
        <Outlet></Outlet>
      </Box>
    </Box>
  );
};

export default MainLayout;
