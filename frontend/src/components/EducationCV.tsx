import React from "react";
import {ListGroup, ListGroupItem} from "react-bootstrap";
import {useFetchData} from "../api/UseFetchData";

type BlockNameObject = {
    block_name: string;
}

interface EducationItemInterface {
    id: number;
    institution: string;
    start_date: string;
    end_date: string;
    degree_title: string;

}

const EducationCV = () => {
    const name = "Education"
    const url: string = "http://localhost:8002/education/";
    const {data, loading, error} = useFetchData<[BlockNameObject, EducationItemInterface[]]>(url);

    if (loading) {
        return <div> Loading data for {name}...</div>
    }

    if (error) {
        return <div>`Error on fetching {name}: ${error}`</div>

    }

    if (!data) {
        return <div>No data on {name}</div>

    }

    const [block_name, data_education] = data;

    return (
        <>
            <ListGroup>
                <ListGroupItem className="block-name">{block_name.block_name}</ListGroupItem>
            </ListGroup>

            <ListGroup>
                {
                    data_education.map((item) => (
                        <ListGroupItem className="education-items">
                            <strong>{item.institution}</strong><br/>
                            {item.start_date} - {item.end_date}<br/>
                            {item.degree_title}
                        </ListGroupItem>
                    ))
                }
            </ListGroup>
        </>

    )
}


export default EducationCV;
