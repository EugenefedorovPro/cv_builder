import React from "react";
import {Image, ListGroup, Container, Col, Row, Figure} from "react-bootstrap";
import {useFetchData, UseDataFetchInterface} from "../api/UseFetchData";

interface PhotoInterface {
    photo_url: string,
}

export interface HeaderInterface {
    'id': number,
    'first_name': string,
    'second_name': string,
    'phone': string,
    'email': string,
    'city'?: string,
    'country'?: string,
    'district'?: string,
    'github'?: string,
    'linkedin'?: string,
    'photo'?: PhotoInterface,
}

const HeaderCV = () => {
    const url: string = "http://localhost:8002/header/";
    const {data, loading, error} = useFetchData<HeaderInterface>(url);

    if (loading) {
        return <div>Data is loading...</div>
    }

    if (error) {
        return <div>Error while fetching data: {error}</div>
    }

    if (!data) {
        return <div>No data available</div>

    }
    return (
        <Container fluid className="g-0">
            <Row className="">
                <Col xs={2} className="d-none d-md-block">
                    <Image
                        thumbnail
                        width={150}
                        height={200}
                        alt="150x200"
                        src={`http://localhost:8002${data?.photo?.photo_url}/`}
                    />
                </Col>
                <Col sm={12} md={10} lg={10} className="">
                    <ListGroup horizontal className="flex-wrap gap-1">
                        <ListGroup.Item><h5><b>{data.first_name} {data.second_name}</b></h5></ListGroup.Item>

                        <ListGroup.Item>
                            <a href={`tel:${data.phone}`} target="_blank" rel="noopener noteferrer">{data.phone}</a>
                        </ListGroup.Item>

                        <ListGroup.Item>
                            <a href={`mailto:${data.email}`} target="_blank" rel="noopener noteferrer">{data.email}</a>
                        </ListGroup.Item>

                        {data.github &&
                            <ListGroup.Item>
                                <a href={data.github} target="_blank" rel="noopener noreferrer">github</a>
                            </ListGroup.Item>
                        }
                        {data.linkedin &&
                            <ListGroup.Item>
                                <a href={data.linkedin} target="_blank" rel="noopener noreferrer">LinkedIn</a>
                            </ListGroup.Item>
                        }

                        {(data.country || data.city || data.district) && (
                            <ListGroup.Item className="d-flex flex-wrap gap-3">

                                {data.country &&
                                    <div><b>Country</b>: {data.country}</div>
                                }

                                {data.city &&
                                    <div><b>City</b>: {data.city}</div>
                                }

                                {data.district &&
                                    <div><b>District</b>: {data.district}</div>
                                }
                            </ListGroup.Item>

                        )}

                    </ListGroup>


                </Col>
            </Row>
        </Container>

    )
}

export default HeaderCV;