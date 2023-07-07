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
import UserLabeling from "@views/user/userLabeling";
import ManagerLabelPage from "@views/manager/managerLabelPage";
import AddSentencesPage from "@views/document/addSentencesPage";
import { useAppSelector } from "@redux/hooks";

const NavigationRouter: React.FC = () => {
  const user = useAppSelector((store) => store.user);
  //define your all page below
  const pathList: RouterElement[] = [
    {
      path: "/manager",
      element: <ManagerHomePage />,
    },
    {
      path: "/label",
      element: <ManagerLabelPage />,
    },
    {
      path: "/user",
      element: <UserHomePage />,
    },
    {
      path: "/user/labeling/:assignmentId",
      element: <UserLabeling />,
    },
    {
      path: "/admin",
      element: <AdminHomePage />,
    },
    {
      path: "/project/:projectId/document",
      element: <DocumentPage />,
    },
    {
      path: "/document/add-sentences",
      element: <AddSentencesPage />,
    },
    {
      path: "/assignment",
      element: <AssignmentPage />,
    },
  ];

  const user_view = [
    {
      path: "/user/labeling/:assignmentId",
      element: <UserLabeling />,
    },
    {
      path: "user/assign",
      element: <AssignMePage />,
    },
  ];
  return (
    <BrowserRouter>
      <Routes>
        {user.role === "MANAGER" && (
          <Route path="/" element={<MainLayout />}>
            {pathList.map((item) => (
              <Route path={item.path} element={item.element} key={item.path} />
            ))}
          </Route>
        )}
        {user.role === "USER_LV_1" && (
          <Route path="/" element={<MainLayout />}>
            {user_view.map((item) => (
              <Route path={item.path} element={item.element} key={item.path} />
            ))}
          </Route>
        )}
        {user.role === undefined && (
          <Route path="*" element={<LoginPage />}></Route>
        )}

        <Route path="*" element={<NotFound />}></Route>
      </Routes>
    </BrowserRouter>
  );
};
export default NavigationRouter;
