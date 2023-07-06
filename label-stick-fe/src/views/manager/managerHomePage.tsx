import {
  Box,
  Button,
  Fab,
  IconButton,
  Modal,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  TextField,
  Typography,
} from "@mui/material";
import AddIcon from "@mui/icons-material/Add";
import CloseIcon from "@mui/icons-material/Close";
import EditIcon from "@mui/icons-material/Edit";
import { useEffect, useState } from "react";
import fetchCreateProject from "@apolloClient/mutaion/project/createProject";
import fetchGetProjects from "@apolloClient/query/project/getProjects";
import fetchUpdateProject from "@apolloClient/mutaion/project/updateProject";
import SourceIcon from "@mui/icons-material/Source";
import { useNavigate } from "react-router-dom";

const initProject: Project = {
  id: 0,
  name: "",
  description: "",
  maxUser: 0,
};

const ManagerHomePage: React.FC = () => {
  const navigate = useNavigate();
  const [projects, setProjects] = useState<Project[]>([]);
  const [isOpenModal, setIsOpenModal] = useState<boolean>(false);
  const [nowProject, setNowProject] = useState<Project>(initProject);
  const [isEdit, setIsEdit] = useState<boolean>(false);

  // event handler
  const onClickEditProject = (projectId: number) => {
    let nowEdit = projects.filter((item) => item.id === projectId);
    setNowProject(nowEdit[0]);
    setIsEdit(true);
    setIsOpenModal(true);
  };
  const onCloseModal = () => {
    setNowProject(initProject);
    setIsEdit(false);
    setIsOpenModal(false);
  };
  const handleSaveProject = () => {
    if (isEdit) {
      fetchUpdateProject(
        nowProject.id,
        nowProject.name,
        nowProject.description,
        nowProject.maxUser
      ).then((response) => {
        if (response.statusCode === 200) {
          let list_temp_ = projects.map((item) => {
            if (item.id === nowProject.id) {
              let temp: Project = {
                id: item.id,
                name: response.data.name,
                description: response.data.description,
                maxUser: response.data.maxUser,
              };
              return temp;
            }
            return item;
          });
          setProjects(list_temp_);
          onCloseModal();
        } else {
          console.log(response.message);
        }
      });
    } else {
      fetchCreateProject(
        nowProject.name,
        nowProject.description,
        nowProject.maxUser
      ).then((response) => {
        if (response.statusCode === 200) {
          let temp: Project = {
            id: response.data.id,
            maxUser: response.data.maxUser,
            description: response.data.description,
            name: response.data.name,
          };
          let list_temp = structuredClone(projects);
          list_temp.push(temp);
          setProjects(list_temp);
          onCloseModal();
        } else {
          console.log(response.message);
        }
      });
    }
  };

  useEffect(() => {
    fetchGetProjects().then((response) => {
      let project_data: Project[] = [];
      response.data?.forEach((item: Project) => {
        project_data.push({
          id: item.id,
          description: item.description,
          maxUser: item.maxUser,
          name: item.name,
        });
      });
      setProjects(project_data);
    });
  }, []);

  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        gap: "32px",
        padding: "16px",
      }}
    >
      <Box sx={{ width: "100%", display: "flex" }}>
        <Box sx={{ flex: 1 }}>
          <h1>Project</h1>
        </Box>
        <Fab
          color="primary"
          aria-label="add"
          variant="extended"
          onClick={() => {
            setIsOpenModal(true);
          }}
        >
          <AddIcon />
          Add project
        </Fab>
      </Box>
      <TableContainer component={Paper} sx={{ height: 500 }}>
        <Table
          sx={{ minWidth: 650, maxHeight: 500 }}
          aria-label="simple table"
          stickyHeader={true}
        >
          <TableHead>
            <TableRow>
              <TableCell sx={{ backgroundColor: "#ebebeb" }}>ID</TableCell>
              <TableCell align="right" sx={{ backgroundColor: "#ebebeb" }}>
                Name
              </TableCell>
              <TableCell align="right" sx={{ backgroundColor: "#ebebeb" }}>
                Description
              </TableCell>
              <TableCell align="right" sx={{ backgroundColor: "#ebebeb" }}>
                Max user
              </TableCell>
              <TableCell align="right" sx={{ backgroundColor: "#ebebeb" }}>
                Action
              </TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {projects.map((project, idx) => (
              <TableRow
                key={project.id + idx}
                sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
              >
                <TableCell component="th" scope="row">
                  {project.id}
                </TableCell>
                <TableCell align="right">{project.name}</TableCell>
                <TableCell align="right">{project.description}</TableCell>
                <TableCell align="right">{project.maxUser}</TableCell>
                <TableCell align="right">
                  <Box
                    sx={{
                      display: "flex",
                      gap: "8px",
                      justifyContent: "flex-end",
                    }}
                  >
                    <Box>
                      <IconButton
                        onClick={() => {
                          navigate(`/project/${project.id}/document`);
                        }}
                      >
                        <SourceIcon />
                      </IconButton>
                      <IconButton
                        onClick={() => {
                          onClickEditProject(project.id);
                        }}
                      >
                        <EditIcon />
                      </IconButton>
                    </Box>
                  </Box>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>

      <Modal
        open={isOpenModal}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box
          sx={{
            position: "absolute" as "absolute",
            top: "50%",
            left: "50%",
            transform: "translate(-50%, -50%)",
            width: 600,
            bgcolor: "#fff",
            border: "2px solid #000",
            boxShadow: 24,
            p: 4,
            display: "flex",
            flexDirection: "column",
            gap: "12px",
          }}
        >
          <Box
            sx={{
              display: "flex",
              flexDirection: "row",
              justifyContent: "space-between",
            }}
          >
            <Typography id="modal-modal-title" variant="h6" component="h2">
              Add new project
            </Typography>
            <IconButton
              onClick={onCloseModal}
              sx={{ backgroundColor: "#ebebeb" }}
            >
              <CloseIcon></CloseIcon>
            </IconButton>
          </Box>
          <TextField
            id="name"
            label="Project name"
            fullWidth
            value={nowProject.name}
            onChange={(e) => {
              let temp = structuredClone(nowProject);
              temp.name = e.target.value;
              setNowProject(temp);
            }}
          />
          <TextField
            id="description"
            label="Project description"
            fullWidth
            value={nowProject.description}
            onChange={(e) => {
              let temp = structuredClone(nowProject);
              temp.description = e.target.value;
              setNowProject(temp);
            }}
          />
          <TextField
            id="maxUser"
            label="Project max user"
            type="number"
            fullWidth
            value={nowProject.maxUser}
            onChange={(e) => {
              let temp = structuredClone(nowProject);
              temp.maxUser = Number(e.target.value);
              setNowProject(temp);
            }}
          />
          <Box sx={{ display: "flex", justifyContent: "center" }}>
            <Button
              variant="outlined"
              sx={{ textTransform: "capitalize" }}
              onClick={handleSaveProject}
            >
              {isEdit ? "Update" : "Add Project"}
            </Button>
          </Box>
        </Box>
      </Modal>
    </Box>
  );
};
export default ManagerHomePage;
