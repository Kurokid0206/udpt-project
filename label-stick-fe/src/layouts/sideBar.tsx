import Drawer from "@mui/material/Drawer";
import Toolbar from "@mui/material/Toolbar";
import List from "@mui/material/List";
import Divider from "@mui/material/Divider";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import InboxIcon from "@mui/icons-material/MoveToInbox";
import MailIcon from "@mui/icons-material/Mail";
import { NavLink } from "react-router-dom";

const drawerWidth = 240;
const sideBarList: NavBarElement[] = [
  {
    name: "View project",
    path: "/manager",
    icon: <InboxIcon />,
  },
  {
    name: "User",
    path: "/user",
    icon: <MailIcon />,
  },
  {
    name: "Admin",
    path: "/admin",
    icon: <InboxIcon />,
  },
  {
    name: "Assignment",
    path: "/assignment",
    icon: <InboxIcon />,
  },
  {
    name: "Login",
    path: "/login",
    icon: <InboxIcon />,
  },
];

export default function SideBar() {
  return (
    <Drawer
      sx={{
        width: drawerWidth,
        flexShrink: 0,
        "& .MuiDrawer-paper": {
          width: drawerWidth,
          boxSizing: "border-box",
        },
      }}
      variant="permanent"
      anchor="left"
    >
      <Toolbar />
      <Divider />
      <List>
        {sideBarList.map((item) => (
          <ListItem
            key={item.name}
            disablePadding
            sx={{
              "& .active": {
                backgroundColor: "rgba(0, 0, 0, 0.04)",
                span: {
                  fontWeight: "bold",
                },
              },
            }}
          >
            <NavLink
              to={item.path}
              className={({ isActive, isPending }) =>
                isPending ? "pending" : isActive ? "active" : ""
              }
              style={{
                width: "100%",
                textDecoration: "none",
                color: "inherit",
              }}
            >
              <ListItemButton>
                <ListItemIcon>{item.icon}</ListItemIcon>
                <ListItemText primary={item.name} />
              </ListItemButton>
            </NavLink>
          </ListItem>
        ))}
      </List>
    </Drawer>
  );
}
