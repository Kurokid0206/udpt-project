interface NavBarElement {
  name: string;
  path: string;
  icon: React.ReactNode;
}

interface RouterElement {
  path: string;
  element: React.ReactNode;
}

interface Project {
  id: number;
  name: string;
  description: string;
  maxUser: number;
}

interface Label {
  id: number;
  name: string;
}

interface Document {
  id: number;
  name: string;
  documentUrl: string;
  documentType: string;
  projectId: number;
}

interface Sentence {
  id: number;
  name: string;
  sentence: string;
  documentId: number;
}
