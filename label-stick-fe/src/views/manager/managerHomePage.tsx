import fetchGetProjectsByUserId from "@apolloClient/query/project/getProjectByUserId";
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

const initProject: Project = {
  id: 0,
  name: "",
  description: "",
  maxUser: 0,
};

const ManagerHomePage: React.FC = () => {
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
      console.log("update call");
    } else {
      fetchCreateProject(
        nowProject.name,
        nowProject.description,
        nowProject.maxUser
      ).then((response) => {
        console.log(response);
      });
    }
  };

  useEffect(() => {
    fetchGetProjectsByUserId(1).then((response) => {
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
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell align="right">Name</TableCell>
              <TableCell align="right">Description</TableCell>
              <TableCell align="right">Max user</TableCell>
              <TableCell align="right">Action</TableCell>
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
