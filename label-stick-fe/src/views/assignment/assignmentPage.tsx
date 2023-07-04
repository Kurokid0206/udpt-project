import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import AddIcon from "@mui/icons-material/Add";
import { useEffect, useState } from "react";
import {
  Box,
  Button,
  Checkbox,
  Container,
  Fab,
  FormControl,
  FormLabel,
  Input,
  InputLabel,
  ListItemText,
  MenuItem,
  Modal,
  OutlinedInput,
  Select,
  SelectChangeEvent,
  TextField,
  Typography,
} from "@mui/material";
import fetchGetAssignments from "@apolloClient/query/assignment/getAssignments";
import createAssignments from "@apolloClient/query/assignment/createAssignments";

const AssignmentPage: React.FC = () => {
  const [assignments, setAssignments] = useState<any>([]);
  const [openAddModal, setOpenAddModal] = useState<boolean>(false);
  const [assignmentName, setAssignmentName] = useState<string>("");
  const [addSentences, setAddSentences] = useState<number[]>([]);
  const [assignToUser, setAssignToUser] = useState<number>(-1);
  const [assignType, setAssignType] = useState<string>("");

  useEffect(() => {
    fetchGetAssignments().then((res) => setAssignments(res.data));
  }, []);

  const styleModal = {
    position: "absolute",
    top: "50%",
    left: "50%",
    transform: "translate(-50%, -50%)",
    width: 400,
    bgcolor: "background.paper",
    border: "1px solid #ccc",
    borderRadius: "8px",
    boxShadow: 24,
    px: 4,
    py: 3,
  };

  const sentences = [
    { id: 1, name: "sentence 1" },
    { id: 2, name: "sentence 2" },
  ];

  const handleChange = (event: SelectChangeEvent<typeof addSentences>) => {
    setAddSentences(event.target.value as number[]);
  };

  const handleChangeUserSelect = (event: SelectChangeEvent) => {
    setAssignToUser(Number(event.target.value));
  };

  const handleAddAssignment = () => {
    console.log(assignmentName);
    console.log(addSentences);
    console.log(assignToUser);
    console.log(assignType);
    if (
      assignmentName === "" ||
      assignToUser <= 0 ||
      addSentences.length === 0
    ) {
      alert("Please input assignment name");
      return;
    }

    // createAssignments(assignmentName, addSentences, assignToUser).then();
    // setOpenAddModal(false);
  };

  return (
    <Container>
      <h1>Document manager</h1>
      <TableContainer component={Paper} sx={{ marginTop: 1 }}>
        <Table sx={{ minWidth: 650 }} aria-label="caption table">
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell align="right">Assignment Name</TableCell>
              <TableCell align="right">Assign to</TableCell>
              <TableCell align="right">Assign type</TableCell>
              <TableCell align="right">from date</TableCell>
              <TableCell align="right">to date</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {assignments &&
              assignments.map((row: any) => (
                <TableRow key={row.id}>
                  <TableCell component="th" scope="row">
                    {row.id}
                  </TableCell>
                  <TableCell align="right">{row.name}</TableCell>
                  <TableCell align="right">{row.userId}</TableCell>
                  <TableCell align="right">{row.assignType}</TableCell>
                  <TableCell align="right">{row.fromDate}</TableCell>
                  <TableCell align="right">{row.toDate}</TableCell>
                </TableRow>
              ))}
          </TableBody>
        </Table>
      </TableContainer>
      <Fab
        color="primary"
        aria-label="add"
        sx={{ position: "fixed", bottom: "42px", right: "56px" }}
        onClick={() => setOpenAddModal(true)}
      >
        <AddIcon />
      </Fab>

      {/* Model add document */}
      <Modal
        open={openAddModal}
        onClose={() => setOpenAddModal(false)}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={styleModal}>
          <Typography
            id="modal-modal-title"
            variant="h6"
            component="h2"
            sx={{ mb: 4 }}
          >
            Add Document
          </Typography>
          <Box>
            <FormControl defaultValue="" required sx={{ mb: 3, width: "100%" }}>
              <TextField
                value={assignmentName}
                onChange={(e) => setAssignmentName(e.target.value)}
                id="outlined-basic"
                label="Name"
                variant="outlined"
              />
            </FormControl>

            <FormControl sx={{ mb: 3, width: "100%" }}>
              <InputLabel id="demo-multiple-checkbox-label">
                Sentences
              </InputLabel>
              <Select
                labelId="demo-multiple-checkbox-label"
                id="demo-multiple-checkbox"
                multiple
                value={addSentences}
                onChange={(e) => handleChange(e)}
                input={<OutlinedInput label="Sentences" />}
                renderValue={(selected) => selected.join(", ")}
              >
                {sentences.map((sentence) => (
                  <MenuItem key={sentence?.id} value={sentence?.id}>
                    <Checkbox
                      checked={addSentences.indexOf(sentence.id) > -1}
                    />
                    <ListItemText primary={sentence.name} />
                  </MenuItem>
                ))}
              </Select>
            </FormControl>
            {/* userid */}
            <FormControl sx={{ mb: 3, width: "100%" }}>
              <InputLabel id="demo-simple-select-autowidth-label">
                Assign to user
              </InputLabel>
              <Select
                labelId="demo-simple-select-autowidth-label"
                id="demo-simple-select-autowidth"
                value={assignToUser.toString()}
                onChange={(e) => handleChangeUserSelect(e)}
                autoWidth
                label="Assign to user"
              >
                <MenuItem value={10}>Twenty</MenuItem>
                <MenuItem value={21}>Twenty one</MenuItem>
                <MenuItem value={22}>Twenty one and a half</MenuItem>
              </Select>
            </FormControl>
            {/* assign type */}
            <FormControl sx={{ mb: 3, width: "100%" }}>
              <InputLabel id="demo-simple-select-autowidth-label">
                Assign type
              </InputLabel>
              <Select
                labelId="demo-simple-select-autowidth-label"
                id="demo-simple-select-autowidth"
                value={assignType}
                onChange={(e) => setAssignType(e.target.value)}
                autoWidth
                label="Assign type"
              >
                <MenuItem value={"LABEL"}>LABEL</MenuItem>
              </Select>
            </FormControl>
          </Box>
          <Box sx={{ display: "flex" }}>
            <Button variant="contained" onClick={handleAddAssignment}>
              Contained
            </Button>
          </Box>
        </Box>
      </Modal>
    </Container>
  );
};
export default AssignmentPage;
