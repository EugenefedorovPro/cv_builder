import {Col, Container, Row, Stack} from "react-bootstrap";
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import NavbarCV from "../components/Navbar";
import HeaderCV from "../components/HeaderCV";
import ManifestCV from "../components/Manifest";
import HardSkillsCV from "../components/HardSkills";
import ProjectsCV from "../components/Projects";
import "./Layout.styles.css";


const Layout = () => {

    return (<>
        <Container
            fluid
            className=""

        >
            <Row
                className=""
            >

                <Col
                    lg={{span: 1, order: 1}}
                    md={{span: 12, order: 1}}
                    sm={{span: 12, order: 1}}
                    xs={{span: 12, order: 1}}

                    className="flex-lg-column"
                >
                    {<NavbarCV/>}
                </Col>
                <Col
                    className=""
                    lg={{span: 9, order: 2}}
                    md={{span: 12, order: 1}}
                    sm={{span: 12, order: 1}}
                    xs={{span: 12, order: 1}}
                >
                    <Row className="flex-column">
                        <Col>
                            {<HeaderCV/>}
                        </Col>
                        <Col className="d-block d-lg-none">
                            {<HardSkillsCV/>}
                        </Col>
                        <Col>
                            <Stack
                                className=""
                            >

                                <div className="">
                                    {<ManifestCV/>}
                                </div>

                                <div className="">
                                    {<ProjectsCV/>}
                                </div>

                                <div className="">
                                    {/*<h3>Experience</h3>*/}
                                </div>

                                <div className="">
                                    {/*<h3>Soft skills</h3>*/}
                                </div>

                                <div className="">
                                    {/*<h3>Hobbies</h3>*/}
                                </div>

                            </Stack>

                        </Col>

                    </Row>

                </Col>

                <Col
                    className="d-none d-lg-block flex-lg-column"
                    lg={{span: 2, order: 4}}
                    md={{span: 12, order: 1}}
                    sm={{span: 12, order: 1}}
                    xs={{span: 12, order: 1}}
                >
                    <HardSkillsCV/>

                </Col>


            </Row>

        </Container>

    </>)
};

export default Layout;
