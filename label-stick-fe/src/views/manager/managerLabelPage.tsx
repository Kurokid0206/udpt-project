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
import createLabel from "@apolloClient/mutaion/label/createLabel";
import fetchGetLabels from "@apolloClient/query/label/getLabels";
import updateLabel from "@apolloClient/mutaion/label/updateLabel";

const initLabel: Label = {
  id: 0,
  name: "",
};

const ManagerLabelPage: React.FC = () => {
  const [Labels, setLabels] = useState<Label[]>([]);
  const [isOpenModal, setIsOpenModal] = useState<boolean>(false);
  const [nowLabel, setNowLabel] = useState<Label>(initLabel);
  const [isEdit, setIsEdit] = useState<boolean>(false);

  // event handler
  const onClickEditLabel = (LabelId: number) => {
    const nowEdit: Label[] = Labels.filter((item) => item.id === LabelId);
    setNowLabel(nowEdit[0]);
    setIsEdit(true);
    setIsOpenModal(true);
  };
  const onCloseModal = () => {
    setNowLabel(initLabel);
    setIsEdit(false);
    setIsOpenModal(false);
  };
  const handleSaveLabel = () => {
    if (isEdit) {
      updateLabel(nowLabel.id, nowLabel.name).then((response) => {
        if (response.statusCode === 200) {
          const list_temp_ = Labels.map((item) => {
            if (item.id === nowLabel.id) {
              const temp: Label = {
                id: item.id,
                name: response.data.name,
              };
              return temp;
            }
            return item;
          });
          setLabels(list_temp_);
          onCloseModal();
        } else {
          console.log(response.message);
        }
      });
    } else {
      createLabel(nowLabel.name).then((response) => {
        if (response.statusCode === 200) {
          const temp: Label = {
            id: response.data.id,
            name: response.data.name,
          };
          const list_temp = structuredClone(Labels);
          list_temp.push(temp);
          setLabels(list_temp);
          onCloseModal();
        } else {
          console.log(response.message);
        }
      });
    }
  };

  useEffect(() => {
    fetchGetLabels().then((response) => {
      const Label_data: Label[] = [];
      response.data?.forEach((item: Label) => {
        Label_data.push({
          id: item.id,
          name: item.name,
        });
      });
      setLabels(Label_data);
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
          <h1>Label</h1>
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
          Add Label
        </Fab>
      </Box>
      <TableContainer component={Paper} sx={{ height: 500 }}>
        <Table
          sx={{ minWidth: 650, height: 500 }}
          aria-label="simple table"
          stickyHeader={true}
        >
          <TableHead>
            <TableRow>
              <TableCell sx={{ backgroundColor: "#ebebeb" }}>ID</TableCell>
              <TableCell align="right" sx={{ backgroundColor: "#ebebeb" }}>
                Label Name
              </TableCell>
              <TableCell align="right" sx={{ backgroundColor: "#ebebeb" }}>
                Action
              </TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {Labels.map((Label, idx) => (
              <TableRow
                key={Label.id + idx}
                sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
              >
                <TableCell component="th" scope="row">
                  {Label.id}
                </TableCell>
                <TableCell align="right">{Label.name}</TableCell>
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
                          onClickEditLabel(Label.id);
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
            position: "absolute",
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
              Add new Label
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
            label="Label name"
            fullWidth
            value={nowLabel.name}
            onChange={(e) => {
              const temp = structuredClone(nowLabel);
              temp.name = e.target.value;
              setNowLabel(temp);
            }}
          />
          <Box sx={{ display: "flex", justifyContent: "center" }}>
            <Button
              variant="outlined"
              sx={{ textTransform: "capitalize" }}
              onClick={handleSaveLabel}
            >
              {isEdit ? "Update" : "Add Label"}
            </Button>
          </Box>
        </Box>
      </Modal>
    </Box>
  );
};
export default ManagerLabelPage;
