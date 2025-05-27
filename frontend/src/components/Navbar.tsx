import React, {useState} from 'react';
import {Col, Container, Dropdown, Nav, Navbar, Row} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

const NavbarCV = () => {
    const [language, setLanguage] = useState("EN");

    const handleSelect = (lang: any) => {
        setLanguage(lang);
        // Optional: persist in localStorage or update i18n library
    };
    return (
        <Navbar expand="md" className="bg-danger-subtle d-lg-flex flex-lg-column p-3 h-100 bg-info align-items-start">
            <Navbar.Brand className="mb-lg-auto bg-body" href="/">CV</Navbar.Brand>
            <Navbar.Toggle className=""/>
            <Navbar.Collapse className="w-100">

                <Container fluid className="h-100 d-lg-flex flex-lg-column">
                    <Row className="h-100 d-lg-flex flex-lg-column">

                        <Col className=" d-lg-flex flex-lg-column bg-info-subtle">
                            <Nav className="d-lg-flex flex-lg-column">
                                <Nav.Link href="#cases">Cases</Nav.Link>
                                <Nav.Link href="#why-me">Why me?</Nav.Link>
                                <Nav.Link href="#feedback">Feedback</Nav.Link>
                            </Nav>

                        </Col>

                        <Col className="d-lg-flex flex-lg-column bg-info">
                            <Nav className="d-lg-flex flex-lg-column h-100 bg-secondary">
                                <div className="ms-0 ms-sm-auto ms-lg-0 mt-lg-auto">

                                    <Dropdown onSelect={handleSelect}>
                                        <Dropdown.Toggle variant="light" id="language-dropdown">
                                            {language}
                                        </Dropdown.Toggle>

                                        <Dropdown.Menu>
                                            <Dropdown.Item eventKey="EN">English</Dropdown.Item>
                                            <Dropdown.Item eventKey="UA">Ukrainian</Dropdown.Item>
                                            <Dropdown.Item eventKey="RU">Russian</Dropdown.Item>
                                        </Dropdown.Menu>
                                    </Dropdown>

                                </div>
                            </Nav>

                        </Col>
                    </Row>

                </Container>


            </Navbar.Collapse>

        </Navbar>

    )
};

export default NavbarCV;

