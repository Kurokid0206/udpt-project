import fetchGetAssignmentByUserId from "@apolloClient/query/assignment/getAssignmentByUserID";
import fetchGetSentenceByIds from "@apolloClient/query/sentence/getSentenceById";
import {
  Autocomplete,
  Box,
  IconButton,
  Paper,
  Stack,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  TextField,
} from "@mui/material";
import EditIcon from "@mui/icons-material/Edit";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import fetchGetLabels from "@apolloClient/query/label/getLabels";

const UserLabeling: React.FC = () => {
  let { assignmentId } = useParams();
  const [sentences, setSentences] = useState<Sentence[]>([]);
  const [labels, setLabels] = useState<Label[]>([]);
  const [labelSentence, setLabelSentence] = useState<
    { sentenceId: number; labels: string[]; nowLabelSelect: string | "" }[]
  >([]);

  const addLabelToSentence = (sentenceId: number) => {
    let nowData = labelSentence.filter((item) => item.sentenceId == sentenceId);
  };

  useEffect(() => {
    fetchGetAssignmentByUserId(1)
      .then((response) => {
        if (response.statusCode === 200) {
          let nowSentenceIds: string[] = [];
          response.data?.forEach(
            (element: { id: string | undefined; sentenceIds: string[] }) => {
              if (Number(element.id) === Number(assignmentId)) {
                nowSentenceIds = element.sentenceIds;
              }
            }
          );
          if (nowSentenceIds.length === 0) {
            console.log("No sentences");
            return;
          }
          let nowSentences: Sentence[] = [];
          fetchGetSentenceByIds(nowSentenceIds.map((id) => Number(id))).then(
            (sentences_response) => {
              sentences_response.data.forEach(
                (element: {
                  id: any;
                  name: any;
                  sentence: any;
                  documentId: any;
                }) => {
                  nowSentences.push({
                    id: element.id,
                    name: element.name,
                    sentence: element.sentence,
                    documentId: element.documentId,
                  });
                }
              );
              setSentences(nowSentences);
              let nowSentenceLabel: {
                sentenceId: number;
                labels: string[];
                nowLabelSelect: string | "";
              }[] = [];
              nowSentences.forEach((item) => {
                nowSentenceLabel.push({
                  labels: [],
                  nowLabelSelect: "",
                  sentenceId: item.id,
                });
              });
              setLabelSentence(nowSentenceLabel);
            }
          );
        } else {
          console.log(response.message);
        }
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);

  useEffect(() => {
    fetchGetLabels().then((response) => {
      if (response.statusCode === 200) {
        let nowLabels: Label[] = [];
        response.data.forEach((element: { id: any; name: any }) => {
          nowLabels.push({
            id: element.id,
            name: element.name,
          });
        });
        setLabels(nowLabels);
      } else {
        console.log(response.message);
      }
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
          <h1>Label for sentences</h1>
        </Box>
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
                Sentences
              </TableCell>
              <TableCell align="right" sx={{ backgroundColor: "#ebebeb" }}>
                Label
              </TableCell>
              <TableCell align="right" sx={{ backgroundColor: "#ebebeb" }}>
                Action
              </TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {sentences.map((sentence, idx) => (
              <TableRow
                key={sentence.id + idx}
                sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
              >
                <TableCell component="th" scope="row">
                  {sentence.id}
                </TableCell>
                <TableCell align="right">{sentence.name}</TableCell>
                <TableCell align="right">{sentence.sentence}</TableCell>
                <TableCell align="right">No labels</TableCell>
                <TableCell align="right">
                  <Box
                    sx={{
                      display: "flex",
                      gap: "8px",
                      justifyContent: "flex-end",
                    }}
                  >
                    <Stack spacing={2} sx={{ width: 300 }}>
                      <Autocomplete
                        id={"select_label_" + sentence.id}
                        freeSolo
                        value={
                          labelSentence.filter(
                            (item) => item.sentenceId == sentence.id
                          )[0].nowLabelSelect
                        }
                        onChange={(event: any, newValue: string | null) => {
                          let newList = labelSentence.map((item) => {
                            if (item.sentenceId == sentence.id) {
                              return {
                                ...item,
                                nowLabelSelect: newValue ? newValue : "",
                              };
                            }
                            return item;
                          });
                          console.log(newList);
                          setLabelSentence(newList);
                        }}
                        options={labels.map((label) => label.name)}
                        renderInput={(params) => (
                          <TextField {...params} label="freeSolo" />
                        )}
                      />
                    </Stack>
                    <Box>
                      <IconButton
                        onClick={() => {
                          addLabelToSentence(sentence.id);
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
    </Box>
  );
};
export default UserLabeling;
