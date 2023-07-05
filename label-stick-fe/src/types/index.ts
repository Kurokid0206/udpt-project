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
