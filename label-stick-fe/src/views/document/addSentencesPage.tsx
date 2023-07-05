import { useState } from "react";
import { Box, Button, Container, TextField } from "@mui/material";

const AddSentencesPage: React.FC = () => {
  const [paragraph, setParagraph] = useState<string>("");

  return (
    <Container>
      <h1>Add Sentence to document</h1>
      <TextField
        id="outlined-multiline-static"
        label="Paragraph"
        value={paragraph}
        onChange={(e) => setParagraph(e.target.value)}
        multiline
        rows={20}
        sx={{ width: "100%" }}
      />
      <Box sx={{ display: "flex", justifyContent: "flex-end", marginTop: 2 }}>
        <Button variant="contained">Add</Button>
      </Box>
    </Container>
  );
};
export default AddSentencesPage;
