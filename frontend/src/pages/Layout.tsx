import {Col, Container, Row, Stack} from "react-bootstrap";
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import NavbarCV from "../components/Navbar";
import HeaderCV from "../components/HeaderCV";
import HardSkillsCV from "../components/HardSkills";
import "./Layout.styles.css";


const Layout = () => {

    return (<>
        <Container
            fluid
            className="p-0"

        >
            <Row
                className=""
            >

                <Col
                    lg={2}
                    md={12}
                    sm={12}
                    xs={12}
                    className="navbar-col d-lg-flex flex-lg-column"
                >
                    {<NavbarCV/>}
                </Col>

                <Col
                    className="outer-body-col flex-lg-column"
                    lg={10}
                    md={12}
                    sm={12}
                    xs={12}

                >

                    <Row>

                        <Col
                            className="inner-body-col"
                            lg={9}
                            md={12}
                            sm={12}
                            xs={12}
                        >
                            <Stack
                                gap={0}
                                className=""
                            >
                                <div
                                    className="header-div"
                                >
                                    {<HeaderCV/>}
                                </div>

                                <div className="hard-skills-placeholder text-center">
                                    {/*<h3>Manifest</h3>*/}
                                </div>

                                <div className="cases-placeholder text-center">
                                    {/*<h3>Experience</h3>*/}
                                </div>

                                <div className="why-me-placeholder text-center">
                                    {/*<h3>Soft skills</h3>*/}
                                </div>

                                <div className="feedback-placeholder text-center">
                                    {/*<h3>Hobbies</h3>*/}
                                </div>


                            </Stack>


                        </Col>

                        <Col
                            className="d-lg-flex flex-lg-column position-relative"
                            lg={3}
                            md={12}
                            sm={12}
                            xs={12}
                        >
                            <div
                                className=""
                            >
                                <HardSkillsCV/>

                            </div>
                        </Col>

                    </Row>


                </Col>


            </Row>

        </Container>

    </>)
};

export default Layout;
