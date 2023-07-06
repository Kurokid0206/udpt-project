import { ThemeProvider } from "@mui/material/styles";
import "./App.css";
import { QueryClient, QueryClientProvider } from "react-query";
import theme from "@utils/theme";
import NavigationRouter from "@routers/router";
import store from "@redux/store";
import { Provider } from "react-redux";

const queryClient = new QueryClient();

function App() {
  return (
    <Provider store={store}>
      <QueryClientProvider client={queryClient}>
        <ThemeProvider theme={theme}>
          <NavigationRouter />
        </ThemeProvider>
      </QueryClientProvider>
    </Provider>
  );
}

export default App;
