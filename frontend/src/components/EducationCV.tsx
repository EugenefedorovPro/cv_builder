import React from "react";
import {ListGroup, ListGroupItem} from "react-bootstrap";
import {useFetchData} from "../api/UseFetchData";

interface BlockNamesInterface {
    education_name: string;
}

interface EducationItemInterface {
    id: number;
    institution: string;
    start_date: string;
    end_date: string;
    degree_title: string;

}

interface EducationBlockInterface {
    education: EducationItemInterface[];
    block_names: BlockNamesInterface;
}

const EducationCV = () => {
    const name = "Education"
    const url: string = "http://localhost:8002/education/";
    const {data, loading, error} = useFetchData<EducationBlockInterface>(url);

    if (loading) {
        return <div> Loading data for {name}...</div>
    }

    if (error) {
        return <div>`Error on fetching {name}: ${error}`</div>

    }

    if (!data) {
        return <div>No data on {name}</div>

    }

    const {education, block_names} = data;

    if (!education || !block_names) {
        return <div>No data on {name}</div>

    }

    return (
        <>
            <ListGroup>
                <ListGroupItem className="block-name">{block_names.education_name}</ListGroupItem>
            </ListGroup>

            <ListGroup>
                {
                    education.map((item) => (
                        <ListGroupItem className="education-items">
                            <span className="title">{item.institution}</span><br/>
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
