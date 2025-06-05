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
    const url: string = "http://localhost:8002/education/";
    const {data, loading, error} = useFetchData<[BlockNameObject, EducationItemInterface[]]>(url);

    if (loading) {
        return <div> Loading data for Hard Skills...</div>
    }

    if (error) {
        return <div>`Error on fetching Hard Skills: ${error}`</div>

    }

    if (!data) {
        return <div>No data on Education</div>

    }

    const [block_name, data_education] = data;

    return (
        <>
            <ListGroup>
                <ListGroupItem className="accent">{block_name.block_name}</ListGroupItem>
            </ListGroup>

            <ListGroup>
                {
                    data_education.map((item) => (
                        <ListGroupItem>
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
