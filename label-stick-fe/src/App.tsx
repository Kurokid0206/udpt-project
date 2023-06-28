import { ThemeProvider } from "@mui/material/styles";
import "./App.css";
import { QueryClient, QueryClientProvider } from "react-query";
import theme from "@utils/theme";
import React from "react";
import fetchHealthCheck from "@apolloClient/query/healthCheck";
import NavigationRouter from "@routers/router";

const queryClient = new QueryClient();

function App() {
  React.useEffect(() => {
    fetchHealthCheck().then((res) => console.log(res));
  }, []);

  return (
    <QueryClientProvider client={queryClient}>
      <ThemeProvider theme={theme}>
        <NavigationRouter />
      </ThemeProvider>
    </QueryClientProvider>
  );
}

export default App;
