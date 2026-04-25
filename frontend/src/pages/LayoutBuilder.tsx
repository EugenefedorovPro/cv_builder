import { Col, Container, Row } from "react-bootstrap";
// import "bootstrap/dist/css/bootstrap.min.css";
import NavbarBuilder from "../builder/NavbarBuilder";
// import "./Layout.styles.css";

const LayoutBuilder = () => {
  return (
    <Container fluid className="overall-background">
      <Row>
        <Col
          lg={{ span: 2 , order: 1 }}
          md={{ span: 12, order: 1 }}
          sm={{ span: 12, order: 1 }}
          xs={{ span: 12, order: 1 }}
          className="navbar-col flex-lg-column"
        >
          <NavbarBuilder />
        </Col>

        <Col
          lg={{ span: 10, order: 2 }}
          md={{ span: 12, order: 1 }}
          sm={{ span: 12, order: 1 }}
          xs={{ span: 12, order: 1 }}
        >
          <Row className="flex-column">
            <Col className="header-col">
              <div>Placeholder First</div>
            </Col>

          </Row>
        </Col>

      </Row>
    </Container>
  );
};

export default LayoutBuilder;
