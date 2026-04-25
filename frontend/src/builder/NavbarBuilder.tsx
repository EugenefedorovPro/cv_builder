import { Nav, Navbar, NavDropdown, Container } from "react-bootstrap";
// import "bootstrap/dist/css/bootstrap.min.css";
// import "../components/Navbar.css";
import { useLang, LangArray, LangValues } from "../contexts/LangContext";
import { UseFetchDocx } from "../api/UseFetchDocx";
import { useAuth } from "../contexts/AuthContext";

const NavbarBuilder = () => {
  const { lang, setLang } = useLang();
  const { isAuthenticated, logout } = useAuth();

  const handleSelect = (eventKey: string | null) => {
    const languages: LangArray = {
      "1": "eng",
      "2": "ukr",
      "3": "rus",
    };

    if (eventKey) {
      setLang(languages[eventKey as LangValues]);
    }
  };

  const url: string = "http://localhost:8002/generate_docx/";
  const filename: string = "cv.docx";
  const { loading, error, download } = UseFetchDocx(url, filename);

  const handleSaveClick = () => {
    download();
    console.log(loading);
    console.log(error);
  };

  const handleLogoutClick = async () => {
    await logout();
  };

  console.log("isAuthenticated in Navbar");
  console.log(isAuthenticated);

  return (
    <Navbar expand="sm" className="sticky-lg-top">
      <Container className="m-0 flex-lg-column align-items-start">
        <Navbar.Brand className="" href="#home">
          CV
        </Navbar.Brand>

        <Navbar.Toggle className="toggle-button" aria-controls="basic-nav-dropdown" />
        <Navbar.Collapse className="">
          <Nav variant="" defaultActiveKey="/" className="flex-lg-column">
            <Nav.Item>
              <Nav.Link href="#cases">User</Nav.Link>
            </Nav.Item>

            <Nav.Item>
              <Nav.Link href="#why-me">Occupation</Nav.Link>
            </Nav.Item>

            <Nav.Item>
              <Nav.Link href="#feedback">Manifest</Nav.Link>
            </Nav.Item>

            <Nav.Item>
              <Nav.Link href="#feedback">Photo</Nav.Link>
            </Nav.Item>

            <Nav.Item>
              <Nav.Link href="#feedback">Header</Nav.Link>
            </Nav.Item>

            <Nav.Item>
              <Nav.Link href="#feedback">Hard Skills</Nav.Link>
            </Nav.Item>

            <Nav.Item>
              <Nav.Link href="#feedback">Soft Skills</Nav.Link>
            </Nav.Item>

            <Nav.Item>
              <Nav.Link href="#feedback">Experience</Nav.Link>
            </Nav.Item>

            <Nav.Item>
              <Nav.Link href="#feedback">Interests</Nav.Link>
            </Nav.Item>

            <Nav.Item>
              <Nav.Link href="#feedback">Languages</Nav.Link>
            </Nav.Item>

            <Nav.Item>
              <Nav.Link href="#feedback">Cases</Nav.Link>
            </Nav.Item>

            <Nav.Item>
              <Nav.Link href="#feedback">Why me</Nav.Link>
            </Nav.Item>

            <Nav.Item>
              <Nav.Link
                as="span"
                onClick={handleSaveClick}
                style={{ cursor: "pointer" }}
              >
                Save as Word
                {loading === "loading..." && <div>Downloading...</div>}
                {error && <div>Error: {error.message}</div>}
              </Nav.Link>
            </Nav.Item>

            {isAuthenticated ? (
              <Nav.Item>
                <Nav.Link
                  as="span"
                  onClick={handleLogoutClick}
                  style={{ cursor: "pointer" }}
                >
                  Logout
                </Nav.Link>
              </Nav.Item>
            ) : (
              <Nav.Item>
                <Nav.Link href="/login">Login</Nav.Link>
              </Nav.Item>
            )}

            <NavDropdown title={lang} onSelect={handleSelect}>
              <NavDropdown.Item eventKey="1">ENG</NavDropdown.Item>
              <NavDropdown.Item eventKey="2">UKR</NavDropdown.Item>
              <NavDropdown.Item eventKey="3">RUS</NavDropdown.Item>
            </NavDropdown>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default NavbarBuilder;
