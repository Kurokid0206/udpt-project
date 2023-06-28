import useWindowDimensions from "@utils/common";
import React from "react";
import ResponsiveAppBar from "./appbar";
import { Outlet } from "react-router-dom";

const MainLayout: React.FC = () => {
  const [isOpenMenu, setIsOpenMenu] = React.useState<boolean>(false);
  const { height } = useWindowDimensions();

  return (
    <>
      <ResponsiveAppBar></ResponsiveAppBar>
      <Outlet />
    </>
  );
};

export default MainLayout;
