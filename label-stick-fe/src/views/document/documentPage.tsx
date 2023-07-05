import {
  Box,
  Button,
  Fab,
  IconButton,
  MenuItem,
  Modal,
  Paper,
  Select,
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
import fetchDocuments from "@apolloClient/query/document/getDocumentByProjectId";
import fetchCreateDocument from "@apolloClient/mutaion/document/createDocument";

const initDocument: Document = {
  id: 0,
  name: "",
  documentUrl: "",
  documentType: "",
  projectId: 1,
};
const DocumentPage: React.FC = () => {
  const [documents, setDocuments] = useState<Document[]>([]);
  const [isOpenModal, setIsOpenModal] = useState<boolean>(false);
  const [nowDocument, setNowDocument] = useState<Document>(initDocument);

  const createDocument = () => {
    fetchCreateDocument(
      nowDocument.name,
      nowDocument.documentType,
      nowDocument.projectId,
      nowDocument.documentUrl
    ).then((response) => {
      console.log(response);
    });
  };
  const handleUploadFile = (file: File) => {
    const data = new FormData();
    data.append("file", file ?? new File([], ""));
    data.append("project_id", nowDocument.projectId.toString());

    fetch("http://103.176.179.83:8000/upload-file", {
      method: "POST",
      body: data,
    }).then((response) => {
      const data = response.json();
      nowDocument.documentUrl = data?.url;
    });
  };
  useEffect(() => {
    fetchDocuments().then((response) => {
      let documents_data: Document[] = [];
      response.data?.forEach((item: Document) => {
        documents_data.push({
          id: item.id,
          name: item.name,
          documentUrl: item.documentUrl,
          documentType: item.documentType,
          projectId: item.projectId,
        });
      });
      setDocuments(documents_data);
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
          <h1>Document</h1>
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
          Add document
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
            {documents.map((document, idx) => (
              <TableRow
                key={document.id + idx}
                sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
              >
                <TableCell component="th" scope="row">
                  {document.id}
                </TableCell>
                <TableCell align="right">{document.name}</TableCell>
                <TableCell align="right">{document.documentType}</TableCell>
                <TableCell align="right">{document.documentUrl}</TableCell>
                <TableCell align="right">
                  <Box
                    sx={{
                      display: "flex",
                      gap: "8px",
                      justifyContent: "flex-end",
                    }}
                  >
                    <Box>
                      <IconButton onClick={() => {}}>
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
          <TextField
            label="Name"
            variant="outlined"
            onChange={(event) => {
              nowDocument.name = (event.target.value ?? "") as string;
            }}
          />
          <Select
            onChange={(event) => {
              nowDocument.documentType = (event.target.value ??
                "QUESTION") as string;
            }}
          >
            <MenuItem value={"QUESTION"}>QUESTION</MenuItem>
            <MenuItem value={"TRANSLATE"}>TRANSLATE</MenuItem>
            <MenuItem value={"ENTITY"}>ENTITY</MenuItem>
            <MenuItem value={"SYNONYMOUS"}>SYNONYMOUS</MenuItem>
            <MenuItem value={"TRUE_FALSE"}>TRUE_FALSE</MenuItem>
            <MenuItem value={"ANSWER"}>ANSWER</MenuItem>
          </Select>
          <TextField
            label="project_id"
            variant="outlined"
            onChange={(event) => {
              nowDocument.projectId = Number(event.target.value ?? 1);
            }}
          />
          <input
            type="file"
            onChange={(e) => {
              handleUploadFile(e.target.files![0]);
            }}
          />

          <Button
            variant="contained"
            onClick={() => {
              createDocument();
            }}
          >
            Add
          </Button>
        </Box>
      </Modal>
    </Box>
  );
};
export default DocumentPage;
