import { BrowserRouter, Route, Routes } from "react-router-dom";
import MainLayout from "@layouts/main";
import NotFound from "@views/notFound/notFound";
import ManagerHomePage from "@views/manager/managerHomePage";
import UserHomePage from "@views/user/userHomePage";
import AdminHomePage from "@views/admin/adminHomePage";
import LoginPage from "@views/login/loginPage";
import DocumentPage from "@views/document/documentPage";
import AssignmentPage from "@views/assignment/assignmentPage";
import AssignMePage from "@views/user/assignMePage";

const NavigationRouter: React.FC = () => {
  //define your all page below
  const pathList: RouterElement[] = [
    {
      path: "/manager",
      element: <ManagerHomePage />,
    },
    {
      path: "/user",
      element: <UserHomePage />,
    },
    {
      path: "/admin",
      element: <AdminHomePage />,
    },
    {
      path: "/document",
      element: <DocumentPage />,
    },
    {
      path: "/assignment",
      element: <AssignmentPage />,
    },
    {
      path: "user/assign",
      element: <AssignMePage />,
    },
  ];
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainLayout />}>
          {pathList.map((item) => (
            <Route path={item.path} element={item.element} key={item.path} />
          ))}
        </Route>
        <Route path="/login" element={<LoginPage />}></Route>
        <Route path="*" element={<NotFound />}></Route>
      </Routes>
    </BrowserRouter>
  );
};
export default NavigationRouter;
