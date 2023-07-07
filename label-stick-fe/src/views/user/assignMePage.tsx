import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { useEffect, useState } from "react";
import { Box, Container, IconButton, Link } from "@mui/material";
import DocumentScannerIcon from "@mui/icons-material/DocumentScanner";
import fetchGetAssignmentByUserId from "@apolloClient/query/assignment/getAssignmentByUserID";
import { useNavigate, useParams } from "react-router-dom";
import { useAppSelector } from "@redux/hooks";

const AssignMePage: React.FC = () => {
  const userState = useAppSelector((store) => store.user);
  const navigate = useNavigate();
  const [assignments, setAssignments] = useState<any>([]);

  useEffect(() => {
    if (!userState.userId) return;
    fetchGetAssignmentByUserId(userState.userId).then((res) =>
      setAssignments(res.data)
    );
  }, []);

  return (
    <Container>
      <h1>Assignment manager</h1>
      <TableContainer component={Paper} sx={{ marginTop: 1 }}>
        <Table sx={{ minWidth: 650 }} aria-label="caption table">
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell align="right">Assignment Name</TableCell>
              <TableCell align="right">Assign type</TableCell>
              <TableCell align="right">from date</TableCell>
              <TableCell align="right">to date</TableCell>
              <TableCell align="right">view assign</TableCell>
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
                      <IconButton
                        onClick={() => {
                          navigate(`/user/labeling/${row.id}`);
                        }}
                      >
                        <DocumentScannerIcon />
                      </IconButton>
                    </Box>
                  </TableCell>
                </TableRow>
              ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Container>
  );
};
export default AssignMePage;
