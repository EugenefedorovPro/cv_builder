import { Col, Container, Row, Stack } from "react-bootstrap";
import { Outlet } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import NavbarCV from "../components/Navbar";
import HeaderCV from "../components/HeaderCV";
import HardSkillsCV from "../components/HardSkills";
import ProjectsCV from "../components/Projects";
import SoftSkillsCV from "../components/SoftSkillsCV";
import EducationCV from "../components/EducationCV";
import ExperienceCV from "../components/ExperienceCV";
import InterestCV from "../components/InterestsCV";
import NaturalLangCV from "../components/NaturalLangCV";
import "./Layout.styles.css";
import { LangProvider } from "../contexts/LangContext";

const Layout = () => {
  return (
    <LangProvider>
      <Container fluid className="overall-background">
        <Row>
          <Col
            lg={{ span: 1, order: 1 }}
            md={{ span: 12, order: 1 }}
            sm={{ span: 12, order: 1 }}
            xs={{ span: 12, order: 1 }}
            className="navbar-col flex-lg-column"
          >
            <NavbarCV />
          </Col>

          <Col
            lg={{ span: 9, order: 2 }}
            md={{ span: 12, order: 1 }}
            sm={{ span: 12, order: 1 }}
            xs={{ span: 12, order: 1 }}
          >
            <Row className="flex-column">
              <Col className="header-col">
                <HeaderCV />
              </Col>

              <Col className="p-0 d-block d-lg-none">
                <HardSkillsCV />
              </Col>

              <Col className="p-0">
                <Stack>
                  <div>
                    <ProjectsCV />
                  </div>

                  <div>
                    <ExperienceCV />
                  </div>

                  <div>
                    <SoftSkillsCV />
                  </div>

                  <div>
                    <EducationCV />
                  </div>

                  <div>
                    <NaturalLangCV />
                  </div>

                  <div>
                    <InterestCV />
                  </div>

                  <Outlet />
                </Stack>
              </Col>
            </Row>
          </Col>

          <Col
            className="hard-skills-col d-none d-lg-block flex-lg-column"
            lg={{ span: 2, order: 4 }}
            md={{ span: 12, order: 1 }}
            sm={{ span: 12, order: 1 }}
            xs={{ span: 12, order: 1 }}
          >
            <HardSkillsCV />
          </Col>
        </Row>
      </Container>
    </LangProvider>
  );
};

export default Layout;
