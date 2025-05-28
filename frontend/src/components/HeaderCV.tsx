import React from "react";
import {Image, ListGroup, Container, Col, Row, Figure} from "react-bootstrap";

interface HeaderCVInterface {
    name: string,
    phone: string,
    email: string,
    linkedin?: string,
    github?: string,
    country?: string,
    city?: string,
    district?: string,
    photo?: string,
}


const HeaderCV: React.FC<HeaderCVInterface> = (props) => {

    return (
        <Container fluid className="g-0">
            <Row className="">
                <Col xs={2} className="d-none d-md-block">
                    <Image
                        thumbnail
                        width={150}
                        height={200}
                        alt="150x200"
                        src="https://placeholder.pics/svg/150x200"
                    />
                </Col>
                <Col sm={12} md={10} lg={10} className="">
                    <ListGroup horizontal className="flex-wrap">
                        <ListGroup.Item><b>Name</b>: {props.name}</ListGroup.Item>
                        <ListGroup.Item><b>Phone</b>: {props.phone}</ListGroup.Item>
                        <ListGroup.Item><b>Email</b>: {props.email}</ListGroup.Item>
                        <ListGroup.Item><b>LinkedIn</b>: {props.linkedin}</ListGroup.Item>
                        <ListGroup.Item><b>GitHub</b>: {props.github}</ListGroup.Item>
                        <ListGroup.Item><b>Country</b>: {props.country}</ListGroup.Item>
                        <ListGroup.Item><b>City</b>: {props.city}</ListGroup.Item>
                        <ListGroup.Item><b>District</b>: {props.district}</ListGroup.Item>
                    </ListGroup>

                </Col>

            </Row>

        </Container>

    )

}

export default HeaderCV;