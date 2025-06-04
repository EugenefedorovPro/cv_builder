import React from 'react';
import {Nav, Navbar, NavDropdown, Container, Form, Button} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

const NavbarCV = () => {

    return (
        <Navbar expand="sm">

            <Container className="m-0 flex-lg-column align-items-start">
                <Navbar.Brand className="" href="#home">CV</Navbar.Brand>

                <Navbar.Toggle aria-controls="basic-nav-dropdown"/>
                <Navbar.Collapse className="">

                    <Nav variant="" defaultActiveKey="/" className="flex-lg-column">

                        <Nav.Item>
                            <Nav.Link href="#cases">Cases</Nav.Link>
                        </Nav.Item>

                        <Nav.Item>
                            <Nav.Link href="#why-me">Why me?</Nav.Link>
                        </Nav.Item>

                        <Nav.Item>
                            <Nav.Link href="#feedback">Feedback</Nav.Link>
                        </Nav.Item>

                        <Nav.Item>
                            <Nav.Link href="#feedback">Save</Nav.Link>
                        </Nav.Item>

                        <NavDropdown title="ENG">
                            <NavDropdown.Item eventKey="1">ENG</NavDropdown.Item>
                            <NavDropdown.Item eventKey="2">UKR</NavDropdown.Item>
                            <NavDropdown.Item eventKey="3">RUS</NavDropdown.Item>
                        </NavDropdown>

                    </Nav>

                </Navbar.Collapse>
            </Container>
        </Navbar>

    )
};

export default NavbarCV;

