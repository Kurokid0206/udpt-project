import { BrowserRouter, Route, Routes } from "react-router-dom";
import MainLayout from "@layouts/main";
import Home from "@views/home/home";
import NotFound from "@views/notFound/notFound";

interface RouterElement {
  path: string;
  element: React.ReactNode;
  childs: RouterElement[] | [];
}
const NavigationRouter: React.FC = () => {
  const pathList: RouterElement[] = [
    {
      path: "/",
      element: <MainLayout />,
      childs: [
        {
          path: "/",
          element: <Home />,
          childs: [],
        },
      ],
    },
    {
      path: "*",
      element: <NotFound />,
      childs: [],
    },
  ];
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainLayout />}>
          <Route path="/" element={<Home />} />
        </Route>
        <Route path="*" element={<NotFound />}></Route>
        {pathList.map((item) => {
          return (
            <Route path={item.path} element={item.element}>
              {item.childs.map((itemChild) => (
                <Route path={itemChild.path} element={itemChild.element} />
              ))}
            </Route>
          );
        })}
      </Routes>
    </BrowserRouter>
  );
};
export default NavigationRouter;
