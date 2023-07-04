import { ThemeProvider } from "@mui/material/styles";
import "./App.css";
import { QueryClient, QueryClientProvider } from "react-query";
import theme from "@utils/theme";
import NavigationRouter from "@routers/router";

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <ThemeProvider theme={theme}>
        <NavigationRouter />
      </ThemeProvider>
    </QueryClientProvider>
  );
}

export default App;
