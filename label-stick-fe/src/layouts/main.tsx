import Box from "@mui/material/Box/Box";
import Grid from "@mui/material/Grid/Grid";
import useWindowDimensions from "@utils/common";
import React from "react";

const MainLayout: React.FC = () => {
  const [isOpenMenu, setIsOpenMenu] = React.useState<boolean>(false);
  const { height } = useWindowDimensions();

  return (
    <>
      <Grid container spacing={2} sx={{ height: height }}>
        <Grid item xs={isOpenMenu ? 2 : 0.5}>
          <Box
            sx={{
              backgroundColor: "gray",
              height: "100%",
              width: "100%",
            }}
          ></Box>
        </Grid>
        <Grid item xs={isOpenMenu ? 10 : 11.5}>
          <Box
            sx={{ height: "100%", width: "100%", backgroundColor: "blue" }}
          ></Box>
        </Grid>
      </Grid>
    </>
  );
};

export default MainLayout;
