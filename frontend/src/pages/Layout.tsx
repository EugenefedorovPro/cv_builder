import {Col, Container, Row, Stack} from "react-bootstrap";
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import NavbarCV from "../components/Navbar";

const Layout = () => {

    return (<>
        <Container
            fluid
            className="p-0"

        >
            <Row
                className="g-0"
            >

                <Col
                    lg={2}
                    md={12}
                    sm={12}
                    xs={12}
                    className="navbar-col d-lg-flex flex-lg-column bg-info"
                >
                    {<NavbarCV/>}
                </Col>

                <Col
                    lg={10}
                    md={12}
                    sm={12}
                    xs={12}
                    className="main-content bg-warning d-lg-flex flex-lg-column position-relative"

                >

                    <Row>

                        <Col
                            lg={{span: 9, order: 1}}
                            md={{span: 12, order: 2}}
                            sm={{span: 12, order: 2}}
                            xs={{span: 12, order: 2}}
                        >
                            <Stack
                                gap={3}
                                style={{"height": "100vh"}}
                            >
                                <div className="header-placeholder text-center">
                                    <h3>HeaderCV</h3>
                                </div>

                                <div className="hard-skills-placeholder text-center">
                                    <h3>Manifest</h3>
                                </div>

                                <div className="cases-placeholder text-center">
                                    <h3>Experience</h3>
                                </div>

                                <div className="why-me-placeholder text-center">
                                    <h3>Soft skills</h3>
                                </div>

                                <div className="feedback-placeholder text-center">
                                    <h3>Hobbies</h3>
                                </div>


                            </Stack>


                        </Col>

                        <Col
                            lg={{span: 3, order: 2}}
                            md={{span: 12, order: 1}}
                            sm={{span: 12, order: 1}}
                            xs={{span: 12, order: 1}}
                            className="hard-skills-col bg-success d-lg-flex flex-lg-column position-relative"
                        >
                            <div
                                className="hardskills-placeholder text-center"
                            >
                                <h3>Hard Skills</h3>
                            </div>
                        </Col>

                    </Row>


                </Col>


            </Row>

        </Container>

    </>)
};

export default Layout;
