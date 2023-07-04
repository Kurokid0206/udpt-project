import fetchGetDocuments from "@apolloClient/query/documents/getDocuments";
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
  Container,
  Fab,
  FormControl,
  FormLabel,
  Input,
  Modal,
  Typography,
} from "@mui/material";
import { Label } from "@mui/icons-material";

const DocumentPage: React.FC = () => {
  const [documents, setDocuments] = useState<any>([]);
  const [openAddModal, setOpenAddModal] = useState<boolean>(false);

  useEffect(() => {
    fetchGetDocuments().then((res) => setDocuments(res.data));
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

  return (
    <Container>
      <h1>Document manager</h1>
      <TableContainer component={Paper} sx={{ marginTop: 1 }}>
        <Table sx={{ minWidth: 650 }} aria-label="caption table">
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell align="right">Document Name</TableCell>
              <TableCell align="right">Document URL</TableCell>
              <TableCell align="right">Type</TableCell>
              <TableCell align="right">Project</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {documents &&
              documents.map((row: any) => (
                <TableRow key={row.id}>
                  <TableCell component="th" scope="row">
                    {row.id}
                  </TableCell>
                  <TableCell align="right">{row.name}</TableCell>
                  <TableCell align="right">{row.documentUrl}</TableCell>
                  <TableCell align="right">{row.documentType}</TableCell>
                  <TableCell align="right">{row.projectId}</TableCell>
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
          <Typography id="modal-modal-title" variant="h6" component="h2">
            Add Document
          </Typography>
          <Box>
            <FormControl defaultValue="" required>
              <FormLabel>Name test</FormLabel>
              <Input placeholder="Type in here…" />
            </FormControl>
          </Box>
        </Box>
      </Modal>
    </Container>
  );
};
export default DocumentPage;
