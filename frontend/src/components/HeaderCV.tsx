import React from "react";
import {Image, ListGroup, ListGroupItem, Container, Col, Row, Figure} from "react-bootstrap";
import {useFetchData, UseDataFetchInterface} from "../api/UseFetchData";
import ManifestCV from "./Manifest";

interface PhotoInterface {
    photo_url: string,
}

export interface BlockNamesInterface {
    github_title?: string,
    linkedin_title?: string,
    country_title?: string,
    city_title?: string,
    district_title?: string,
}

export interface HeaderInterface {
    id: number,
    first_name: string,
    second_name: string,
    phone: string,
    email: string,
    city?: string,
    country?: string,
    district?: string,
    github?: string,
    linkedin?: string,
    photo?: PhotoInterface,
}

export type HeaderBlockType = {
    header: HeaderInterface,
    block_names: BlockNamesInterface,
}

const HeaderCV = () => {
    const name = "Header"
    const url: string = "http://localhost:8002/header/";
    const {data, loading, error} = useFetchData<HeaderBlockType>(url);

    if (loading) {
        return <div> Loading data for {name}...</div>
    }

    if (error) {
        return <div>`Error on fetching {name}: ${error}`</div>

    }

    if (!data) {
        return <div>No data on {name}</div>

    }

    const {header, block_names} = data;

    if (!header || !block_names) {
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
                    src={`http://localhost:8002${header?.photo?.photo_url}/`}
                    className="overall-background rounded-0"
                />
            </Col>
            <Col sm={12} md={10} lg={10} className="">

                <ListGroup>
                    <ListGroupItem><h5><b>{header.first_name.toUpperCase()} {header.second_name.toUpperCase()}</b></h5>
                    </ListGroupItem>
                </ListGroup>

                <ListGroup horizontal className="flex-wrap">

                    <ListGroupItem>
                        <a href={`tel:${header.phone}`} target="_blank" rel="noopener noteferrer">{header.phone}</a>
                    </ListGroupItem>

                    <ListGroupItem>
                        <a href={`mailto:${header.email}`} target="_blank" rel="noopener noteferrer">{header.email}</a>
                    </ListGroupItem>

                    {header.github &&
                        <ListGroupItem>
                            <a href={header.github} target="_blank"
                               rel="noopener noreferrer">{block_names.github_title}</a>
                        </ListGroupItem>
                    }
                    {header.linkedin &&
                        <ListGroupItem>
                            <a href={header.linkedin} target="_blank"
                               rel="noopener noreferrer">{block_names.linkedin_title}</a>
                        </ListGroupItem>
                    }

                    {(header.country || header.city || header.district) && (
                        <ListGroupItem className="d-flex flex-wrap gap-3">

                            {header.country &&
                                <div><span className="title">{block_names.country_title}</span>: {header.country}</div>
                            }

                            {header.city &&
                                <div><span className="title">{block_names.city_title}</span>: {header.city}</div>
                            }

                            {header.district &&
                                <div><span className="title">{block_names.district_title}</span>: {header.district}
                                </div>
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