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
import createAssignment from "@apolloClient/mutaion/assignment/createAssignment";

const AssignmentPage: React.FC = () => {
  const [assignments, setAssignments] = useState<any>([]);
  const [openAddModal, setOpenAddModal] = useState<boolean>(false);
  const [assignName, setAssignName] = useState<string>("");
  const [assignSentences, setassignSentences] = useState<number[]>([]);
  const [assignToUser, setAssignToUser] = useState<number>(-1);
  const [assignType, setAssignType] = useState<string>("");
  const [assignFromDate, setAssignFromDate] = useState<string>("");
  const [assignToDate, setAssignToDate] = useState<string>("");

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

  const handleChange = (event: SelectChangeEvent<typeof assignSentences>) => {
    setassignSentences(event.target.value as number[]);
  };

  const handleChangeUserSelect = (event: SelectChangeEvent) => {
    setAssignToUser(Number(event.target.value));
  };

  const handleAddAssignment = () => {
    console.log(assignName);
    console.log(assignSentences);
    console.log(assignToUser);
    console.log(assignType);

    if (
      assignName === "" ||
      assignToUser <= 0 ||
      assignSentences.length === 0 ||
      assignType === "" ||
      assignFromDate === "" ||
      assignToDate === ""
    ) {
      alert("Please input assignment name");
      return;
    }

    createAssignment(
      assignName,
      assignSentences,
      assignToUser,
      assignType,
      new Date(assignFromDate).toISOString(),
      new Date(assignToDate).toISOString()
    ).then((res) => {
      setAssignments([...assignments, res.data]);
      console.log(res);
      setOpenAddModal(false);
    });
  };

  return (
    <Container>
      <h1>Assignment manager</h1>
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
              <TableCell align="right">Action</TableCell>
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
                  <TableCell align="right">
                    {row.fromDate.slice(0, 10)}
                  </TableCell>
                  <TableCell align="right">{row.toDate.slice(0, 10)}</TableCell>
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

      {/* Model add Assignment */}
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
            Add Assignment
          </Typography>
          <Box>
            <FormControl defaultValue="" required sx={{ mb: 3, width: "100%" }}>
              <TextField
                value={assignName}
                onChange={(e) => setAssignName(e.target.value)}
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
                value={assignSentences}
                onChange={(e) => handleChange(e)}
                input={<OutlinedInput label="Sentences" />}
                renderValue={(selected) => selected.join(", ")}
              >
                {sentences.map((sentence) => (
                  <MenuItem key={sentence?.id} value={sentence?.id}>
                    <Checkbox
                      checked={assignSentences.indexOf(sentence.id) > -1}
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
                <MenuItem value={1}>User 1</MenuItem>
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
            <FormControl sx={{ mb: 3, width: "100%" }}>
              <span>From date</span>
              <Input
                type="date"
                value={assignFromDate}
                onChange={(e) => {
                  setAssignFromDate(e.target.value);
                }}
              />
            </FormControl>
            <FormControl sx={{ mb: 3, width: "100%" }}>
              <span>To date</span>
              <Input
                type="date"
                value={assignToDate}
                onChange={(e) => {
                  setAssignToDate(e.target.value);
                }}
              />
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
