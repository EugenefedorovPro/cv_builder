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
            className="p-0"

        >
            <Row
                className=""
            >

                <Col
                    lg={{span: 2, order: 1}}
                    md={{span: 12, order: 1}}
                    sm={{span: 12, order: 1}}
                    xs={{span: 12, order: 1}}

                    className="navbar-col  flex-lg-column"
                >
                    {<NavbarCV/>}
                </Col>
                <Col
                    className="flex-lx-column bg-info"
                    lg={{span: 8, order: 2}}
                    md={{span: 12, order: 1}}
                    sm={{span: 12, order: 1}}
                    xs={{span: 12, order: 1}}
                >
                    {<HeaderCV/>}
                </Col>

                <Col
                    className="outer-body-col flex-lg-column"
                    lg={{span: 8, order: 3, offset: 2}}
                    md={{span: 12, order: 1}}
                    sm={{span: 12, order: 1}}
                    xs={{span: 12, order: 1}}

                >

                    <Stack
                        gap={0}
                        className=""
                    >

                        <div className="hard-skills-placeholder text-center">
                            {<ManifestCV/>}
                        </div>

                        <div className="projects-placeholder text-center">
                            {<ProjectsCV/>}
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
                    className="d-lg-flex flex-lg-column position-relative bg-warning"
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
