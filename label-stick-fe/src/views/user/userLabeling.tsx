import fetchGetAssignmentByUserId from "@apolloClient/query/assignment/getAssignmentByUserID";
import fetchGetSentenceByIds from "@apolloClient/query/sentence/getSentenceById";
import {
  Autocomplete,
  Box,
  Button,
  Chip,
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
import TurnedInNotIcon from "@mui/icons-material/TurnedInNot";
import { useEffect, useRef, useState } from "react";
import { useParams } from "react-router-dom";
import fetchGetLabels from "@apolloClient/query/label/getLabels";
import fetchGetAssignments from "@apolloClient/query/assignment/getAssignments";
import { useAppSelector } from "@redux/hooks";
import fetchAddLabelsToSentence from "@apolloClient/mutation/label/addLabelsToSentence";
import fetchGetSentenceLabels from "@apolloClient/query/label/getLabelBySentenceId";

const UserLabeling: React.FC = () => {
  let { assignmentId } = useParams();
  const [sentences, setSentences] = useState<Sentence[]>([]);
  const [labels, setLabels] = useState<Label[]>([]);
  const [labelSentence, setLabelSentence] = useState<
    { sentenceId: number; labels: string[]; nowLabelSelect: string | "" }[]
  >([]);
  const userState = useAppSelector((store) => store.user);
  const renderLabel = (sentencesID: number) => {
    let sentenceSlect = labelSentence.filter(
      (item) => item.sentenceId == sentencesID
    );
    return sentenceSlect[0]?.labels.map((item) => (
      <Chip
        key={`${sentencesID}_${item}`}
        label={item}
        color="primary"
        size="small"
        onDelete={() => {
          let nowData = structuredClone(labelSentence).filter(
            (item_) => item_.sentenceId == sentencesID
          );

          let selectedLabels = nowData[0].labels.filter(
            (label) => label != item
          );
          let nowList = structuredClone(labelSentence).map((item) => {
            if (item.sentenceId == sentencesID) {
              return { ...item, labels: selectedLabels };
            }
            return item;
          });

          setLabelSentence(nowList);
        }}
      />
    ));
  };

  const addLabelToSentence = (sentenceId: number) => {
    let nowData = structuredClone(labelSentence).filter(
      (item) => item.sentenceId == sentenceId
    );
    if (nowData[0].nowLabelSelect == "") {
      return;
    }
    if (nowData[0].labels.includes(nowData[0].nowLabelSelect)) {
      return;
    }
    let selectedLabels = structuredClone(nowData[0].labels);
    selectedLabels.push(nowData[0].nowLabelSelect);
    let nowList = structuredClone(labelSentence).map((item) => {
      if (item.sentenceId == sentenceId) {
        return { ...item, labels: selectedLabels };
      }
      return item;
    });

    setLabelSentence(nowList);
  };

  const handleAddLabelsToSentences = () => {
    labelSentence.forEach((element) => {
      let listLabels = labels.filter((label) =>
        element.labels.includes(label.name)
      );
      let listLabelsIds = listLabels.map((label) => label.id);
      if (!userState.userId) return;
      fetchAddLabelsToSentence(
        element.sentenceId,
        listLabelsIds,
        userState.userId
      ).then((res) => {
        console.log(res);
      });
    });
  };

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

  useEffect(() => {
    fetchGetAssignments()
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
              let listPromise = nowSentences.map((item) => {
                return new Promise<{
                  sentenceId: number;
                  labels: string[];
                  nowLabelSelect: string | "";
                }>((resolve, reject) => {
                  fetchGetSentenceLabels(item.id)
                    .then((res) => {
                      resolve({
                        labels: res.data?.map((label_: any) => label_?.label),
                        nowLabelSelect: "",
                        sentenceId: item.id,
                      });
                    })
                    .catch((err) => {
                      reject(err);
                    });
                });
              });
              Promise.all(listPromise).then((listResponse) => {
                setLabelSentence(structuredClone(listResponse));
              });
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

  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        gap: "32px",
        padding: "16px",
      }}
    >
      <Box
        sx={{
          width: "100%",
          display: "flex",
          flexDirection: "row",
          alignItems: "center",
          justifyContent: "space-between",
        }}
      >
        <Box sx={{ flex: 1 }}>
          <h1>Label for sentences</h1>
        </Box>
        <Button variant="contained" onClick={handleAddLabelsToSentences}>
          Save
        </Button>
      </Box>

      <TableContainer component={Paper} sx={{ height: 500 }}>
        <Table
          sx={{ minWidth: 650, maxHeight: 500 }}
          aria-label="simple table"
          stickyHeader={true}
        >
          <TableHead>
            <TableRow>
              <TableCell sx={{ backgroundColor: "#ebebeb" }} width={20}>
                ID
              </TableCell>
              <TableCell align="left" sx={{ backgroundColor: "#ebebeb" }}>
                Sentences
              </TableCell>
              <TableCell
                align="left"
                sx={{ backgroundColor: "#ebebeb" }}
                width={500}
              >
                Label
              </TableCell>
              <TableCell
                align="right"
                sx={{ backgroundColor: "#ebebeb" }}
                width={100}
              >
                Action
              </TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {sentences.map((sentence, idx) => (
              <TableRow
                key={sentence.id}
                sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
              >
                <TableCell component="th" scope="row">
                  {sentence.id}
                </TableCell>
                <TableCell align="left">{sentence.sentence}</TableCell>
                <TableCell align="left">
                  <Box
                    sx={{
                      width: "100%",
                      display: "flex",
                      flexDirection: "row",
                      flexWrap: "wrap",
                      gap: "8px",
                    }}
                  >
                    {renderLabel(sentence.id)}
                  </Box>
                </TableCell>
                <TableCell align="right">
                  <Box
                    sx={{
                      display: "flex",
                      gap: "8px",
                      justifyContent: "flex-end",
                      alignItems: "center",
                    }}
                  >
                    <Stack spacing={2} sx={{ width: 175 }}>
                      <Autocomplete
                        id={"select_label_" + sentence.id}
                        freeSolo
                        value={
                          labelSentence.filter(
                            (item) => item.sentenceId == sentence.id
                          )[0]?.nowLabelSelect || ""
                        }
                        onChange={(event: any, newValue: string | null) => {
                          let newList = structuredClone(labelSentence).map(
                            (item) => {
                              if (item.sentenceId == sentence.id) {
                                return {
                                  ...item,
                                  nowLabelSelect: newValue ? newValue : "",
                                };
                              }
                              return item;
                            }
                          );
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
                        color="secondary"
                      >
                        <TurnedInNotIcon />
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
