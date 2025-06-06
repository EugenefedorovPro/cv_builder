import React from "react";
import {Image, ListGroup, ListGroupItem, Container, Col, Row, Figure} from "react-bootstrap";
import {useFetchData, UseDataFetchInterface} from "../api/UseFetchData";
import ManifestCV from "./Manifest";

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
    const name = "Header"
    const url: string = "http://localhost:8002/header/";
    const {data, loading, error} = useFetchData<HeaderInterface>(url);

    if (loading) {
        return <div> Loading data for {name}...</div>
    }

    if (error) {
        return <div>`Error on fetching {name}: ${error}`</div>

    }

    if (!data) {
        return <div>No data on {name}</div>

    }

    return (
        <Row className="">
            <Col className="d-none d-md-block">
                <Image
                    thumbnail
                    width={150}
                    height={200}
                    alt="150x200"
                    src={`http://localhost:8002${data?.photo?.photo_url}/`}
                    className="overall-background rounded-0"
                />
            </Col>
            <Col sm={12} md={10} lg={10} className="">

                <ListGroup>
                    <ListGroupItem><h5><b>{data.first_name.toUpperCase()} {data.second_name.toUpperCase()}</b></h5>
                    </ListGroupItem>
                </ListGroup>

                <ListGroup horizontal className="flex-wrap">

                    <ListGroupItem>
                        <a href={`tel:${data.phone}`} target="_blank" rel="noopener noteferrer">{data.phone}</a>
                    </ListGroupItem>

                    <ListGroupItem>
                        <a href={`mailto:${data.email}`} target="_blank" rel="noopener noteferrer">{data.email}</a>
                    </ListGroupItem>

                    {data.github &&
                        <ListGroupItem>
                            <a href={data.github} target="_blank" rel="noopener noreferrer">github</a>
                        </ListGroupItem>
                    }
                    {data.linkedin &&
                        <ListGroupItem>
                            <a href={data.linkedin} target="_blank" rel="noopener noreferrer">LinkedIn</a>
                        </ListGroupItem>
                    }

                    {(data.country || data.city || data.district) && (
                        <ListGroupItem className="d-flex flex-wrap gap-3">

                            {data.country &&
                                <div><span className="title">Country</span>: {data.country}</div>
                            }

                            {data.city &&
                                <div><span className="title">City</span>: {data.city}</div>
                            }

                            {data.district &&
                                <div><span className="title">District</span>: {data.district}</div>
                            }
                        </ListGroupItem>

                    )}
                </ListGroup>
                {<ManifestCV/>}
            </Col>
        </Row>

    )
}

export default HeaderCV;