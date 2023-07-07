import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import AddIcon from "@mui/icons-material/Add";
import EditIcon from "@mui/icons-material/Edit";
import { useEffect, useState } from "react";
import {
  Alert,
  Box,
  Button,
  Checkbox,
  Container,
  Fab,
  FormControl,
  IconButton,
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
import fetchGetAssignmentByUserId from "@apolloClient/query/assignment/getAssignmentByUserID";
import createAssignment from "@apolloClient/mutation/assignment/createAssignment";
import fetchGetLabelers from "@apolloClient/query/user/getUsers";
import fetchGetSentenceByDocumentId from "@apolloClient/query/sentence/getSentenceByDocumentId";
import DocumentScannerIcon from "@mui/icons-material/DocumentScanner";
import { useNavigate } from "react-router-dom";
import { useAppSelector } from "@redux/hooks";

const AssignmentPage: React.FC = () => {
  const navigate = useNavigate();
  const [assignments, setAssignments] = useState<any>([]);
  const [sentences, setSentences] = useState<any>([]);
  const [users, setUsers] = useState<any>([]);
  const [openAddModal, setOpenAddModal] = useState<boolean>(false);
  const [isEdit, setIsEdit] = useState<boolean>(false);
  const [errorMessages, setErrorMessages] = useState<string>("");

  const [assignName, setAssignName] = useState<string>("");
  const [assignSentences, setAssignSentences] = useState<number[]>([]);
  const [assignToUser, setAssignToUser] = useState<number>(-1);
  const [assignType, setAssignType] = useState<string>("");
  const [assignFromDate, setAssignFromDate] = useState<string>("");
  const [assignToDate, setAssignToDate] = useState<string>("");
  const user = useAppSelector((store) => store.user);

  useEffect(() => {
    if (!user.userId) return;
    fetchGetAssignmentByUserId(user.userId).then((res) =>
      setAssignments(res.data)
    );
    fetchGetLabelers().then((res) => setUsers(res.data));
    fetchGetSentenceByDocumentId(1).then((res) => setSentences(res.data));
  }, []);

  const styleModal = {
    position: "absolute",
    top: "50%",
    left: "50%",
    transform: "translate(-50%, -50%)",
    width: 600,
    bgcolor: "background.paper",
    border: "1px solid #ccc",
    borderRadius: "8px",
    boxShadow: 24,
    px: 4,
    py: 3,
  };

  const handleChange = (event: SelectChangeEvent<typeof assignSentences>) => {
    setAssignSentences(event.target.value as number[]);
  };

  const handleChangeUserSelect = (event: SelectChangeEvent) => {
    setAssignToUser(Number(event.target.value));
  };

  const handleAddAssignment = () => {
    if (
      assignName === "" ||
      assignToUser <= 0 ||
      assignSentences.length === 0 ||
      assignType === "" ||
      assignFromDate === "" ||
      assignToDate === ""
    ) {
      setErrorMessages("Please fill all fields");
      return;
    }
    if (isEdit) {
      console.log("edit");
    } else {
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
        setErrorMessages("");
        setOpenAddModal(false);
      });
    }
  };

  const onClickAddAssignment = () => {
    setAssignName("");
    setAssignSentences([]);
    setAssignToUser(-1);
    setAssignType("");
    setAssignFromDate("");
    setAssignToDate("");
    setIsEdit(false);
    setOpenAddModal(true);
  };

  const onClickEditAssignment = (id: number) => {
    const nowEdit = assignments.filter((item: any) => item.id === id);

    setAssignName(nowEdit[0].name);
    setAssignSentences(nowEdit[0].sentenceIds);
    setAssignToUser(nowEdit[0].userId);
    setAssignType(nowEdit[0].assignType);
    setAssignFromDate(nowEdit[0].fromDate.slice(0, 10));
    setAssignToDate(nowEdit[0].toDate.slice(0, 10));
    setIsEdit(true);
    setOpenAddModal(true);
  };

  const handleCloseModal = () => {
    setErrorMessages("");
    setOpenAddModal(false);
  };

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
          <h1>Assignments</h1>
        </Box>
        <Fab
          color="primary"
          aria-label="add"
          variant="extended"
          onClick={onClickAddAssignment}
        >
          <AddIcon />
          Assign
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
                  <TableCell align="right">
                    {
                      users.filter((item: any) => item.userId == row.userId)[0]
                        ?.username
                    }
                  </TableCell>
                  <TableCell align="right">{row.assignType}</TableCell>
                  <TableCell align="right">
                    {row.fromDate.slice(0, 10)}
                  </TableCell>
                  <TableCell align="right">{row.toDate.slice(0, 10)}</TableCell>
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
                            navigate(`/user/labeling/${row.id}`);
                          }}
                        >
                          <DocumentScannerIcon />
                        </IconButton>
                        <IconButton
                          onClick={() => {
                            onClickEditAssignment(row.id);
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

      {/* Model add Assignment */}
      <Modal
        open={openAddModal}
        onClose={handleCloseModal}
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
            {errorMessages && (
              <span style={{ color: "red" }}>{errorMessages}</span>
            )}
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
                {sentences &&
                  sentences.map((sentence: any) => (
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
                {users &&
                  users.map((user: any) => {
                    return (
                      <MenuItem key={user.userId} value={Number(user.userId)}>
                        {user.username}
                      </MenuItem>
                    );
                  })}
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
                <MenuItem value={"REVIEW"}>REVIEW</MenuItem>
              </Select>
            </FormControl>
            <Box
              sx={{ display: "flex", justifyContent: "space-between", mb: 4 }}
            >
              <FormControl sx={{ mr: 3, width: "100%" }}>
                <span>From date</span>
                <Input
                  type="date"
                  value={assignFromDate}
                  onChange={(e) => {
                    setAssignFromDate(e.target.value);
                  }}
                />
              </FormControl>
              <FormControl sx={{ ml: 3, width: "100%" }}>
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
          </Box>

          <Box
            sx={{ display: "flex", width: "100%", justifyContent: "flex-end" }}
          >
            <Button
              variant="contained"
              onClick={handleAddAssignment}
              sx={{ width: "25% !important" }}
            >
              {isEdit ? "Edit" : "Add"}
            </Button>
          </Box>
        </Box>
      </Modal>
    </Box>
  );
};
export default AssignmentPage;
