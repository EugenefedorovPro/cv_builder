import React from "react";
import {ListGroup, ListGroupItem} from "react-bootstrap";
import {useFetchData} from "../api/UseFetchData";

type BlockNameObject = {
    block_name: string;
}

interface ExperienceItemInterface {
    id: number;
    company: string;
    position: string;
    start_date: string;
    end_date?: string;
    achievements: string;

}

const ExperienceCV = () => {
    const name = "Experience"
    const url: string = "http://localhost:8002/experience/";
    const {data, loading, error} = useFetchData<[BlockNameObject, ExperienceItemInterface[]]>(url);

    if (loading) {
        return <div> Loading data for {name}...</div>
    }

    if (error) {
        return <div>`Error on fetching {name}: ${error}`</div>

    }

    if (!data) {
        return <div>No data on {name}</div>

    }

    const [block_name, data_experience] = data;

    return (
        <>
            <ListGroup>
                <ListGroupItem className="block-name">{block_name.block_name}</ListGroupItem>
            </ListGroup>

            <ListGroup>
                {
                    data_experience.map((item) => (
                        <ListGroupItem className="experience-items">
                            <span className="title">Company</span> {item.company}<br/>
                            <span className="title">Period</span> {item.start_date} - {item.end_date ? item.end_date : "current"}<br/>
                            <span className="title">Position</span> {item.position}<br/>
                            <span className="title">Achievements</span><br/>
                            <span>{item.achievements}</span>
                        </ListGroupItem>
                    ))
                }
            </ListGroup>
        </>

    )
}


export default ExperienceCV;
