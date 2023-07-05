import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { useEffect, useState } from "react";
import { Container, Link } from "@mui/material";
import fetchGetAssignmentByUserId from "@apolloClient/query/assignment/getAssignmentByUserID";

const AssignMePage: React.FC = () => {
  const [assignments, setAssignments] = useState<any>([]);

  useEffect(() => {
    const userId = 1;
    fetchGetAssignmentByUserId(userId).then((res) => setAssignments(res.data));
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
                    <Link href="/user">View assign</Link>
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
